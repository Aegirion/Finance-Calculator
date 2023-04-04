def giris(grd):
    kasa.append(grd)
    print("Tutar eklendi/Money added:")
    print()

def cikis(grd):
    kasa.remove(grd)
    print("Tutar eksildi/amount is deducted:")

def bky():
    print("Kasa bakiyesi/Cash balance: ", sum(kasa))

print("Hoşgeldiniz / Welcome")
print()
print("1-Türkçe \n2-English")
print()
dil = int(input("Lütfen Dil Seçiniz / Please select language: "))

kasa = []
if dil == 1:
    while True:
        print("1-Para Ekleme \n2-Para Çekme \n3-Toplam Para \n4-Sistemden Çıkış")
        print()
        secim = int(input("Hangi işlemi yapmak istersiniz?: "))
        if secim == 1:
            grd = int(input("Eklemek istediğiniz tutarı yazınız: "))
            giris(grd)
        elif secim == 2:
            grd = int(input("Çekmek istediğiniz tutarı yazınız: "))
            if grd <= sum(kasa):
                cikis(grd)
            else:
                print("Bakiye yetersiz")
        elif secim == 3:
            bky()
        elif secim == 4:
            break
        else:
            print("Geçersiz seçim lütfen geçerli bir komut giriniz.")
elif dil == 2:
    while True:
        print("1-Adding Money \n2-Withdrawing Money \n3-Total Money \n4-Exit System")
        print()
        secim = int(input("What action would you like to take?: "))
        if secim == 1:
            grd = int(input("Enter the amount you want to add: "))
            giris(grd)
        elif secim == 2:
            grd = int(input("Enter the amount you want to withdraw: "))
            if grd <= sum(kasa):
                cikis(grd)
            else:
                print("Insufficient balance")
        elif secim == 3:
            bky()
        elif secim == 4:
            break
        else:
            print("Invalid selection please enter a valid command.")
else:
    print("Invalid selection please select 1 or 2.")
