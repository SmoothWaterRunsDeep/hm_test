import random

player = int(input("请输入您要出的拳 石头 (1) 剪刀 (2) 布(3)"))
computer = random.randint(1,3)

print("玩家选择出的手势是： %d  电脑选择出的手势是：%d" % (player , computer ))

# 这个if条件是指游戏规则，石头胜剪刀，剪刀胜布，布胜石头
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("电脑弱爆了")
elif (player == computer):
    print("真是心有灵犀，再来一局")
else:
    print("别走我们决战到天明")


