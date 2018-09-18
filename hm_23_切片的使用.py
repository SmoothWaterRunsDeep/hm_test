info_str = [0,1,2,3,4,5,6,7,8,9,10]
print(info_str[0:11:2])
print("——"*100)
print(info_str[0: :2])
print("——"*100)
print(info_str[::2])
print("——"*100)
print(info_str[:11:2])
# 步长就是取值的间隔数
print("++"*100)
print(info_str[-1:-12:-1])
print(info_str[-1::-1])
print(info_str[::-1])
# 由于步长是负数所以列表是倒序排列，因此开始索引和结束索引的输入顺序也需要颠倒
print(info_str[11:0:-1])