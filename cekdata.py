import requests
import time
from datetime import datetime
from urllib.parse import quote
from colorama import init, Fore, Style

init(autoreset=True)

class GrokOSINT:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    def banner(self):
        print(Fore.CYAN + "="*75)
        print(Fore.YELLOW + "🔍 KenOSINT v3.0 - Advanced OSINT Tool (Paling Lengkap)")
        print(Fore.CYAN + "="*75)
        print(Fore.RED + "⚠️  Gunakan hanya untuk tujuan LEGAL dan Etis!")
        print(Fore.CYAN + "="*75)

    def cari_username(self, username):
        print(Fore.YELLOW + f"\n🔎 Mencari username: {username}")
        platforms = {
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://instagram.com/{username}",
            "TikTok": f"https://tiktok.com/@{username}",
            "GitHub": f"https://github.com/{username}",
            "YouTube": f"https://youtube.com/@{username}",
            "Facebook": f"https://facebook.com/{username}",
            "Reddit": f"https://reddit.com/user/{username}",
            "LinkedIn": f"https://linkedin.com/in/{username}",
            "Pinterest": f"https://pinterest.com/{username}",
            "Tumblr": f"https://{username}.tumblr.com",
        }
        
        for site, url in platforms.items():
            try:
                r = requests.get(url, headers=self.headers, timeout=6)
                if r.status_code == 200:
                    print(Fore.GREEN + f"✅ [{site}] Ditemukan → {url}")
                else:
                    print(Fore.RED + f"❌ [{site}] Tidak ditemukan")
            except:
                print(Fore.RED + f"❌ [{site}] Error")
            time.sleep(1.2)

    def cari_nama(self, nama, lokasi=""):
        print(Fore.YELLOW + f"\n🧠 Mencari nama: {nama}")
        if lokasi:
            print(f"Lokasi: {lokasi}")
        
        dorks = [
            f'"{nama}"',
            f'"{nama}" "{lokasi}"',
            f'"{nama}" email OR gmail OR whatsapp OR "no hp"',
            f'"{nama}" site:linkedin.com',
            f'"{nama}" site:facebook.com',
            f'"{nama}" filetype:pdf',
        ]
        
        print(Fore.BLUE + "\nLink Google Dorks:")
        for dork in dorks:
            link = f"https://google.com/search?q={quote(dork)}"
            print(Fore.BLUE + f"→ {link}")

    def cari_nomor(self, nomor):
        print(Fore.YELLOW + f"\n📱 Mencari nomor: {nomor}")
        print(Fore.BLUE + f"Google Search: https://google.com/search?q=%22{nomor}%22")
        print(Fore.BLUE + f"Truecaller: https://truecaller.com/search/{nomor}")
        print(Fore.BLUE + "Facebook Search: https://facebook.com/search/top?q=" + nomor)

    def cari_email(self, email):
        print(Fore.YELLOW + f"\n✉️  Mencari email: {email}")
        print(Fore.BLUE + f"Google: https://google.com/search?q=%22{email}%22")
        print("Cek di HaveIBeenPwned.com untuk melihat apakah email pernah bocor.")

    def menu(self):
        self.banner()
        while True:
            print(Fore.CYAN + "\n" + "-"*60)
            print("1.  Cari Username (Multi Platform)")
            print("2.  Cari Nama Lengkap + Lokasi")
            print("3.  Cari Nomor Telepon")
            print("4.  Cari Email")
            print("5.  Keluar")
            print("-"*60)
            
            pilihan = input(Fore.WHITE + "\nPilih nomor (1-5): ").strip()
            
            if pilihan == "1":
                username = input("Masukkan username: ").strip()
                self.cari_username(username)
            elif pilihan == "2":
                nama = input("Masukkan nama lengkap: ").strip()
                lokasi = input("Lokasi (kota/provinsi, tekan enter jika kosong): ").strip()
                self.cari_nama(nama, lokasi)
            elif pilihan == "3":
                nomor = input("Masukkan nomor telepon (+62...): ").strip()
                self.cari_nomor(nomor)
            elif pilihan == "4":
                email = input("Masukkan email: ").strip()
                self.cari_email(email)
            elif pilihan == "5":
                print(Fore.GREEN + "\nTerima kasih telah menggunakan GrokOSINT v3.0!")
                break
            else:
                print(Fore.RED + "Pilihan tidak valid!")

if __name__ == "__main__":
    tool = GrokOSINT()
    tool.menu()
