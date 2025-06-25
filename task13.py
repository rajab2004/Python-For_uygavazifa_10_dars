print("5 ta tilifon narhini kiriting: ")
narh = int(input("1-narhni kiriting: "))
eng_kichik = narh
eng_katta = narh
for i in range(4):  
    narh = int(input(f"{i+2}-narhni kiriting: "))
    if narh < eng_kichik:
        eng_kichik = narh
    if narh > eng_katta:
        eng_katta = narh

print("Eng arzon telefon:", eng_kichik)
print("Eng qimmat telefon:", eng_katta)
