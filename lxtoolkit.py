#!/usr/bin/env python3
import qrcode
import os
from colorama import init, Fore
init()

class QRcodeMaker:
    def __init__(self):
        self.img = None
        self.filename = None
        self.qrcode_banner_path = ".qrcode_banner.txt"
    pass

    def GenerateQRC(self):
        os.system('clear')
        os.system("cat " + self.qrcode_banner_path)
        self.qrcode_link = input("qrcode link: ")
        print("[*] Link saved. ")
        try:
            qr = qrcode.QRCode(
                    version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=10,
                    border=4,
                )
            qr.add_data(self.qrcode_link)
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("qrcode.png")
            print(Fore.GREEN + "[*] QRcode downloaded and saved as: qrcode.png " + Fore.WHITE)
        except KeyboardInterrupt:
            print(Fore.RED + "[!] Interrupted by user. " + Fore.WHITE)
        except Exception as e:
            print(Fore.RED + "[!] Something went wrong: " + Fore.WHITE)
            print(e)
    pass

class Menu:
    def __init__(self):
        self.qr_coder = QRcodeMaker()
    pass

    def clear_screen(self):
        os.system('clear')
    pass

    def display_menu(self):
        self.clear_screen()
        print(Fore.GREEN)
        os.system('cat .toolkit_banner.txt')
        print(Fore.WHITE)
        print("1. QRcode Maker")
        print("2. Exit. ")
    pass

    def run(self):
        self.display_menu()
        try:
            choice = input("Select an option: ")
            if choice == "1":
                self.qr_coder.GenerateQRC()
            elif choice == "2":
                exit()
        except KeyboardInterrupt:
            print(Fore.RED + "[!] Interrupted by user. "+ Fore.WHITE)
        except Exception as e:
            print(Fore.RED + "[!] Something went wrong." + Fore.WHITE)
            print(e)
    pass


menu = Menu()
menu.run()
