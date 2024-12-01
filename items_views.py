from typing import Annotated
from fastapi import APIRouter, Path


router = APIRouter(prefix='/items', tags=['Items'])


@router.get('/')
def list_items():
    return [
        'item1',
        'item2',
        'item3',
        'item4',
        'item5',
        'item6'
    ]


@router.get('/latest/')
def get_latest_item():
    return {
        'item': {
            'id': 0,
            'name': 'latest'
        }
    }


@router.get('/{item_id}/')
def get_item_by_id(item_id: Annotated[int, Path(ge=0, lt=1000)]):
    return {
        'item': {
            'id': item_id
        }
    }
