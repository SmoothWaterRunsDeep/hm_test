"""
双层嵌套
row = 1
先有行再有列
while row < = 9:
    col = 1
    while col <= row
        print(str(row) × str(col)=row*col)

        col +=1

    print row
    row += 1
"""
row = 1
while row <= 9:
    col = 2
    while col <= row:
        print("%d*%d =%d\t" %(col,row,row*col)  ,end="")
        col +=1
    print("")
    row += 1