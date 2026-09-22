"""System 3: an AI agent. LLM + tools + loop."""

import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = (
    "You are a college fee assistant. Never guess a fee: always use get_course_fee. "
    "Use calculator for any arithmetic. Available course codes: CS101, AI202, DS303. "
    "If no tool is needed, answer directly."
)


def agent(question, max_steps=6, verbose=True):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": question}
    ]

    for step in range(1, max_steps + 1):

        # 1. REASON: ask the LLM what to do next
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            tool_choice="auto",
            parallel_tool_calls=False,
            temperature=0,
            extra_body={
                "disable_tool_validation": True
            }
        )

        message = response.choices[0].message

        # 2. If no tool is requested, the LLM has finished
        if not message.tool_calls:
            return message.content.strip()

        # Prepare normalized tool calls
        normalized_tool_calls = []

        for call in message.tool_calls:

            # Groq may sometimes return:
            # calculator<|channel|>commentary
            # Convert it to:
            # calculator
            tool_name = call.function.name.split("<|")[0].strip()

            normalized_tool_calls.append({
                "id": call.id,
                "type": "function",
                "function": {
                    "name": tool_name,
                    "arguments": call.function.arguments
                }
            })

        # Add the assistant's tool request to conversation
        messages.append({
            "role": "assistant",
            "content": message.content or "",
            "tool_calls": normalized_tool_calls
        })

        # 3. ACT and OBSERVE: run each tool
        for call in message.tool_calls:

            # Normalize the tool name
            name = call.function.name.split("<|")[0].strip()

            # Read arguments
            arguments = json.loads(
                call.function.arguments or "{}"
            )

            # Find the Python function
            function = TOOL_FUNCTIONS.get(name)

            # Execute tool
            result = (
                function(**arguments)
                if function
                else f"Unknown tool: {name}"
            )

            # Show tool execution
            if verbose:
                print(
                    f"   step {step}: "
                    f"{name}({arguments}) -> {result}"
                )

            # Send tool result back to LLM
            messages.append({
                "role": "tool",
                "tool_call_id": call.id,
                "content": result
            })

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":

    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", agent(question))
        print("-" * 70)