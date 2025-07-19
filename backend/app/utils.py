import subprocess
from typing import List


def run_cmd(cmd: List[str]) -> str:
    """Run a command and return its output as text."""
    try:
        return subprocess.check_output(cmd, text=True)
    except FileNotFoundError:
        return ""
    except subprocess.CalledProcessError as exc:
        return exc.output
