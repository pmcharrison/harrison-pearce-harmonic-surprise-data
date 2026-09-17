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

`source_pieces.csv` links every stimulus to its originating song. It records
the artist and title, zero-based IDyOM composition index, one-based hcorp
`popular_1` sequence number and record id, and original McGill Billboard song
id. It also records the one-based source-chord span from the excerpt's first
chord through its rated target chord; the two post-target chords remain in the
eight-chord stimulus. The mapping is metadata only: the v1.0.0 audio release
is unchanged.

## Provenance

- Musical material: chord sequences sampled from the CC0
  [McGill Billboard Project](https://ddmal.ca/research/The_McGill_Billboard_Project_%28Chord_Analysis_Dataset%29/)
  corpus.
- Piece identities: the pinned
  [hcorp `popular_1` source](https://github.com/pmcharrison/hcorp/blob/fa78ba60888123f3a6c1ae80f4b95f444da78972/data-raw/json/popular_1.json)
  was aligned as an exact ordered subsequence of the original numeric McGill
  Billboard song directories.
- Study synthesis: TiMidity++ 2.14.0, acoustic-grand-piano timbre, 60 bpm.
- SoundFont: public domain, confirmed by the dataset author on 2026-09-16;
  the exact SoundFont identity is no longer recoverable.
- Original archive: the study author's Google Drive folder, with file content
  fixed here by SHA-256 rather than by claiming reproducible resynthesis.

Only stimuli and their technical inventory are included. Participant-level
data and personal information are not part of this repository.

The published aggregate source table contains inconsistent artist/title
separator whitespace and accidental outer quote characters in two display
strings. `source_pieces.csv` gives canonical structured artist/title metadata,
including corrected values for stimuli 630 and 814, without changing the
source data or audio.

## Citation

Harrison, P. M. C., & Pearce, M. T. (2018). Dissociating sensory and cognitive
theories of harmony perception through computational modeling. *Proceedings
of ICMPC15/ESCOM10*. https://doi.org/10.31234/osf.io/wgjyv

## License

The dataset and stimuli are dedicated to the public domain under CC0 1.0.
See `LICENSE`.
