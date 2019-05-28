import asyncio

from lib import ads

async def main():
  await ads.Model.get(key='my_key')

if __name__ == '__main__':
  asyncio.run(main())
