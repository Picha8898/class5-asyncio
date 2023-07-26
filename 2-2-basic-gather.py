# 2-2
import asyncio
import time

#การรัน hello 1และ2 พร้อมกัน 
async def hello(i):
    print(f"{time.ctime()} helllo {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} helllo {i} dene")

async def main():
    task1 = asyncio.create_task(hello(1))
    #await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1, task2)

if __name__ =='__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')