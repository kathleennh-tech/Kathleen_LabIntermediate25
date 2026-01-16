kata_rahasia = "makan"
tebakan = ["_"] * len(kata_rahasia)
kesempatan = 6
huruf_terpakai = []

while kesempatan > 0:
    print(f"Tebakan kata: {' '.join(tebakan)}")
    print(f"Sisa Kesempetan menebak: {kesempatan}")
    print(f"HUruf yang sudah dicoba: {huruf_terpakai}")

    tebakan_huruf = input("Tebak satu huruf: ").lower()

    if tebakan_huruf in huruf_terpakai:
        print("Tebak huruf lain!")
    else:
        huruf_terpakai.append(tebakan_huruf)
        kesempatan -= 1 

        if tebakan_huruf in kata_rahasia:
            print("Tebakan kamu benar!")
            for i in range(len(kata_rahasia)):
                if kata_rahasia[i] == tebakan_huruf:
                    tebakan[i] = tebakan_huruf
        else:
            print("Tebakan kamu salah!")
    if "_" not in tebakan:
        print(f"Selamat! kamu berhasil menebak kata: {kata_rahasia}")
        break
if "_" in tebakan:
    print(f"Game berakhir! Kesempatan telah habis \nKatanya adalah: {kata_rahasia}")