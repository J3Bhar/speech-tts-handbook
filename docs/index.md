---
title: Speech and TTS Beginner's Handbook
---

# Speech & TTS: Beginner's Handbook

**Start with data, learn how the models work, and finish with a real WAV.** This handbook uses public concepts, generic paths, and official projects.

| Stage | Guide | What you learn |
| --- | --- | --- |
| 1 | [Audio & transcript preparation](data-preparation/) | Correct inputs, splits, sample rates |
| 2 | [Phone or character tokens](text/) | Frontends for different languages |
| 3 | [MFA alignment](alignment/) · [Run it step by step](alignment/run-mfa.html) | Word/phone boundaries and TextGrids |
| 4 | [Model training](training/) | Choose a versioned official recipe |
| 4a | [FastSpeech2](models/fastspeech2/) | Non-autoregressive mel prediction |
| 4b | [Tacotron2](models/tacotron2/) | Attention-based mel prediction |
| 4c | [VITS](models/vits/) | Integrated waveform model |
| 4d | [F5-TTS](models/f5-tts/) | Flow-matching TTS |
| 5 | [HiFi-GAN vocoding](vocoder/) | Convert mels into speech |
| 6 | [Inference](inference/) | Use a saved checkpoint on new text |
| 7 | [Troubleshooting](troubleshooting/) | Diagnose common problems |\n| 8 | [Quick revision sheet](revision/) | Recall key concepts and checks before running jobs |

## Example path conventions

```bash
DATA_DIR="path/to/dataset"          # Replace with your own WAV/text data
MODEL_DIR="path/to/model"            # Replace with the official code checkout
OUTPUT_DIR="path/to/outputs"        # Replace with a writable output directory
```

**Remember:** ESPnet `token_type=char` can represent *written characters* or *phones encoded as characters*. These are **not the same input format**.

[Project credits and licenses](credits.html) · [Publication checklist](publishing.html)
