from __future__ import annotations

import asyncio

from . import ds

class Model(ds.Model):
  @classmethod
  async def get(cls, key: str) -> Model:
    print('Model async get()')

    def callback(k):
      get_task = asyncio.create_task(get(k))
      return asyncio.wait({get_task})

    done, unfinished = await Model._get(callback, key)

    # Missing some error handling here - what if not finished, etc.
    return done.pop().result()


async def get(key: str) -> typing.Any:
  print(f'async get() with key = {key}')
  return Model(key=key)
