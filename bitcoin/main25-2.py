import pyupbit
import sqlite3

ticker = 'KRW-BTC'
interval = 'minute1'
to = '2021-12-02 11:20'
count = 200
price_now = pyupbit.get_ohlcv(ticker=ticker, interval=interval, to=to, count=count)

db_path = r"bitcoin\coin.db"

con = sqlite3.connect(db_path, isolation_level=None)
price_now.to_sql('BTC', con, if_exists='append')

con.close