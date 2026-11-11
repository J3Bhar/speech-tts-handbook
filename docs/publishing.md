---
title: Safe publication checklist
---

# Publish safely

Before committing a TTS project, check that it contains **only material you are permitted to share**.

1. Replace personal/organization server paths with `path/to/...` examples and explanatory comments.
2. Do not commit WAVs, speaker identities, licensed data, trained checkpoints or unreleased findings.
3. Do not publish API keys, passwords, tokens, environment dumps or internal URLs.
4. Cite official upstream sources and preserve license notices when reusing code.
5. Check all files and **Git history**, not only the newest README.
6. For a clean public release, start from an **empty Git repository** rather than copying an old `.git` directory.

Deleting old public commits does not guarantee previously accessed copies or caches disappear. A scanner is only an aid; manual review is essential.

[Home](./)
