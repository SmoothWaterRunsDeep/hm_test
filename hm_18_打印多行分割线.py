def lines(char,length):
    """
    分割线函数
    :param char:用什么符号作为分割线
    :param length: 分割线的长度
    """
    row = 0
    while row <= 5:
        print(char*length)
        row += 1


lines('^',100)
