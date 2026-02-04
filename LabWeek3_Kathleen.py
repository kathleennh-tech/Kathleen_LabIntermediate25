def kolom_jawaban(kata_rahasia, tebakan_huruf):
  tampilan_huruf = ""
  for huruf in kata_rahasia:
    if huruf.lower() in tebakan_huruf:
      tampilan_huruf += huruf + " "
    else:
      tampilan_huruf += "_ "
  return tampilan_huruf.strip()

def hangman_game(kata_rahasia):
  kata_rahasia = kata_rahasia.lower()
  tebakan_huruf = []
  kesempatan = 4

  print("SELAMAT DATANG DI PERMAINAN HANGMAN!")

  while kesempatan > 0:
    tampilan = kolom_jawaban(kata_rahasia, tebakan_huruf)
    print(f"Kata: {tampilan}")
    print(f"Sisa kesempatan: {kesempatan}")

    tebakan = input("Tebak satu huruf: ").lower()
    
    if len(tebakan) != 1:
      print("Tolong masukan satu huruf saja!")
      continue
    
    if tebakan in tebakan_huruf:
      print(f"Kamu sudah menebak huruf '{tebakan}'!")
      continue
    
    tebakan_huruf.append(tebakan)

    if tebakan in kata_rahasia:
      print(f"Selamat! '{tebakan}' ada di dalam kata rahasia!")
    else: 
      kesempatan -= 1
      print(f"Maaf, '{tebakan}' tidak ada di dalam kata rahasia")
     
    tampilan = kolom_jawaban(kata_rahasia, tebakan_huruf)

    if "_" not in tampilan:
      print("Selamat kamu menang!")
      print(f"Kata rahasianya adalah {kata_rahasia}")
      break
  
  else:
    print("Kamu kalah!")
    print(f"Kata rahasiannya adalah {kata_rahasia}")

hangman_game("makan")