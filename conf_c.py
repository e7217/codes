import pymssql
import time
import socket

class conf_connDB:
    #set configuration to connect to DB from dic
    def __init__(self, filename):
        dict = {'port': ''}
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                comp = line.split('=')
                for i in range(len(comp)):
                    comp[i] = comp[i].strip()
                if (comp[0] == "server") and (comp[1].find(":") > 0):
                    dict[comp[0]], dict['port'] = (comp[1].split(':'))[0], (comp[1].split(':'))[1]
                else:
                    dict[comp[0]] = comp[1]

        envList = dict

        self.server = envList['server'] + ':' + envList['port']
        self.user = envList['user']
        self.password = envList['password']
        self.database = envList['database']

    def connect(self):
        conn = pymssql.connect(self.server, self.user, self.password, self.database, timeout=3)
        return conn

class conf_fromDB:
    #read configuration data from DB
    def __init__(self, fc_path):
        self.fc_path = fc_path
        self.conn = conf_connDB(self.fc_path)
        self.zone_id = []
        self.sequence_t = ""
        self.hopper_id = ""
        self.tmp_id_num = ""
        self.send_cycle = ""
        self.response_count = ""
        self.mchcd = ""
        self.device = ""

    def getconfDB(self, colname, cursor, row):
        for i in range(len(cursor.description)):
            if colname == cursor.description[i][0]:
                print colname, '=', row[i]
                return row[i]

    def setallconfDB(self):
        print "[Set config data from DB]"
        conn = conf_connDB(self.fc_path).connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM dbo.setinfo01t WHERE ip_address = %s", getdeviceip())
        row = cursor.fetchone()

        self.sequence_t = self.getconfDB('sequence_cycle', cursor, row)
        self.hopper_id = self.getconfDB('zone_hopper_id', cursor, row)
        self.tmp_id_num = self.getconfDB('tmp_id_num', cursor, row)
        self.send_cycle = self.getconfDB('send_cycle', cursor, row)
        self.response_count = self.getconfDB('response_count', cursor, row)
        self.mchcd = self.getconfDB('machinename', cursor, row)
        self.device = self.getconfDB('machinetype', cursor, row)

        self.zone_id = []
        for i in range(0, self.tmp_id_num):
            self.zone_id.append(int(self.getconfDB('zone_{}_id'.format(str(i + 1)), cursor, row)))
        self.zone_id.append(int(self.getconfDB('zone_cnt_id', cursor, row)))

        conn.close()
        time.sleep(0.01)

        print

        return self

def getdeviceip():
    #get device ip address by socket return
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    time.sleep(0.01)
    return ip
