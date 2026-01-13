kata = "rumah"
tebak = input("Tebak satu huruf: ")

if len(tebak) == 1:
    if tebak.lower() in kata.lower():
        print("Benar, huruf ada di kata rahasia")
    else: 
        print("Salah, huruf tidak ada di kata rahasia")
else:
    print("Tidak valid! Input satu huruf kecil")