!image.png

## What is an Agent in AI?

An Agent is an AI system that can reason, plan, and interact with its environment to achieve user-defined objectives through a combination of reasoning, planning, and tool execution.

**Key Details:**

- An Agent has "agency" - the ability to interact with and modify its environment
- The core definition: "An Agent is a system that leverages an AI model to interact with its environment in order to achieve a user-defined objective"
- Agents combine reasoning, planning, and action execution (typically through external tools)

**The Agent Architecture:**

| Component | Function | Example |
| --- | --- | --- |
| AI Model | Handles reasoning and planning | LLMs like GPT-4, Llama, Gemini |
| Action Space | Defines possible actions available to the agent | "send email", "search web", "calculate" |
| Tools | Physical or digital interfaces that execute actions | Coffee machine, email client, calculator |

**Common AI Models Used:**

- Large Language Models (LLMs): Best for text processing tasks
- Vision Language Models (VLMs): Handle text AND image inputs
- LLMs are the most common choice for contemporary agents

**How Agents Take Action:**

- LLMs can only generate text, but can use "tools" to perform external actions
- Examples: generating images, sending emails, controlling devices, searching web
- Tools are essential for agents to interact with the real world

**Real-World Applications:**

| Use Case | Functionality |
| --- | --- |
| Personal Virtual Assistants | Answer questions, set reminders, control smart devices |
| Customer Service Chatbots | Answer queries, troubleshoot issues, complete transactions |
| Video Game NPCs | Generate dynamic responses, adapt to player interactions, create natural dialogue |

**Why It Matters:**
Agents enable natural language interaction with AI systems, allowing them to understand human instructions, make informed decisions, and perform physical or digital actions in their environment - transforming how companies and individuals use AI technology.

---

## What are Large Language Models and How They Power AI Agents

This page explains what Large Language Models (LLMs) are, how they function, and their role in powering AI Agents.

**Key Details:**

- LLMs are AI models trained on vast text datasets to understand and generate human language
- Most LLMs use Transformer architecture with attention mechanism, typically having billions of parameters
- Three main Transformer types: Encoders, Decoders, and Seq2Seq (Encoder-Decoder) architectures
- LLMs work by predicting the next token in a sequence, using autoregressive generation until reaching EOS token
- Special tokens are used to structure generation (start/end of sequence, messages, etc.)

**Core Technologies:**

| Component | Function |
| --- | --- |
| **Tokenization** | Breaks text into units (typically 32,000 tokens instead of 600,000 words) |
| **Attention Mechanism** | Calculates importance of each word in a sentence for prediction |
| **Autoregressive Generation** | Output from previous token becomes input for next prediction |
| **Context Length** | Maximum number of tokens an LLM can process at once |

**Training Process:**

- **Pre-training**: Self-supervised learning to predict next word in sequence
- **Fine-tuning**: Supervised learning on specific tasks (conversation, coding, classification)

**Implementation Options:**

- Run locally (requires sufficient hardware)
- Use cloud/API (Hugging Face Serverless Inference API - primary method in this course)

**Why It Matters:**
LLMs serve as the "brain" of AI Agents, enabling them to interpret instructions, maintain conversation context, create plans, and select appropriate tools for complex tasks.

!image.png

attention mechanism

---

## Chat Templates: Structuring Conversations with LLMs

Chat templates are essential formatting systems that structure conversations between users and language models by converting multiple messages into a single prompt that the model can understand.

!image.png

**Key Details:**

| Aspect | Description |
| --- | --- |
| **Core Function** | Convert user/assistant message exchanges into properly formatted prompts for LLMs |
| **Template Structure** | Use Jinja2 code to transform message lists into textual representations |
| **Message Types** | System messages (persistent instructions), user messages, and assistant responses |
| **Special Tokens** | Unique delimiters that indicate where user/assistant turns start and end |
| **Model Compatibility** | Ensures different LLMs receive correct formatting despite their unique token requirements |

**Conversation Flow:**

1. User sends message → Model responds
2. Model's response becomes new assistant message
3. System automatically concatenates all messages into single prompt
4. Template converts this into formatted input for the model

