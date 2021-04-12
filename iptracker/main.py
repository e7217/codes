import ping3, arrow, pymssql, datetime, time, os
import logging
from logging.handlers import RotatingFileHandler

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlalchemy.sql.default_comparator

from models import Xnlog11t

target_list = {
    "gw": "172.16.0.254",
    "10101": "172.16.0.150",
    "10102": "172.16.0.152",
    "10103": "172.16.0.153",
    "10104": "172.16.0.154",
    "10105": "172.16.0.155",
    "10106": "172.16.0.157",
    "10107": "172.16.0.158",
}

conn_env = (
    "mssql+pymssql://frienderp:ctf$0501#@14.35.235.221:1566/q3i_polytec?charset=utf8"
)

log = None

def _get_logger():
    # FORMAT = ('%(asctime)-15s %(threadName)-15s %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s')
    FORMAT = "%(asctime)-15s %(levelname)-8s %(module)-15s:%(lineno)-8s %(message)s"
    # logging.basicConfig(format=FORMAT)
    global log
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)
    fileMaxByte = 1024 * 1024 * 10
    fh = RotatingFileHandler("iplogs.log", maxBytes=fileMaxByte, backupCount=2)
    fh.setFormatter(logging.Formatter(FORMAT))
    fh.setLevel(logging.DEBUG)
    log.addHandler(fh)


def orm_agent():
    engine = create_engine(conn_env)
    SessionLocal = sessionmaker()
    # session = SessionLocal(bind=engine)
    with SessionLocal(bind=engine) as session:
        for target in target_list:
            # response = ping3.verbose_ping(target_list[target])
            response = os.system(f'ping -n 1 {target_list[target]}')
            session.add(
                Xnlog11t(
                    mchcd=target,
                    ipaddr=target_list[target],
                    status='0' if response == 1 else '1',
                    # created=arrow.utcnow().to("Asia/Seoul").format('YYYY-MM-DD HH:mm:ss'),
                    created=datetime.datetime.now(),
                )
            )
        session.commit()


def _init():
    ping3.DEBUG = True
    _get_logger()


def main():
    orm_agent()


if __name__ == "__main__":
    try:
        while True:
            _init()
            main()
            time.sleep(60)
    except Exception as e:
        log.debug(e)
        print(e)
        time.sleep(5)
