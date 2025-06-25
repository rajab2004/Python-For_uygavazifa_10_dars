son = int(input("1-sonni kiriting: "))
eng_kichik = son
eng_katta = son
for i in range(4):  
    son = int(input(f"{i+2}-sonni kiriting: "))
    if son < eng_kichik:
        eng_kichik = son
    if son > eng_katta:
        eng_katta = son
ortacha = (eng_kichik + eng_katta) / 2

print("Eng kichik son:", eng_kichik)
print("Eng katta son:", eng_katta)
print("Ularning o‘rtachasi:", ortacha)
