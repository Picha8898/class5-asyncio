#1-1 simple-sync.py
import time

def sleep():
    print(f'Time:{time.time() - start:.2f}')
    time.sleep(1)

#ช่วยให้คอมพิวเตอร์คำนวน
def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')
        sleep()
        total += number
    #
    print(f'Task {name}: Sum = {total}\n')

start = time.time()
#การtaskว่าtaskกี่ครั่ง
tasks = [
    sum("A", [1, 2]),
    sum("B", [1, 2, 3]),
]
end = time.time()
print(f'Time: {end-start:.2f} sec')



