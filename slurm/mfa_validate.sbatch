#!/bin/bash
#SBATCH --job-name=mfa-validate
#SBATCH --time=02:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
# Set cluster partition/account directives according to your own site.
set -euo pipefail
: "${MFA_CORPUS:?Set MFA_CORPUS to path/to/mfa_corpus}"
: "${MFA_DICT:?Set MFA_DICT to a compatible dictionary path/name}"
: "${MFA_ACOUSTIC:?Set MFA_ACOUSTIC to an MFA acoustic model path/name}"
command -v mfa >/dev/null || { echo 'MFA is not on PATH; activate its environment'; exit 1; }
# MFA 3.x legacy command. Verify 'mfa validate --help' for installed version.
mfa validate "$MFA_CORPUS" "$MFA_DICT" --acoustic_model_path "$MFA_ACOUSTIC"
