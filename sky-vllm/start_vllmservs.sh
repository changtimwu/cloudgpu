#!/bin/sh
# Terminal 1 - Start the language model server
python -m vllm.entrypoints.openai.api_server \
    --model nvidia/Llama-3.3-70B-Instruct-FP4 \
    --port 8000 \
    --gpu-memory-utilization 0.7

# Terminal 2 - Start the embedding model server
python -m vllm.entrypoints.openai.api_server \
    --model BAAI/bge-m3 \
    --port 8001 \
    --gpu-memory-utilization 0.3
