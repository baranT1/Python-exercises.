
ürün1 = float(input("1. Ürün fiyatı: "))

ürün2 = float(input("2. Ürün fiyatı: "))

ürüntoplam = (ürün1 + ürün2)

if ürüntoplam <= 5000 :
    
    print(f"Toplam tutar: {ürüntoplam:.2f} TL")

else :
    if ürün1 <= ürün2 :
        indirimlitutar1 = (ürün2 * 0.9) + ürün1
        print(f"Toplam tutar: {indirimlitutar1:.2f} TL")
    
    else: 
        
        indirimlitutar2 = (ürün1 * 0.9) + ürün2
        print(f"Toplam tutar: {indirimlitutar2:.2f} TL")
    