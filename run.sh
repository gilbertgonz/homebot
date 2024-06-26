#!/bin/bash

# Detect if GPU is available
gpu=$(lspci | grep -ci nvidia)

if ((gpu > 1)); then    
    echo "GPU detected."
    export USE_GPU=true
else
    echo "No GPU detected."
    export USE_GPU=false
fi

if [ "$USE_GPU" = true ]; then
    docker compose up web_gpu --remove-orphans -d
    echo "HomeBot up and running with human detection!"
else
    docker compose up web_cpu --remove-orphans -d
    echo "HomeBot up and running without human detection"
fi