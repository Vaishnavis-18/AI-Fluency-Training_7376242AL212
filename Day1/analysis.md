# Day 1 Assessment: Plain Chatbot vs Rule-Based Workflow vs AI Agent

## 1. Scenario

The private-data scenario is a **college course-fee assistant**. The application contains private course-fee data:

- **CS101:** Rs. 12,000
- **AI202:** Rs. 18,000
- **DS303:** Rs. 15,000

The same type of user request is handled using a plain chatbot, a rule-based workflow, and a tool-using AI agent.

## 2. Plain Chatbot

A plain chatbot mainly uses an LLM to understand a user's question and generate a response. In this implementation it has no dedicated course-fee lookup tool or calculator.

For example, if the user asks, "What is the fee for AI202?", the chatbot generates an answer from the information available to the model. It does not automatically retrieve the application's private course-fee dictionary. Therefore, private course-fee data is not reliably accessible unless it is explicitly supplied as prompt/context.

The chatbot is simple and flexible for general language questions, but it cannot independently verify private numerical data or use application-side tools in this implementation.

## 3. Rule-Based Workflow

A rule-based workflow does not use an LLM. It follows predefined steps and conditions written by the programmer.

For this scenario, the workflow can check a course code against the private fee dictionary. For a multi-step request, the programmer can explicitly define the sequence: retrieve the fees, add them, calculate the scholarship, and produce the result.

This approach can directly access the private data and gives predictable results for programmed cases. Its limitation is flexibility: new wording, conditions, or task sequences may require additional rules and programming.

## 4. AI Agent

An AI agent combines an **LLM + Tools + Loop**. The LLM interprets the request and selects an appropriate tool. The tool performs an operation using private application data, the result is returned to the LLM, and the agent can continue the loop until the task is completed.

This scenario uses two tools: a **course-fee lookup tool** and a **calculator**. For example, for "What is the total fee for CS101 and AI202 after a 10% scholarship?", the agent can retrieve both fees, calculate their total, calculate the scholarship reduction, and return the final result.

The agent therefore combines natural-language understanding with private-data access and multi-step tool use. Its limitation is greater system complexity and dependence on correct model/tool-call behavior.

## 5. Comparison Table

| Basis for comparison | Plain chatbot | Rule-based workflow | AI agent |
|---|---|---|---|
| **Flexibility** | High for natural-language conversation, limited by information available to the LLM. | Lower; limited to predefined rules and cases. | High; can interpret requests and select available tools. |
| **Decision-making** | Generates an LLM response without application tool execution. | Decisions are explicitly programmed using conditions. | LLM selects tools and can continue through multiple steps. |
| **Tool usage** | No dedicated tools in this implementation. | Uses programmed functions/rules. | Uses course-fee lookup and calculator tools. |
| **Private-data access** | Not directly available in this implementation. | Direct through application data and rules. | Direct through tools connected to private data. |
| **Multi-step task handling** | Can explain steps but does not independently execute private-data operations. | Possible when the complete sequence is predefined. | Can perform multiple tool calls and use their results in a loop. |
| **Automation** | Limited in this implementation. | Strong for fixed, repetitive processes. | Strong for flexible tasks requiring tool actions. |
| **Reliability** | Depends on LLM response generation and available information. | Predictable for programmed cases. | Depends on correct tool selection, tool execution, and model behavior. |

## 6. Suitability Analysis

For this course-fee scenario, the **AI agent is the most suitable approach when the requirement is to handle varied user questions involving private data and multi-step calculations**. The agent can use the course-fee lookup tool to obtain private values and the calculator to perform arithmetic. It can also interpret different natural-language requests and decide which tools are needed.

A rule-based workflow is suitable when expected questions and processing steps are fixed. It provides predictable behavior and direct private-data access, but new types of requests require new rules. A plain chatbot is useful for conversational responses, but in this implementation it does not directly access the private course-fee data or perform application-side operations through tools.

Therefore, the appropriate choice depends on the task. A fixed process can use a rule-based workflow, while a task requiring natural-language flexibility together with private-data tool use can use an AI agent.

## 7. Conclusion

A plain chatbot, a rule-based workflow, and an AI agent solve problems differently. A plain chatbot is appropriate when the main requirement is natural-language interaction and response generation. A rule-based workflow is appropriate for predictable processes whose steps and conditions are known in advance.

An AI agent is appropriate for tasks that require an LLM to interpret a request, select tools, use external or private data, observe tool results, and continue through multiple steps until the task is completed. The key distinction is that an agent combines an LLM with tools and a loop so that it can take actions based on the task and the results of those actions.

For the course-fee scenario, the comparison demonstrates the importance of private-data access, tool usage, and multi-step handling when selecting among these three approaches.
