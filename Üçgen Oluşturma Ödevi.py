

x = float(input("1. Açı Değerini Giriniz: "))

y = float(input("2. Açı Değerini Giriniz: "))

z = float(input("3. Açı Değerini Giriniz: "))

icacıtoplam = x + y + z


if icacıtoplam == 180 and x > 0 and y > 0 and z > 0 :
    
    print(f"Kenarları {x},{y},{z} olan bir üçgen oluşturulabilir.")
    
else :
    
    print("!!Böyle bir üçgen oluşturulamaz.")

     