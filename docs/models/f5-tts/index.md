---
title: F5-TTS — execution and revision
---

# F5-TTS: learn, train, revise

**Idea:** Flow-matching/reference-conditioned TTS. Use official reference-audio/text workflow and verify source audio and usage rights.

## Before running

1. Obtain licensed recordings and matching transcripts; audit them using [data preparation](../../data-preparation/).
2. Choose a **phoneme-derived** or **character-based** input representation; do not mix the two. Read [tokenization](../../text/).
3. Install a pinned version of the [official implementation](https://github.com/SWivid/F5-TTS) and read its exact training recipe.
4. Prepare manifests, vocabulary, any durations and features **required by that recipe**.
5. Run a tiny preprocessing/training batch and inspect the resulting logs.

## Practical training sequence

1. Use the official recipe's training script and configuration. Record the software version and **actual command** in your private experiment log.
2. Choose a new output directory and confirm disk/GPU resources.
3. Submit a reviewed training command locally or via [our generic Slurm wrapper](../../../slurm/f5-tts.sbatch).
4. Check the first batches for valid features and finite losses before leaving the job running.
5. Preserve the configuration, token vocabulary, best checkpoint, full resume state and logs in your private workspace.
6. Run the installed model's official inference command on **unseen sentences** with the identical text frontend.
7. Inspect the model's own waveform output.

```bash
export TTS_RECIPE_DIR="path/to/recipe"       # Replace with your installed recipe folder
export TTS_RUN_SCRIPT="path/to/recipe/run.sh" # Replace with the actual upstream entrypoint
# First check the Slurm wrapper and upstream command.
sbatch slurm/f5-tts.sbatch
# To enable execution after verifying your script, see slurm/README.md.
```

### What should you see?

| Stage | Expected output | Troubleshooting |
| --- | --- | --- |
| Preparation | Input manifests, token list/features | Missing WAVs, unknown tokens, split overlap |
| Smoke test | A short log with finite training loss | Environment, data shape, memory |
| Full training | Checkpoints and validation logs | Divergence, overwrites, checkpoint mismatch |
| Inference | Generated speech WAV | Missing words, odd timing, voice quality |

## Five points for quick revision

**Architecture:** Flow-matching/reference-conditioned TTS. **Inputs:** paired speech/text with matching frontend. **Key challenge:** Use official reference-audio/text workflow and verify source audio and usage rights. **Training:** versioned official recipe. **Evaluation:** test short and long unseen text, listen, verify WAV properties.

**Scope:** These are reusable templates; model-specific preprocessing and training arguments **must come from the actual installed upstream version**. The public repository includes no private training recipe or research results.

[All model guides](../../training/) · [Inference](../../inference/) · [Troubleshooting](../../troubleshooting/) · [Official source](https://github.com/SWivid/F5-TTS)
