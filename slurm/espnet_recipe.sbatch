#!/bin/bash
#SBATCH --job-name=espnet-example
#SBATCH --output=path/to/logs/espnet-%j.out
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
# Customize scheduler resources and request GPUs only as needed.
set -euo pipefail
cd "path/to/espnet/egs2/your_corpus/tts1"  # Replace with your installed recipe folder
bash ./run.sh --help  # Consult the exact version's recipe options before training
