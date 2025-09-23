#!/usr/bin/env python3
import qrcode
import os
import pyshorteners
from colorama import init, Fore
init()

# Author: luxe0x64
# date of an update: 09/23/2025
# Version 1.1
# update description: URLshortener added.



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


class URLshortener:
    def __init__(self):
        self.user = None
    pass

    def Shortener(self):
        os.system('clear && cat .url_shortener_banner.txt')
        try:
            self.user = input(str("URL: "))
            print("[*] URL: " + self.user)
        except KeyboardInterrupt:
            print(Fore.RED + "[!] Interrupted by user. " + Fore.WHITE)
        except Exception as e:
            print(Fore.RED + "[!] Something went wrong. " + Fore.WHITE + e)
        try:
            print("[*] Shorting the URL... ")
            self.s = pyshorteners.Shortener()
            print(self.s.tinyurl.short(str(self.user)))
            print(Fore.GREEN + "[*] Done. " + Fore.WHITE)
        except KeyboardInterrupt:
            print(Fore.RED + "[!] Interrupted by user. " + Fore.WHITE)
        except Exception as e:
            print(Fore.RED + "[!] Something went wrong: " + Fore.WHITE + e)
    pass

class Menu:
    def __init__(self):
        self.qr_coder = QRcodeMaker()
        self.short = URLshortener()
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
        print("2. URL Shortener")
        print("3 Exit.")
    pass

    def run(self):
        self.display_menu()
        try:
            choice = input("Select an option: ")
            if choice == "1":
                self.qr_coder.GenerateQRC()
            elif choice == "2":
                self.short.Shortener()
            elif choice == "3":
                exit()
        except KeyboardInterrupt:
            print(Fore.RED + "[!] Interrupted by user. "+ Fore.WHITE)
        except Exception as e:
            print(Fore.RED + "[!] Something went wrong." + Fore.WHITE)
            print(e)
    pass


menu = Menu()
menu.run()
