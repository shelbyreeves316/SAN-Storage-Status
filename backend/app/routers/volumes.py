from fastapi import APIRouter
from typing import List
from ..btrfs import list_volumes
from ..models import Volume

router = APIRouter()


@router.get("/", response_model=List[Volume])
async def get_volumes():
    return list_volumes()
