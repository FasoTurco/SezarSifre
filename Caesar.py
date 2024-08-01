import time
import os

def caesar_encrypt(text, shift):
    """
    Caesar şifrelemesi ile metni şifreler.

    :param text: Şifrelenecek metin
    :param shift: Kaydırma sayısı
    :return: Şifrelenmiş metin
    """
    result = ""

    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char

    return result

def caesar_decrypt(text, shift):
    """
    Caesar şifrelemesi ile metni çözer.

    :param text: Şifrelenmiş metin
    :param shift: Kaydırma sayısı
    :return: Çözülmüş metin
    """
    return caesar_encrypt(text, -shift)

def brute_force_decrypt(text):
    """
    Brute force ile şifrelenmiş metni çözer.

    :param text: Şifrelenmiş metin
    :return: Çözülmüş metin
    """
    for shift in range(26):
        decrypted_text = caesar_decrypt(text, shift)
        print(f"Kaydırma sayısı: {shift}, Çözülmüş metin: {decrypted_text}")
        time.sleep(1)  # 1 saniye beklet

def about():
    """
    Hakkında bilgi gösterir.
    """
    print("Caesar Şifrelemesi Uygulaması")
    print("-------------------------------")
    print("Yapımcı: FasoTurco")
    print("Versiyon: 1.0")
    print("Telegram: https://t.me/HilalYazilim")
    print("")

def main():
    print("Caesar Şifrelemesi Uygulaması")
    print("-------------------------------")

    while True:
        print("1. Metni Şifrele")
        print("2. Metni Çöz")
        print("3. Brute Force ile Çöz")
        print("4. Hakkında")
        print("5. Çıkış")

        choice = input("Seçenek girin: ")

        if choice == "1":
            text = input("Şifrelenecek metni girin: ")
            shift = int(input("Kaydırma sayısını girin: "))

            encrypted_text = caesar_encrypt(text, shift)
            print(f"Şifrelenmiş metin: {encrypted_text}")

        elif choice == "2":
            text = input("Şifrelenmiş metni girin: ")
            shift = int(input("Kaydırma sayısını girin: "))

            decrypted_text = caesar_decrypt(text, shift)
            print(f"Çözülmüş metin: {decrypted_text}")

        elif choice == "3":
            text = input("Şifrelenmiş metni girin: ")

            print("Brute force ile çözme işlemi başlatılıyor...")
            brute_force_decrypt(text)

        elif choice == "4":
            about()

        elif choice == "5":
            print("Çıkış yapıldı.")
            break

        else:
            print("Geçersiz seçenek. Lütfen tekrar deneyin.")

        time.sleep(5)  # 5 saniye beklet
        os.system('cls' if os.name == 'nt' else 'clear')  # terminali temizle

if __name__ == "__main__":
    main()
