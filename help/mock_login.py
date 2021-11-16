import time
from selenium import webdriver
import requests


def open_web(url: str, driver_path: str):
    browser_ins = webdriver.Chrome(executable_path=driver_path)
    browser_ins.get(url)
    browser_ins.maximize_window()
    time.sleep(5)
    browser_ins.quit()


def login():
    # TODO
    start = requests.session()
    login = start.post('https://gray.930pm.cn/home.php/Login/userLogin', data={}, headers={}, cookies='')
    pass


def main():
    chrome_dirver = 'F:\software\chromedriver.exe'
    url = 'https://gray.930pm.cn/home.php/Login/index'
    open_web(url, chrome_dirver)


if __name__ == '__main__':
    main()
