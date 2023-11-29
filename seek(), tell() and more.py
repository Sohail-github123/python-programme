f = open ("python .txt")

#print(f.tell())   # it shows where is pointer
print(f.readline())
#print(f.tell())
f.seek(11)         # it will move pointer to particular place
print(f.readline())
#print(f.tell())
f.close()
