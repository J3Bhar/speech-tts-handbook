---
title: Text-to-speech inference
---

# Inference: make your model read a new sentence

1. Load the checkpoint and **the exact saved training configuration**.
2. Normalize text and tokenize using the frontend the model learned.
3. For phoneme-derived models, run the matching pronunciation dictionary/G2P and symbol mapping.
4. Check unknown tokens instead of silently accepting them.
5. Use the installed model's version-compatible inference script.
6. If it predicts mels, run a compatible vocoder. If it predicts a waveform, save it directly.
7. Listen for incorrect words, missing endings, long pauses, noise and sample-rate mistakes.

```bash
CHECKPOINT="path/to/checkpoint"       # Replace with your trained weights
CONFIG="path/to/config"               # Replace with matching model configuration
TEXT="path/to/test_sentences.txt"     # Replace with new sentences
OUT="path/to/generated_wavs"          # Replace with an output folder
```

Inference is **not** completed just because the file exists: listen to unseen examples and check pronunciation.

[HiFi-GAN](../vocoder/) · [Troubleshooting](../troubleshooting/)
