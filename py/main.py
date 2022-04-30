from ChromeLogger import ChromeLogger
from Database import Database
from Scrapper import Scrapper
CONNECTION_STRING = 'add your Mongodb connector'
path = r'add your chromedriver.exe path'
username = 'your instagram username'
password = 'your instagram password'
if __name__ == "__main__":
    db = Database(CONNECTION_STRING)
    driver = ChromeLogger(path,username,password).connect()
    data = Scrapper(driver).scrap()
    print(data)
    db.add(data)
