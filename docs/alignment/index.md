---
title: Montreal Forced Aligner
---

# Montreal Forced Aligner (MFA)

**What is it?** A forced aligner estimates the time when transcript words and dictionary phones occur in a recording. Many duration-supervised models use such timing information.

## Workflow

1. Prepare clean paired audio and transcripts.
2. Select a compatible language-specific pronunciation dictionary and acoustic model.
3. Install the versioned upstream [MFA release](https://montreal-forced-aligner.readthedocs.io/).
4. Use `mfa validate --help` and `mfa align --help` to inspect supported arguments.
5. Validate a small sample first and view TextGrid tiers in Praat.
6. Check phone order and *listen* to the boundaries before using durations downstream.

```bash
CORPUS_DIR="path/to/corpus"       # Your paired audio/transcript folder
DICT="path/to/dictionary.dict"   # A reviewed pronunciation dictionary
ACOUSTIC="path/to/model"         # Compatible acoustic model
OUT="path/to/textgrids"          # New output folder
```

Do **not** reuse a Hindi G2P/dictionary unchanged for Indian English, or assume every English accent shares the same pronunciations. MFA phone intervals are measured in **seconds**. A TTS duration target may need conversion into mel **frames** using the selected model's hop length.

[Official MFA source](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) · [Troubleshooting](../troubleshooting/)
