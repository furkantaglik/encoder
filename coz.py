import os

def decrypt(key):
     
    srcPath = r'çözülecek klasörün yolu \  kullanın örnek C\user\örnek'

    #uzantılar
    ext_list = ['.txt','png','jpg','jfif']
   
    for root, dirs, files in os.walk(srcPath):
        for file in files:
            if file.endswith(tuple(ext_list)):
              
                file_path = os.path.join(root, file)
  
                with open(file_path, 'rb') as f:
                    data = f.read()
                decrypted_data = xor(data, key)
               
                with open(file_path, 'wb') as f:
                    f.write(decrypted_data)


def xor(data, key):
    xored = b''
    for i in range(len(data)):
        xored += bytes([data[i] ^ ord(key[i % len(key)])])
    return xored

if __name__ == '__main__':
    key = input("Lütfen şifre çözme anahtarını girin: ")
    decrypt(key)
    print("Dosyalarınız çözüldü.")
