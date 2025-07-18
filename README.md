# SAN Storage Status

This project provides a simple web interface for monitoring BTRFS volumes and SMART data on an Arch Linux system.

## Requirements
- Python 3.9+
- `btrfs-progs` and `smartmontools` installed on the host

Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Running

Start the server with:

```bash
python app.py
```

Then open <http://localhost:8000> in your browser.

The interface displays detected BTRFS volumes, device usage, and SMART status for each drive.
