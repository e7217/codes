# -*- coding: utf-8 -*-
import os, time
import conf_c

def _setElement():
    fc_path = 'env/connect_env.txt'

    conn = conf_c.conf_connDB(fc_path).connect()

    cursor = conn.cursor()
    device_ip = conf_c.getdeviceip()
    print "Device ip is "+device_ip
    cursor.execute("SELECT checkAddress FROM dbo.setinfo01t WHERE ip_address = %s", device_ip)
    row = cursor.fetchone()
    conn.close()
    print row
    cnt = 0
    while row == None:
        print "There is no {} of ".format('checkAddress')+device_ip
        time.sleep(10)

        conn = conf_c.conf_connDB(fc_path).connect()
        cursor = conn.cursor()
        cursor.execute("SELECT checkAddress FROM dbo.setinfo01t WHERE ip_address = %s", device_ip)
        row = cursor.fetchone()
        conn.close()
    elm = conf_c.conf_fromDB(fc_path).getconfDB('checkAddress', cursor, row)

    return str(elm)

def ping_reboot(hostname):

    def ping_ok(hostname):
        print hostname, 'is up!'
        if os.path.isfile(dirpath + 'net_ok.txt'):
            filesize1 = os.path.getsize("./network/net_ok.txt")
            if filesize1 > 1048576:
                os.remove('./network/net_ok.txt')
        with open('./network/net_ok.txt', 'a') as f:
            f.write(time.ctime() + ' -------- ok!\n')
        time.sleep(60)
        if check > 10:
            return 0
        return check

    def ping_down(hostname):
        print hostname, 'is down!'
        if os.path.isfile(dirpath + 'net_down.txt'):
            filesize1 = os.path.getsize(dirpath + "net_down.txt")
            if filesize1 > 1048576:
                os.remove(dirpath + 'net_down.txt')
        with open('./network/net_down.txt', 'a') as f:
            f.write(time.ctime() + ' -------- Down!\n')
        time.sleep(3)
        if check > 10:
            # os.system("sudo ifconfig wlan0 down")
            # os.system("sudo ifconfig wlan0 up")
            os.system("sudo reboot")
#             print "reboot!!"
        return check + 1

    global check
    # with open('./ping_address.txt', 'r') as fi:
    #     hostname = fi.readline()
    print 'Ping address ---------------------------- : ' + str(hostname)

    # response = os.system("ping -c 1 " + hostname) # linux
    response = os.system("ping -n 1 " + hostname) # windowns
    print '--------------------- checking network ---------------------> ', check
    # and then check the response...
    dirpath = './network/'
    if not (os.path.isdir(dirpath)):
        os.makedirs(os.path.join(dirpath))
    if response == 0:
        return ping_ok(hostname)
    else:
        return ping_down(hostname)

if __name__ == "__main__":

    hostname = _setElement()
    check = 0
    while 1:
        check = ping_reboot(hostname)
