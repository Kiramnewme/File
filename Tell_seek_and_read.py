# f=open("name.txt","r")
# print(f.tell())
# f.seek(2)
# print(f.tell())
# d=f.read()
# print(f.tell())
# print(d)


f=open("my_file.txt")
f.seek(2)
f1=f.read()
print(f1)
f2=f.tell()
print(f2)
f.close() 