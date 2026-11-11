# Generic Slurm templates

`python_script.sbatch`, `espnet_recipe.sbatch`, `mfa_validate.sbatch`, and `mfa_align.sbatch` are **examples only**. The MFA pair is described in the [MFA runbook](../docs/alignment/run-mfa.md). Replace `path/to/...`, partition, GPU requests, Conda activation and official training entrypoints according to your own cluster and installed software.

Do not submit an example unchanged. Training weights, experiment logs, dataset files and other outputs should stay in private directories.

Slurm is a cluster scheduler; local machines or Google Colab may not use it.
