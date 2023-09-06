n = int(input())
y = n**3 / 9
print("y = ", y)
if (y%1!=0):
    y = int(y) + 1
print(y, type(y))

print(f"Ты {'очень ' * int(y)}крут")