from __future__ import annotations

import asyncio

from . import ds

class Model(ds.Model):
  @classmethod
  async def get(cls, key: str) -> Model:
    print('Model async get()')
    return Model._get(lambda k: get(k), key)

async def get(key: str) -> typing.Any:
  print(f'async get() with key = {key}')
