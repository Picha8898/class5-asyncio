# 2-3
import asyncio
import time

#การรัน hello 1-10 พร้อมกัน 
async def hello(i):
    print(f"{time.ctime()} helllo {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} helllo {i} dene")

async def main():
    coros = [hello(i) for i in range(10)]
    await asyncio.gather(*coros)
 
if __name__ =='__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')