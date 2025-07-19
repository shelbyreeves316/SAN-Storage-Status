import json
from typing import List
from .utils import run_cmd
from .models import Volume, Device, SmartInfo
from .smart import get_smart_status


def list_volumes() -> List[Volume]:
    output = run_cmd(["btrfs", "filesystem", "show", "--raw", "--json"])
    if not output:
        return []
    try:
        data = json.loads(output)
    except json.JSONDecodeError:
        return []

    volumes: List[Volume] = []
    for fs in data.get("filesystems", []):
        label = fs.get("label", "")
        uuid = fs.get("uuid", "")
        devices = []
        for dev in fs.get("devices", []):
            smart = get_smart_status(dev.get("path", ""))
            device = Device(
                devid=str(dev.get("devid", "")),
                size=dev.get("size", ""),
                used=dev.get("used", ""),
                path=dev.get("path", ""),
                smart=smart,
            )
            devices.append(device)
        volumes.append(Volume(label=label, uuid=uuid, drives=devices))
    return volumes
