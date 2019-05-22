from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import time
import random
from telegram import Bot
def urlserch(url):
    try:
        agnetsList = ["User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"]
        agnetStr = random.choice(agnetsList)
        req = urllib.request.Request(url)
        req.add_header("User-Agent", agnetStr)
        responses = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(responses, features='lxml')
        title = soup.title
        print(time.time())
    except Exception as e:
        cw = str(e)
        bot = Bot(token="814416255:AAHWXrUJsGkiRPDUQjYkadKqyu2C64dUMs0")
        bot.send_message("674721504", url + cw)
if __name__ == "__main__":
    while True:
        time.sleep(60*10)
        file = open(r"D:\web\url.txt")
        with file as f:
            for line in f.readlines():
                urlserch(line)
