#请编写move(n, a, b, c)函数，它接收参数n，表示3个柱子A、B、C中第1个柱子A的盘子数量，
#然后打印出把所有盘子从A借助B移动到C的方法[汉诺塔移动]

def move(n, a, b, c):
    if n==1:
        print(a, " -->> ", c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

print("请输入盘子个数：")
num = input()
num = int(num)
move(num, 'A', 'B', 'C')