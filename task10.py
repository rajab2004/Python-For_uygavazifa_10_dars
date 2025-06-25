print("7 ta son kiriting: ")
son = int(input("1-sonni kiriting: "))
eng_katta = son

for i in range(6):  
    son = int(input(f"{i+2}-sonni kiriting: "))
    if son > eng_katta:
        eng_katta = son
print("Eng katta son:", eng_katta)