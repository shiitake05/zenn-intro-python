import time

def task1():
    print("Task 1 started")
    time.sleep(2)  # 2秒間処理をブロック
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(2)  # 2秒間処理をブロック
    print("Task 2 completed")

def main():
    task1()
    task2()

main()