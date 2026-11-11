#!/bin/bash
#SBATCH --job-name=mfa-align
#SBATCH --time=08:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
# Site-specific partition/account/resource options belong here.
set -euo pipefail
: "${MFA_CORPUS:?Set MFA_CORPUS to path/to/mfa_corpus}"
: "${MFA_DICT:?Set MFA_DICT to a compatible dictionary path/name}"
: "${MFA_ACOUSTIC:?Set MFA_ACOUSTIC to an MFA acoustic model path/name}"
: "${MFA_OUTPUT:?Set MFA_OUTPUT to a NEW path/to/textgrids directory}"
[[ ! -e "$MFA_OUTPUT" ]] || { echo "Output exists; refuse to overwrite: $MFA_OUTPUT"; exit 1; }
command -v mfa >/dev/null || { echo 'MFA is not on PATH; activate its environment'; exit 1; }
# MFA 3.x legacy command. Verify 'mfa align --help' for installed version.
mfa align "$MFA_CORPUS" "$MFA_DICT" "$MFA_ACOUSTIC" "$MFA_OUTPUT"
