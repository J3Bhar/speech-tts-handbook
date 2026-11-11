---
title: Prepare speech data
---

# Preparing audio and transcripts

Every TTS training example needs a **recording** and the **words actually spoken in it**.

```text
path/to/dataset/
  wavs/example_001.wav
  wavs/example_002.wav
  transcripts.txt
```

The directory and filenames are fictional examples; replace them with your own.

## Beginner checklist

1. Listen to a few recordings; is the speech correct and understandable?
2. Ensure the same utterance ID appears in the WAV filename and its transcript.
3. Confirm the selected training recipe supports your audio sample rate and channel format.
4. Normalize spelling, numerals, abbreviations, punctuation and code-switching consistently.
5. Split examples into train, validation and test sets without duplicate leakage; consider speaker-disjoint splits when evaluating speakers.
6. Preserve originals and write processed data into a separate output directory.

**Before training:** use `python scripts/audit_corpus.py --help` from the repository root, then run the checker on your **own** test corpus. A file check cannot replace human transcription review.

[Next: input symbols](../text/)
