---
title: Run a complete MFA alignment workflow
---

# MFA: a beginner's runbook (version 3.x legacy workflow)

These are **new universal templates**, not private research scripts. **Version note:** the validation command uses `--acoustic_model_path` on MFA 3.x. Confirm the syntax with your installed version's `mfa validate --help`. The positional forms may change in other versions. MFA 3.x uses four positional arguments for `mfa align`: corpus, dictionary, acoustic model and output directory. The official MFA documentation documents this syntax; the newer 3.4+ model format introduces alternatives, so **check your installed version**. <https://montreal-forced-aligner.readthedocs.io/en/latest/user_guide/workflows/alignment.html>

## 0. Prerequisites

- Install MFA using the official guide and verify `mfa --help`.
- Obtain **licensed data** and an appropriate pronunciation dictionary + compatible acoustic model for **your language**.
- Install Python 3.9+ for the helper scripts. `praatio` is required for TextGrid checking: `python -m pip install praatio`.
- Slurm is only needed if you're using a Slurm cluster. All core MFA CLI commands can also run locally.

## 1. Create a tiny manifest

A tab-separated file has these columns **without a header**:

```text
example_001<TAB>path/to/wav/example_001.wav<TAB>Hello world<TAB>speaker_001
example_002<TAB>path/to/wav/example_002.wav<TAB>How are you<TAB>speaker_001
```

Replace the literal `<TAB>` with an actual tab character. WAV paths are resolved relative to the manifest directory. Use a reviewed transcript with the words spoken in the recording, and select a dictionary appropriate to its language.

## 2. Prepare a new MFA corpus

```bash
python scripts/mfa_prepare.py \
  --manifest "path/to/manifest.tsv" \
  --output "path/to/new_mfa_corpus" --dry-run
# After dry-run succeeds:
python scripts/mfa_prepare.py \
  --manifest "path/to/manifest.tsv" \
  --output "path/to/new_mfa_corpus"
```

This creates `speaker_001/example_001.wav` and `speaker_001/example_001.txt` with matching names, copying WAVs rather than modifying the originals. It refuses to overwrite an existing output path.

## 3. Check the corpus

```bash
python scripts/mfa_check_corpus.py --corpus "path/to/new_mfa_corpus"
```

**PASS** requires readable PCM WAVs, matching TXT files and nonempty transcripts. A file-level PASS does **not** ensure that every word is accurately transcribed.

## 4. Validate with MFA before alignment

On a local machine running MFA 3.x:

```bash
mfa validate "path/to/new_mfa_corpus" \
  "path/to/dictionary.dict" \
  --acoustic_model_path "path/to/acoustic_model"
```

Read the validator output and fix any unreadable files, speaker grouping errors or out-of-vocabulary (OOV) pronunciations. **Don't proceed until validation succeeds.**

For Slurm, first activate the correct MFA environment on the compute node, then customize the directives inside `slurm/mfa_validate.sbatch` and run:

```bash
export MFA_CORPUS="path/to/new_mfa_corpus"       # Your prepared corpus
export MFA_DICT="path/to/dictionary.dict"        # Reviewed pronunciation lexicon
export MFA_ACOUSTIC="path/to/acoustic_model"     # Compatible installed MFA model
sbatch --export=ALL slurm/mfa_validate.sbatch
```

Check the output job log using the job ID Slurm prints. Do not assume submission means success.

## 5. Run alignment after validation passes

Locally:

```bash
mfa align "path/to/new_mfa_corpus" \
  "path/to/dictionary.dict" \
  "path/to/acoustic_model" \
  "path/to/new_textgrids"
```

Or on Slurm, **after the validation job completed successfully**:

```bash
export MFA_OUTPUT="path/to/new_textgrids"    # MUST NOT exist already
sbatch --export=ALL slurm/mfa_align.sbatch
```

The sample jobs are intentionally separated so you must inspect validation before spending resources on alignment. They do not modify training checkpoints.

## 6. Check TextGrids

```bash
python scripts/mfa_check_textgrids.py \
  --corpus "path/to/new_mfa_corpus" \
  --textgrids "path/to/new_textgrids" --tier phones
```

The checker tests presence and basic interval structure, **not** phone correctness or boundary accuracy. Inspect representative outputs in Praat and listen to the audio.

## 7. Hand off to TTS

MFA TextGrid times are in **seconds**. FastSpeech2-style duration supervision usually requires mapping phones or character tokens to **integer mel frames**, trimming audio consistently, and verifying duration sums. That processing is **model/recipe-specific**; never insert TextGrid seconds directly as duration targets.

### Common situations

| What might happen | What to check |
| --- | --- |
| WAV file has no TXT | The ID/filename pairing in your manifest |
| OOV words | Normalize transcripts and add reviewed dictionary pronunciations |
| MFA reports phone-set mismatch | Dictionary/acoustic-model compatibility |
| No TextGrid | Job log, output path, alignment exit code |
| TextGrid exists but speech sounds wrong | Transcript, pronunciation and actual acoustic timing |
| A later TTS duration check fails | Token/silence conventions, trimming and mel hop settings |

[All alignment concepts](./) · [Official MFA guide](https://montreal-forced-aligner.readthedocs.io/) · [General troubleshooting](../troubleshooting/)
