#!/bin/sh
until curl -s http://localhost:11434; do
    echo "Waiting for Ollama server to start..."
    sleep 1
done

ollama pull gemma3

exec ollama serve &
