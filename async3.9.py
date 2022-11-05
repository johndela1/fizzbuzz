#!/usr/bin/env python3.9

import asyncio

async def f():
    return 1

print(asyncio.get_event_loop().run_until_complete(f()))
print(asyncio.run(f()))
