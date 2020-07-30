#basit bir sözlük
kelimeler = {

    "get":["almak","edinmek","olmak"],
    "break":["mola","ara","kırılma"],
    "winner":["kazanan","galip","birinci"]
}

def kelimeEkle(kelime,kelimeler):
    if kontrol(kelime,kelimeler):
        mevcut_anlamlar = set(kelimeler[kelime])
        yeni_giriş = input("kelime zaten mevcut.girdiğiniz kelimenin kayıtlı anlamları: {}\n yeni bir anlam girmek istermisiniz ? (E\H)".format(mevcut_anlamlar))
        if yeni_giriş.lower()=="e":
            yeni_anlamlar=input("girmek istediğiniz anlamları aralarına virgül koyarak yazın: ")
            yeni_anlamlar_bölünmüş = set(yeni_anlamlar.split(","))
            kelimeler[kelime]=list(mevcut_anlamlar|yeni_anlamlar_bölünmüş)
            print("girdiniz anlamlar kaydedildi. anlamlar listesinin son hali: ",kelimeler[kelime])
        elif yeni_giriş.lower()=="h":
            pass
    else:
        yeni_anlamlar=input("girmek istediğiniz anlamları aralarına virgül koyarak yazın: ")
        yeni_anlamlar_bölünmüş = set(yeni_anlamlar.split(","))
        kelimeler[kelime]=list(yeni_anlamlar_bölünmüş)
        print("girdiniz anlamlar kaydedildi. anlamlar listesinin son hali: ",kelimeler[kelime])







def kelimeÇevir(kelime,kelimeler):
    if kontrol(kelime,kelimeler):
        print("{} kelimesinin anlamları".format(kelime),end=":")
        print(*kelimeler[kelime])
    else:
        print("girdiniz kelime mevcut değildir. ")

def kontrol(kelime,kelimeler):
    if kelime in kelimeler:
        return True
    else:
        return False


def kelimeleriListele():
    for no,kelime in enumerate(kelimeler,1):
        print("{}.{}".format(no,kelime))


seçenekler="""
        [1] kelime ekle
        [2] kelime çevir
        [3] kelimeleri listele

        """
while True:

    print(seçenekler)
    seçenek=int(input("seçiminizi yapın: "))

    if seçenek == 1:
        kelime=input("eklenecek ingilizce kelimeyi girin: ")
        kelimeEkle(kelime,kelimeler)
    elif seçenek == 2:
        kelime=input("anlamını öğrenmek istediğiniz kelimeyi girin: ")
        kelimeÇevir(kelime,kelimeler)
    elif seçenek == 3:
        kelimeleriListele()