len = input("有多少个问题？：")
filename = input("生成的文件名？：")

len = int(len) + 1

que = "question:"

for i in range(0,len):
    que += "\n  - id: " + str(i) + "\n    str: \n    rev: \n"

filename += ".yml"

with open(filename,'w') as f:
    f.write(que)

print("完成了！")