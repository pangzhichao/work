print("你好，世界")
print("我是一个学生")
# 这是我得到第一个的练习题
a=1+23;
if(a>0):
    print("大于0")
else:print("小于0")
for i in range(1,10):
    for j in range(1,10):
     print("%d*%d=%2d" % (i,j,i*j),end=" ");
     print("")

print("---------------------------")
 #左上三角格式输出九九乘法表
for i in range(1,10):
 for j in range(i,10):
         print("%d*%d=%2d" % (i,j,i*j),end=" ")
         print("")