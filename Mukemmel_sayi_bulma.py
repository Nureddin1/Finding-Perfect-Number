print(""""
********************
Mukemmel Sayi Bulma

Cikmak icin q'e basiniz
********************
""")
while True:
    sayi =(input("Sayi: "))
    sayinin_bolenleri = []
    bolenleri_cemi = 0
    if sayi == "q":
        print("Programdan Cikiliyor...")
        break
    sayi = int(sayi)
    for i in range(1, sayi):
        if sayi % i == 0:
            sayinin_bolenleri.append(i)
    for i in sayinin_bolenleri:
        bolenleri_cemi += i
    if bolenleri_cemi == sayi:
        print("Bu Sayi MUKEMMEL Sayidir")
    else:
        print("Bu Sayi Mukemmel Sayi degildir..")