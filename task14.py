yosh = 0
print("5 kishining yoshini kiriting:")
for i in range(5):
    yosh += int(input(f"{i+1}-yoshni kiriting: "))
    if yosh < 0:
        print("Yosh manfiy bo'lmasligi kerak!")
        yosh = 0
        break
if yosh > 0:
    yosh = yosh / 5
    print("o'rtacha yosh:", yosh)