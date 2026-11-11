---
title: Phoneme-based and character-based TTS
---

# What should the model read: phones or characters?

Two TTS systems can share the same architecture but learn **different types of symbols**.

| Approach | Input represents | Before training | At inference |
| --- | --- | --- | --- |
| Phone-based | Pronounced sounds | Text → dictionary/G2P → phones | Reuse the same G2P/phone inventory |
| Character-based | Written letters or script characters | Normalized writing → tokens | Reuse the same normalization/token list |

## Why `token_type=char` doesn't necessarily mean grapheme TTS

ESPnet can be configured so that **each phone is encoded as a single Unicode character**. In that case, `token_type=char` tokenizes *phone-derived symbols*, not raw Hindi, English, or another written language. Avoid sending raw text into a model trained on custom encoded phones.

```text
Phone route: written text → pronunciation conversion → phones → model symbols
Char route:  written text → written-character normalization → model symbols
```

For **Hindi and other Indic scripts**, carefully handle vowel marks, script normalization and language-specific pronunciation. For **Indian English**, consider pronunciation of names, borrowed words, accents and code-switching. Always check unknown-token counts.

[Next: alignment](../alignment/) · [Choose a model](../training/)
