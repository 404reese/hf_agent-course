
# LLM Hardware, Ecosystem, and Performance Notes

## 1. Hardware Requirements for LLMs (Llama 3 70B Case Study)

### GPU Memory Composition
- **Model Weights/Parameters:** Fixed space.
- **KV Cache:** Dynamic; grows with every token generated per active request.

### Memory Breakdown for Llama 3 70B
- **Weights:** 140GB (at 2 bytes per parameter)
    - *Minimum:* 2x 80GB GPUs
    - *Practical deployment:* 4x 80GB GPUs (standard unit)
- **KV Cache (per long-context request):**
    - 32K tokens → requires **10GB** in KV cache
- **Scaling with 180GB KV cache:** Can serve ~18 long-context users in parallel
- **Naive serving setup:** Only supports 2–3 parallel users

### Total Memory Example (4x GPUs)
- Parameters: 180GB KV cache
- Total: 4 × 80GB = **320 GB**

> *Visual note:* One diagram shows GPU memory > 2×80GB for Llama 3 70B, with weights fixed and KV cache dynamic per request.

---

## 2. Evolution of the Open-Source AI Model Ecosystem

### Key Milestones (Jan 2023 – Aug 2025)

| Date | Models Released |
|------|----------------|
| Jan 2023 | RedPajama, MPT, Falcon |
| March 2023 | Llama (Meta) |
| July 2023 | Llama 2 |
| Sept 2023 | Mistral, Granite 2 |
| Nov 2023 | Zephyr |
| Jan 2024 | Mixtral, Phi-2 |
| March 2024 | DBRX, Phi3 |
| May 2024 | Llama 3, Qwen 2 |
| July 2024 | Gemma 2, Nemotron |
| Sept 2024 | DBRX, Granite 3, Qwen2-VL |
| Nov 2024 | Phi-3, Arctic |
| Jan 2025 | DeepSeek-R1 |
| Apr 2025 | Llama 4, Qwen 3 |
| May 2025 | Phi-4 reasoning |
| July 2025 | Kimi K2 |
| Aug 2025 | OpenAI gpt-oss |

### Key Organizations Involved
- Meta, AI2, Mistral AI, Databricks, IBM, Microsoft, Google, DeepSeek, NVIDIA, Hugging Face, Snowflake

---

## 3. Measurable Targets for LLM Reliability & Performance

### Accuracy Service Level Objectives (SLOs)
- Accuracy must exceed usability thresholds to avoid:
    - **Hallucinations** (inaccurate/incorrect outputs)
    - **Off-brand responses**

### Inference Performance SLOs

| Metric | Description |
|--------|-------------|
| **Time to First Token (TTFT)** | Time taken to generate the first output token |
| **Inter-Token Latency (ITL)** | Average time between consecutive tokens (excluding first) |
| **Request Latency** | Total end-to-end time |
| **Throughput** | Average number of output tokens generated per second across all requests |

### Example Benchmark: Llama 3.1 7B Instruct (FP8 vs BF16)

| Benchmark | BF16 | FP8 | Recovery |
|-----------|------|-----|----------|
| MMLU (5-shot) | 83.83 | 83.73 | 99.88% |
| MMLU-cot (0-shot) | 86.01 | 85.44 | 99.34% |
| ARC Challenge (0-shot) | 93.26 | 92.92 | 99.64% |
| GSM-8K-cot (8-shot) | 94.92 | 94.54 | 99.60% |
| Hellaswag (10-shot) | 86.75 | 86.64 | 99.87% |
| Winogrande (5-shot) | 85.32 | 85.95 | 100.7% |
| TruthfulQA (0-shot, mc2) | 60.68 | 60.84 | 100.2% |
| **Average** | **84.40** | **84.29** | **99.88%** |


graph TD
    subgraph "Hardware Requirements"
        A[GPU Memory] --> B[Model Weights<br/>Fixed: 140GB for Llama 70B]
        A --> C[KV Cache<br/>Dynamic: 10GB per 32K tokens]
        B --> D[Needs: 4x 80GB GPUs]
        C --> E[180GB cache → 18 parallel users]
        C --> F[Naive: only 2-3 users]
    end

    subgraph "Performance SLOs"
        G[Latency Metrics] --> H[TTFT<br/>Time to First Token]
        G --> I[ITL<br/>Inter-Token Latency]
        G --> J[Request Latency<br/>End-to-end]
        K[Throughput] --> L[Tokens/sec across all requests]
    end

    subgraph "Accuracy"
        M[Key Risks] --> N[Hallucinations]
        M --> O[Off-brand responses]
        P[Quantization Impact] --> Q[FP8 preserves ~99.88%<br/>accuracy vs BF16]
    end

    subgraph "Model Evolution Timeline"
        R[2023] --> S[Llama, Mistral, Falcon]
        T[2024] --> U[Llama 3, Mixtral, Gemma 2]
        V[2025] --> W[DeepSeek-R1, Llama 4,<br/>GPT-oss]
    end

    style A fill:#f9f,stroke:#333,stroke-width:2px
    style G fill:#bbf,stroke:#333,stroke-width:2px
    style M fill:#bfb,stroke:#333,stroke-width:2px