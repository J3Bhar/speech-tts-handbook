# General-purpose data-checking utilities

These small scripts are freshly authored educational examples, not copies of private training code.

Run any helper with `--help` to see its input format. You must replace `path/to/...` with your own files.

| Script | Purpose |
| --- | --- |
| `audit_corpus.py` | Check text/WAV pairs |
| `split_corpus.py` | Make reproducible train/dev/test ID lists |
| `check_text.py` | Check tokens against vocabulary |
| `check_durations.py` | Validate durations against mel frames |
| `check_mels.py` | Check mel array shapes |
| `check_wav.py` | Check WAV header and signal |
| `audit_textgrids.py` | Check for TextGrid files |
| `mfa_prepare.py` | Make MFA WAV/TXT pairs from a TSV manifest |
| `mfa_check_corpus.py` | Validate WAV/TXT pairs |
| `mfa_check_textgrids.py` | Check expected TextGrids and phone tiers |
| `publication_audit.py` | Flag potentially private files/paths |

[**Follow the complete MFA runbook**](../docs/alignment/run-mfa.md) for the correct order and the Slurm templates.

Always manually check outputs. Passing an automated test **does not** guarantee acoustic alignment, pronunciation, naturalness or permission to redistribute data.
