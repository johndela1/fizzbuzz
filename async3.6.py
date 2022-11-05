#!/usr/bin/env python3.6

import asyncio

async def f():
    return 1
def g():
    pass
print(asyncio.get_event_loop().run_until_complete(f()))
