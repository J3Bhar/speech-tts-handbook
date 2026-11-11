---
title: VITS
---

# VITS: beginner guide

**What is it?** VITS is an end-to-end TTS model with integrated waveform generation.

## Step-by-step learning path

1. Install a versioned **official implementation**: [upstream source](https://github.com/jaywalnut310/vits).
2. Prepare correctly paired and licensed audio/transcripts.
3. Select phone-derived or written-character input **before** generating tokens.
4. Inspect the selected recipe's training data format and configuration.
5. Run preprocessing and a small smoke test, checking that losses are finite.
6. Train with validation and preserve the matching config/checkpoint.
7. Synthesize unseen sentences using the training frontend.
8. Inspect audio quality and diagnose shortcomings before changing the model.

```bash
MODEL_DIR="path/to/vits"            # Replace with your model installation
DATA_DIR="path/to/dataset"           # Replace with an authorized dataset
CONFIG="path/to/config.yaml"         # Replace with the recipe's real config
OUT="path/to/training_outputs"        # Replace with a writable results folder
```

**Important check:** Check speaker, frontend, alignment and waveform settings.

**Typical output:** The model produces speech without a separate HiFi-GAN in its standard inference path.

### Problems that might occur

- **Missing input files:** review corpus manifest paths and permissions.
- **Unknown symbols:** check tokenization and vocabulary.
- **Unstable training:** inspect audio consistency, data shapes, loss and learning rate.
- **Unexpected pronunciation or prosody:** verify frontend and decoding before retraining.

Command flags and configs vary by release. This page is educational, **not a claim to have trained every possible version**.

[Models](../../training/) · [Inference](../../inference/)
