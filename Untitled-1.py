import random

x = random.randint(1,100)
a = int(input("0~100猜一个数:"))

if a == x:
    print("猜对了")
else:
    print(f"猜错了\n结果是{x}")
