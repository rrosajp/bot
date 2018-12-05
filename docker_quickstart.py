import os
from time import sleep

from selenium.common.exceptions import WebDriverException

from include import Bot

# Write your automation here
# Stuck ? Look at the github page or the examples in the examples folder


# If you want to enter your Instagram Credentials directly just enter
# username=<your-username-here> and password=<your-password> into InstaPy
# e.g like so InstaPy(username="instagram", password="test1234")


def login():
    try:
        bot.login()
    except WebDriverException as wde:
        print("WebDriverException in login(): %s \n%s" % (wde, wde.stacktrace))
        sleep(10)
        login()


def run():
    global bot
    try:
        bot = Bot(multi_logs=True, selenium_local_session=False, proxy_address_port=os.environ.get("PROXY"))
        bot.set_selenium_remote_session(
            selenium_url="http://%s:%d/wd/hub" % (os.environ.get('SELENIUM', 'selenium'), 4444))
        login()
        bot.set_settings()
        bot.act()
    except WebDriverException as wde:
        print("WebDriverException in act(): %s \n%s" % (wde, wde.stacktrace))
        run()


run()

bot.end()
