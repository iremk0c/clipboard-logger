import pyperclip
import time

def main():
    print("Clipboard Logger başlatıldı.")
    print("Çıkmak için ctrl + c yapabilirsin.\n")

    son_kopyalanan = ""

    while True:
        try:
            kopya = pyperclip.paste()

            if kopya != son_kopyalanan:
                zaman_damgasi = time.strftime("%Y-%m-%d %H:%M:%S")
                with open("clipboard_kayitlari.txt", "a", encoding="utf-8") as dosya:
                    dosya.write(f"[{zaman_damgasi}]\n{kopya}\n\n")

                print(f"[{zaman_damgasi}] Yeni kopyalama kaydedildi.")
                son_kopyalanan = kopya

            time.sleep(0.5) 

        except KeyboardInterrupt:
            print("\nProgram sonlandırıldı.")
            break

if __name__ == "__main__":
    main()
