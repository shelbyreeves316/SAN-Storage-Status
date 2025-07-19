import json
from .utils import run_cmd
from .models import SmartInfo


def get_smart_status(device: str) -> SmartInfo:
    if not device:
        return SmartInfo(status="unknown")
    output = run_cmd(["smartctl", "-H", "-A", "-j", device])
    if not output:
        return SmartInfo(status="unknown")
    try:
        data = json.loads(output)
    except json.JSONDecodeError:
        return SmartInfo(status="unknown")

    health = data.get("smart_status", {}).get("passed")
    status = "PASSED" if health else "FAILED"
    temp = None
    for attr in data.get("ata_smart_attributes", {}).get("table", []):
        if attr.get("name") == "Temperature_Celsius":
            try:
                temp = float(attr.get("value"))
            except (TypeError, ValueError):
                pass
    alert = None if health else "SMART FAIL"
    return SmartInfo(status=status, alert=alert, temperature=temp)
