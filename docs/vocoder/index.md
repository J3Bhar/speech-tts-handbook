---
title: HiFi-GAN vocoder
---

# HiFi-GAN: from mel features to speech

HiFi-GAN is a **neural vocoder**. It accepts acoustic features rather than phones or words.

## Learn in this order

1. Prepare licensed speech audio and train/validation manifests.
2. Select a versioned [official HiFi-GAN implementation](https://github.com/jik876/hifi-gan).
3. Choose a compatible mel representation: sample rate, FFT, hop, windows, filters, log base and normalization.
4. Test reference mel → waveform reconstruction before using predicted mels.
5. Train the generator and preserve checkpoints/configs privately.
6. Load the matching generator and use it to synthesize WAVs from compatible acoustic-model mels.

```bash
HIFIGAN_DIR="path/to/hifi-gan"           # Replace with the source checkout
DATA_DIR="path/to/dataset"              # Replace with your audio directory
CONFIG="path/to/vocoder_config.json"    # Replace with matching saved settings
WEIGHTS="path/to/vocoder_checkpoint"    # Replace with compatible generator weights
OUT="path/to/output_wavs"               # Replace with a writable WAV directory
```

**Common pitfall:** two 80-band mels can still be incompatible due to different features. Only if source is **log10** and destination **natural log**, the conversion is `np.log(10.0) * mel`; never apply this automatically to normalized mels.

A vocoder's input is not inherently phone-based or character-based; its compatibility depends on the acoustic features and speech distribution.

[Official HiFi-GAN](https://github.com/jik876/hifi-gan) · [Inference](../inference/)
