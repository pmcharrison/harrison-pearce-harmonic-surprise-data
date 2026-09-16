#!/usr/bin/env python3
"""Validate the canonical WAV inventory and write a deterministic release ZIP."""

from __future__ import annotations

import argparse
import csv
import hashlib
import zipfile
from pathlib import Path

FIXED_TIMESTAMP = (2017, 8, 27, 0, 0, 0)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("wav_directory", type=Path)
    parser.add_argument("output_zip", type=Path)
    args = parser.parse_args()

    inventory_path = Path(__file__).resolve().parents[1] / "audio_sources.csv"
    with inventory_path.open(newline="", encoding="utf-8") as handle:
        inventory = list(csv.DictReader(handle))
    if len(inventory) != 300:
        raise ValueError(f"expected 300 inventory rows, got {len(inventory)}")

    expected_names = {row["filename"] for row in inventory}
    actual_names = {path.name for path in args.wav_directory.glob("*.wav")}
    if actual_names != expected_names:
        raise ValueError(
            "WAV inventory mismatch: "
            f"missing={sorted(expected_names - actual_names)[:5]}, "
            f"extra={sorted(actual_names - expected_names)[:5]}"
        )

    args.output_zip.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        args.output_zip,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for row in sorted(inventory, key=lambda item: int(item["stimulus_id"])):
            path = args.wav_directory / row["filename"]
            if path.stat().st_size != int(row["bytes"]):
                raise ValueError(f"byte-size mismatch: {path}")
            if sha256(path) != row["sha256"]:
                raise ValueError(f"SHA-256 mismatch: {path}")
            info = zipfile.ZipInfo(row["filename"], date_time=FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes(), compresslevel=9)

    print(f"{sha256(args.output_zip)}  {args.output_zip}")


if __name__ == "__main__":
    main()
