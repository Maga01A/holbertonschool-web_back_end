#!/usr/bin/env python3
"""
Async comprehension example
"""

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Collects 10 random numbers using an async comprehension
    and returns them as a list.
    """
    return [i async for i in async_generator()]
