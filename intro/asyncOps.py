# syncOps.pyを非同期処理に変更したもの

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # 非同期で2秒間待機
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)  # 非同期で2秒間待機
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())  # task1とtask2を同時に実行

asyncio.run(main())