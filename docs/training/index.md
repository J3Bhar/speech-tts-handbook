---
title: TTS model training
---

# Choose the right model

| Model | Type | Output |
| --- | --- | --- |
| [FastSpeech2](../models/fastspeech2/) | Non-autoregressive, duration-aware acoustic model | Mels → vocoder |
| [Tacotron2](../models/tacotron2/) | Attention-based autoregressive acoustic model | Mels → vocoder |
| [VITS](../models/vits/) | Integrated end-to-end synthesis | Speech waveform |
| [F5-TTS](../models/f5-tts/) | Flow-matching/reference-conditioned synthesis | Speech waveform with its inference pipeline |

## The safe training order

1. Audit your data and choose a frontend (phones or written characters).
2. Choose an official recipe and **pin its commit/version**.
3. Prepare token lists, manifests and any alignments required by the model.
4. Examine the training configuration; ensure feature settings match your audio and output path.
5. Run a tiny smoke test; inspect finite loss and a saved checkpoint.
6. Train and monitor validation; keep best weights, latest resume state and configuration privately.
7. Run unseen-sentence tests with exactly the same frontend.
8. Compare intelligibility, missing words, prosody and waveform quality.

**Do not copy a Slurm script unchanged onto a different cluster.** Paths, GPUs, scheduler directives and software environments vary.

[Models and official links](../credits.html) · [Inference](../inference/)
