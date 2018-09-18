students = [
    {"name": "阿土"},
    {"name": "小美"}
]
find_name = "小美"

for stu_name in students:
    # 将字典student中的键值对存储到列表中方便遍历
    print(stu_name)
    if stu_name["name"] == find_name:
        # 对数组循环的终止条件进行设置
        print("找到了该同学 %s" % find_name)
        # 输出列表中符合条件的值
        break
        # 如果条件满足，那么后面else的语句就可以不用执行了
else:
    print("没有找到该同学 %s" % find_name)
    # 这个语句是为了防止出现上面条件都不满足的情况而设立的

print("循环结束")