**Base vs. Instruct Models:**

| Model Type | Training Approach | Key Characteristic |
| --- | --- | --- |
| Base Model | Trained on raw text data | Predicts next token |
| Instruct Model | Fine-tuned for instructions | Follows conversation patterns |
| Example | SmolLM2-135M (base) | SmolLM2-135M-Instruct (fine-tuned) |

**Why It Matters:**
Chat templates maintain context across multi-turn conversations, ensure proper formatting for different LLMs, and enable consistent user-agent interactions by handling the conversion from message lists to the final prompt that the model actually consumes.

example with SmolLM2

```python
<|im_start|>system
You are a helpful AI assistant named SmolLM, trained by Hugging Face<|im_end|>
<|im_start|>user
I need help with my order<|im_end|>
<|im_start|>assistant
I'd be happy to help. Could you provide your order number?<|im_end|>
<|im_start|>user
It's ORDER-123<|im_end|>
<|im_start|>assistant
```

example with Llama 3.2

```java
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: December 2023
Today Date: 10 Feb 2025

<|eot_id|><|start_header_id|>user<|end_header_id|>

I need help with my order<|eot_id|><|start_header_id|>assistant<|end_header_id|>

I'd be happy to help. Could you provide your order number?<|eot_id|><|start_header_id|>user<|end_header_id|>

It's ORDER-123<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

Here’s a concise, interview-ready explanation you can use:

---

**"In short, chat templates are the formatting rules that let large language models understand conversations.**

Even though we chat with AI using messages like ‘user’ and ‘assistant’, the model doesn’t ‘remember’ the conversation. Instead, all messages are combined into one single prompt. Chat templates ensure this prompt is structured correctly with special tokens that tell the model where each message starts and ends.

There are two types of models:

- **Base models**, which just predict the next word, and
- **Instruct models**, which are fine-tuned to follow instructions and chat.

Each model uses its own unique template (like ChatML), so using the right one is critical. Tools like Hugging Face’s `apply_chat_template()` handle this automatically, turning a list of messages into the exact prompt format the model expects.

Without chat templates, multi-turn conversations would be chaotic or impossible, because the model wouldn’t know how to interpret who said what."

---

You can add:

> "Think of it like translating a conversation into a language the model speaks — without it, the AI would be confused about context and roles."
> 

This keeps it clear, technical but accessible, and shows you understand both the *why* and *how*.

---

Yes, exactly. That's the core mechanism.

**The short answer:**
Jinja2 code in the chat template doesn't just "know when to stop." It **structures the prompt** so the model can clearly see when an action (tool call) is needed and how to format that instruction.

Here is how it works in practice:

1. **Structured Delimiters:** The Jinja2 template inserts special tokens (like `<tool_call>` or `<|tool|>`) around the data. It tells the model: *"Everything between these tokens is a tool command, not a normal chat response."*
2. **Explicit Formatting:** If a tool needs parameters (e.g., `{"location": "Paris"}`), the template forces the model to output that data in a specific JSON structure within the prompt. Without the template, the model might just say "I'll search for Paris" as text, which the code can't parse.
3. **The "Stop" Signal:** The template often includes a specific **End-of-Sequence (EOS)** or **Stop Token** after the tool command. This signals the system: *"The model has finished its thought and issued a command. Stop generating text and execute the tool."*

**In a Job Interview Context:**

> "Chat templates use Jinja2 to wrap tool calls in specific tags and JSON structures. This ensures the model outputs a valid command rather than natural language. The template also includes stop tokens that signal the system to pause text generation and execute the tool immediately, bridging the gap between the model's text generation and the application's execution logic."
> 

**Example of what the template does:**
Without the template, the model might write:

> "I need to check the weather in London." (System doesn't know to call a tool).
> 

With the chat template (Jinja2), it formats it as:

```
<tool_call>
name: get_weather
arguments: {"city": "London"}
</tool_call>```
The system sees the `<tool_call>` tag, extracts the JSON, executes the tool, and feeds the result back into the conversation.
```