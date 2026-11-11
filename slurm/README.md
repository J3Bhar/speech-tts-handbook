# Generic Slurm templates

`python_script.sbatch`, `espnet_recipe.sbatch`, `mfa_validate.sbatch`, and `mfa_align.sbatch` are **examples only**. The MFA pair is described in the [MFA runbook](../docs/alignment/run-mfa.md). Replace `path/to/...`, partition, GPU requests, Conda activation and official training entrypoints according to your own cluster and installed software.

Do not submit an example unchanged. Training weights, experiment logs, dataset files and other outputs should stay in private directories.

Slurm is a cluster scheduler; local machines or Google Colab may not use it.

## Model-specific wrappers

- `fastspeech2.sbatch`
- `tacotron2.sbatch`
- `vits.sbatch`
- `f5-tts.sbatch`

These require `TTS_RECIPE_DIR` and `TTS_RUN_SCRIPT` to point to **your own reviewed official recipe**. They start in **dry-run mode**. Only set `TTS_CONFIRM_RUN=YES` after reviewing and configuring the exact upstream script and all cluster-specific resource directives. **Do not assume the recipe script works for every model or release.**
