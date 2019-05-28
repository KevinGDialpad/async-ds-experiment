import asyncio

from lib import ads

async def main():
  model = await ads.Model.get(key='my_key')
  print(f'Got a model with key={model.key}')

if __name__ == '__main__':
  asyncio.run(main())
