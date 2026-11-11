# Speech & TTS: Beginner's Handbook

A beginner-friendly Speech & TTS handbook with a **clear, step-by-step learning path from data preparation to model training, vocoding, inference, and evaluation**.

This is a **universal educational repository**, not a publication of anyone's research, dataset, private server, checkpoint, experiment results, or unpublished model implementation.

## Follow the learning path

1. [Prepare speech recordings](docs/data-preparation/index.md)
2. [Understand phone-based vs character-based inputs](docs/text/index.md)
3. [Learn forced alignment with MFA](docs/alignment/index.md)
4. [Train with a matching official recipe](docs/training/index.md):
   [FastSpeech2](docs/models/fastspeech2/index.md) · [Tacotron2](docs/models/tacotron2/index.md) · [VITS](docs/models/vits/index.md) · [F5-TTS](docs/models/f5-tts/index.md)
5. [Understand HiFi-GAN vocoding](docs/vocoder/index.md)
6. [Generate an unseen speech WAV](docs/inference/index.md)
7. [Check common issues](docs/troubleshooting/index.md)

Each page aims to answer: **What is this? Why does it matter? What do I need? What do I run or check? What could go wrong?**

## General-purpose helper scripts

| Script | Purpose |
| --- | --- |
| [audit_corpus.py](scripts/audit_corpus.py) | Check paired audio/text and basic WAV health |
| [split_corpus.py](scripts/split_corpus.py) | Generate non-overlapping train/dev/test IDs |
| [check_text.py](scripts/check_text.py) | Compare model symbols with a token vocabulary |
| [check_durations.py](scripts/check_durations.py) | Check token/duration counts against mel frames |
| [check_mels.py](scripts/check_mels.py) | Inspect .npy mel arrays |
| [check_wav.py](scripts/check_wav.py) | Check output WAV integrity |
| [audit_textgrids.py](scripts/audit_textgrids.py) | Verify that TextGrid files are present and readable |
| [publication_audit.py](scripts/publication_audit.py) | Flag likely private paths or unsafe file types |

These are independent educational checks. **They are not replacements for the original training scripts** of upstream TTS frameworks.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
python scripts/audit_corpus.py --help
python -m unittest discover -s tests -v
```

## Replace example paths

```bash
DATA_DIR="path/to/dataset"             # Replace with YOUR dataset directory
MODEL_DIR="path/to/model"               # Replace with YOUR model checkout
CONFIG="path/to/model_config.yaml"     # Replace with YOUR saved configuration
OUTPUT_DIR="path/to/outputs"           # Replace with YOUR writable output folder
```

## Publication and ownership

The model implementations belong to their [original developers](docs/credits.md). Use official installation instructions and **check software, checkpoint, voice and dataset licenses separately**. No real research recordings or trained weights are distributed here. See the [publication checklist](docs/publishing.md).

## GitHub Pages

This repository is designed for `main` → `/docs` under **Settings → Pages**. GitHub Pages deployment must be enabled by an authorized repository administrator.
