#!/bin/bash
#SBATCH --job-name=tacotron2-example
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
# Replace Slurm directives (including GPU, account, partition and walltime)
# according to your own environment; this is NOT a full training time estimate.
set -euo pipefail
: "${TTS_RECIPE_DIR:?Set TTS_RECIPE_DIR to path/to/your/official/recipe}"
: "${TTS_RUN_SCRIPT:?Set TTS_RUN_SCRIPT to the reviewed official training script}"
[[ -d "$TTS_RECIPE_DIR" ]] || { echo "Missing recipe directory"; exit 1; }
[[ -f "$TTS_RUN_SCRIPT" ]] || { echo "Missing training entrypoint"; exit 1; }
cd "$TTS_RECIPE_DIR"
echo "Model: Tacotron2"
echo "Training command: bash $TTS_RUN_SCRIPT"
# Safety default: do NOT start a long training run automatically.
if [[ "${TTS_CONFIRM_RUN:-NO}" != YES ]]; then
    echo "DRY RUN: review the official recipe and provide TTS_CONFIRM_RUN=YES to enable."
    exit 0
fi
bash "$TTS_RUN_SCRIPT"
