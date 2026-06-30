import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
from urllib.parse import quote, urlparse
from colorama import init, Fore, Style

init(autoreset=True)

class GrokOSINT:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

    def banner(self):
        print(Fore.CYAN + "="*80)
        print(Fore.YELLOW + "🔍 GrokOSINT v4.0 - ULTIMATE OSINT TOOL")
        print(Fore.CYAN + "="*80)
        print(Fore.RED + "⚠️ HANYA UNTUK PENGGUNAAN LEGAL & ETIS ⚠️")
        print(Fore.CYAN + "="*80)

    # ==================== FITUR UTAMA ====================
    def cari_username(self, username):
        print(Fore.YELLOW + f"\n🔎 Mencari Username: {username}")
        platforms = {
            "Twitter": f"https://twitter.com/{username}",
            "Instagram": f"https://instagram.com/{username}",
            "TikTok": f"https://tiktok.com/@{username}",
            "GitHub": f"https://github.com/{username}",
            "YouTube": f"https://youtube.com/@{username}",
            "Facebook": f"https://facebook.com/{username}",
            "Reddit": f"https://reddit.com/user/{username}",
            "LinkedIn": f"https://linkedin.com/in/{username}",
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
            time.sleep(1)

    def cari_nama(self, nama, lokasi=""):
        print(Fore.YELLOW + f"\n🧠 Mencari Nama: {nama}")
        if lokasi:
            print(f"Lokasi: {lokasi}")
        dorks = [f'"{nama}"', f'"{nama}" "{lokasi}"', f'"{nama}" whatsapp OR email OR hp']
        print(Fore.BLUE + "\nGoogle Dorks:")
        for d in dorks:
            print(f"https://google.com/search?q={quote(d)}")

    def cari_nomor(self, nomor):
        print(Fore.YELLOW + f"\n📱 Mencari Nomor: {nomor}")
        print(Fore.BLUE + f"→ Google: https://google.com/search?q=%22{nomor}%22")
        print(Fore.BLUE + f"→ Truecaller: https://truecaller.com/search/{nomor}")

    def cari_email(self, email):
        print(Fore.YELLOW + f"\n✉️ Mencari Email: {email}")
        print(Fore.BLUE + f"→ Google: https://google.com/search?q=%22{email}%22")

    def analyze_link(self, link):
        print(Fore.YELLOW + f"\n🔗 Menganalisis Link: {link}")
        try:
            r = requests.get(link, headers=self.headers, timeout=10)
            soup = BeautifulSoup(r.text, 'html.parser')
            title = soup.title.string.strip() if soup.title else "Tidak ada judul"
            print(Fore.GREEN + f"Judul Halaman: {title}")
            print(Fore.GREEN + "Link bisa diakses!")
        except:
            print(Fore.RED + "Gagal mengakses link.")

    # ==================== MENU ====================
    def menu(self):
        self.banner()
        while True:
            print(Fore.CYAN + "\n" + "="*50)
            print("1. Cari berdasarkan Username")
            print("2. Cari berdasarkan Nama Lengkap")
            print("3. Cari berdasarkan Nomor Telepon")
            print("4. Cari berdasarkan Email")
            print("5. Analyze Link Akun (Instagram/Twitter/dll)")
            print("6. Keluar")
            print("="*50)
            
            pilihan = input(Fore.WHITE + "\nPilih nomor (1-6): ").strip()

            if pilihan == "1":
                username = input("Masukkan Username: ").strip()
                self.cari_username(username)
            elif pilihan == "2":
                nama = input("Masukkan Nama Lengkap: ").strip()
                lokasi = input("Lokasi (kosongkan jika tidak ada): ").strip()
                self.cari_nama(nama, lokasi)
            elif pilihan == "3":
                nomor = input("Masukkan Nomor Telepon (+62...): ").strip()
                self.cari_nomor(nomor)
            elif pilihan == "4":
                email = input("Masukkan Email: ").strip()
                self.cari_email(email)
            elif pilihan == "5":
                link = input("Masukkan Link Akun: ").strip()
                self.analyze_link(link)
            elif pilihan == "6":
                print(Fore.GREEN + "\nTerima kasih telah menggunakan GrokOSINT v4.0!")
                break
            else:
                print(Fore.RED + "Pilihan tidak valid!")

if __name__ == "__main__":
    tool = GrokOSINT()
    tool.menu()
