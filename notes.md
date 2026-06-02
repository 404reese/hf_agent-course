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
