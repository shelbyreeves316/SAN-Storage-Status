from fastapi import APIRouter
from typing import List
from ..models import SmartInfo
from ..smart import get_smart_status

router = APIRouter()


def _list_block_devices() -> List[str]:
    # simplistic device listing; for real system use lsblk or os
    return [f"/dev/{d}" for d in ("sda", "sdb", "sdc")]


@router.get("/", response_model=List[SmartInfo])
async def list_disks():
    devices = _list_block_devices()
    return [get_smart_status(dev) for dev in devices]


@router.get("/{name}", response_model=SmartInfo)
async def disk_detail(name: str):
    return get_smart_status(f"/dev/{name}")
