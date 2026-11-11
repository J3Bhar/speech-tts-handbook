---
title: Possible problems and solutions
---

# What might go wrong?

| Problem | First thing to check | Possible fix |
| --- | --- | --- |
| Audio/text pairing fails | Recording IDs and transcript list | Fix missing/duplicate pairs |
| MFA cannot align | Dictionary OOVs and model phone inventory | Review pronunciations and match resources |
| Phone-based model reads nonsense | Text representation/tokenizer | Use the exact training G2P and phone mapping |
| Duration mismatch | Tokens, intervals and mel frames | Recalculate durations from consistent boundaries |
| Low-quality waveform | Mel/vocoder compatibility | Compare sample rate, FFT/hop and log convention |
| Missing or repeated words | Attention or decoding stop rules | Inspect output behavior before retraining |
| GPU out of memory | Batch size, long utterances and padding | Reduce batch/sequence length |
| Wrong accent or speaker | Training/reference conditions | Verify conditioning and sample identity |
| Training won't resume | Last checkpoint and optimizer state | Restore full matching resume state |

Start with **data and input formats** before changing a trained model. Use small test batches to make problems easier to reproduce.

[Start again](../) · [Official sources](../credits.html)
