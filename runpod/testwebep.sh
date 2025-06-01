#!/bin/sh
vllmep="https://oy4r315fxeteec-8000.proxy.runpod.net"
#vllmep="http://localhost:8000"
# Call the server using curl:
model="unsloth/Llama-3.2-11B-Vision-Instruct"
curl -X POST "${vllmep}/v1/completions" \
	-H "Content-Type: application/json" \
	--data '{
		"model": "neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8",
		"prompt": "Once upon a time,",
		"max_tokens": 512,
		"temperature": 0.5
	}'
