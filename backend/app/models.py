from typing import List, Optional
from pydantic import BaseModel


class SmartInfo(BaseModel):
    status: str
    alert: Optional[str] = None
    temperature: Optional[float] = None


class Device(BaseModel):
    devid: str
    size: str
    used: str
    path: str
    smart: SmartInfo


class Volume(BaseModel):
    label: str
    uuid: str
    usage: Optional[str] = None
    drives: List[Device]
