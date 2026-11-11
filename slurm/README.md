# Generic Slurm templates

`python_script.sbatch` and `espnet_recipe.sbatch` are **examples only**. Replace `path/to/...`, partition, GPU requests, Conda activation and official training entrypoints according to your own cluster and installed software.

Do not submit an example unchanged. Training weights, experiment logs, dataset files and other outputs should stay in private directories.

Slurm is a cluster scheduler; local machines or Google Colab may not use it.
