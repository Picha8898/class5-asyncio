import asyncio
import time

async def sleep():
    print(f'Time:{time.time() - start:.2f}')
    time.sleep(1)
#ช่วยให้คอมพิวเตอร์คำนวน
async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        await sleep()
        total += number
    print(f'Task {name}: Sum = {total}\n')
# ทำเหมือนเดิม แต่ใช้ gather
async def main():
    await asyncio.gather(sum("A", [1, 2]), sum("B", [1, 2, 3]))

if __name__ =='__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')