from __future__ import annotations

import asyncio

from . import ds

class Model(ds.Model):
  @classmethod
  async def get(cls, key: str) -> Model:
    print('Model async get()')

    loop = asyncio.get_running_loop()

    def callback(k):
      get_task = loop.create_task(get(k))
      loop.call_soon(get_task)

      # Need to make sure the task runs here

      return get_task.result()

    return Model._get(callback, key)


async def get(key: str) -> typing.Any:
  print(f'async get() with key = {key}')
  return Model(key=key)
