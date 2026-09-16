# Harrison–Pearce harmonic-surprise stimuli

This repository publishes the 300 WAV stimuli used for the popular-music
harmonic-expectation experiment reported by Harrison and Pearce (2018). Each
stimulus is an eight-chord piano sequence at 60 beats per minute; participants
rated the surprisingness of chord six.

The WAV files are distributed as the release asset
`harrison-pearce-harmonic-surprise-audio-v1.0.0.zip`. `audio_sources.csv`
records the filename, byte size, audio format, and SHA-256 digest of every
file. Run `python scripts/package_release.py WAV_DIRECTORY OUTPUT_ZIP` to
validate source WAVs against that inventory and recreate the deterministic
release archive.

## Provenance

- Musical material: chord sequences sampled from the CC0 McGill Billboard
  Project corpus.
- Study synthesis: TiMidity++ 2.14.0, acoustic-grand-piano timbre, 60 bpm.
- SoundFont: public domain, confirmed by the dataset author on 2026-09-16;
  the exact SoundFont identity is no longer recoverable.
- Original archive: the study author's Google Drive folder, with file content
  fixed here by SHA-256 rather than by claiming reproducible resynthesis.

Only stimuli and their technical inventory are included. Participant-level
data and personal information are not part of this repository.

## Citation

Harrison, P. M. C., & Pearce, M. T. (2018). Dissociating sensory and cognitive
theories of harmony perception through computational modeling. *Proceedings
of ICMPC15/ESCOM10*. https://doi.org/10.31234/osf.io/wgjyv

## License

The dataset and stimuli are dedicated to the public domain under CC0 1.0.
See `LICENSE`.
