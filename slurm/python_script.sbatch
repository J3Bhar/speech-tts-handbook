#!/bin/bash
#SBATCH --job-name=tts-example
#SBATCH --output=path/to/logs/example-%j.out
#SBATCH --time=00:30:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
# Replace Slurm directives (including output path) with your cluster's values.
set -euo pipefail
cd "path/to/project"     # Replace with the directory containing your script
python "path/to/script.py" --help  # Replace with your tested program/arguments
