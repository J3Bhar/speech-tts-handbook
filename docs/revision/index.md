---
title: TTS revision and execution checklist
---

# TTS revision sheet for new scholars

Use this page before a GPU job, a meeting or an exam. See the [complete learning path](../).

## One flow to remember

```text
WAV + transcript → audit + normalization → choose phones or graphemes
      → MFA alignment when needed → train acoustic/end-to-end model
      → vocoder for mel-based models → unseen-text inference → evaluation
```

| Model | What it does | Check first |
| --- | --- | --- |
| MFA | Transcripts + WAV → word/phone intervals | Dictionary/model compatibility and TextGrids |
| FastSpeech2 | Non-autoregressive text → mel | Token-to-duration and frame totals |
| Tacotron2 | Attention-based text → mel | Attention, stop, missing/repeated words |
| VITS | Text → waveform | Token/speaker compatibility |
| F5-TTS | Reference-conditioned flow-matching TTS | Reference speech/text |
| HiFi-GAN | Mel → waveform | Mel scale, log base, mel filters, normalization |

## Before training: 10-second check

- Are WAV and transcript IDs paired, and are there duplicate or leaked splits?
- Are the sample rates and features compatible with the **chosen** recipe?
- Is the input **phoneme-derived or written-character**? Does it match the token list?
- Did the preprocessing/smoke test pass?
- Are checkpoint outputs in a **new** directory with enough storage?
- Are the model/software version and training command recorded?
- Is the environment properly configured and are you authorized to use the data?

## After training

- Preserve best, latest and full-resume checkpoint states privately.
- Reuse training text normalization at inference.
- Listen to short and long held-out examples.
- Use a compatible vocoder only when the model predicts mels.
- Record systematic errors and quality observations, not just the loss value.

## Execution links

[Data preparation](../data-preparation/) · [MFA runbook](../alignment/run-mfa.html) · [Model overview](../training/) · [Troubleshooting](../troubleshooting/)

The [Slurm wrappers](https://github.com/J3Bhar/speech-tts-handbook/tree/main/slurm) are **dry-run by default** and require a versioned upstream training script. The handbook does not distribute private code, weights or research results.
