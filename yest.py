s
sss
s
s
ss
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from pandas import read_csv
from time import sleep


def getCredentials():
    cred = []
    with open('insta-bot/username.txt', 'r') as text_file:
        userName = text_file.readline()
        cred.append(userName)
    with open('insta-bot/password.txt', 'r') as text_file:
        password = text_file.readline()
        cred.append(password)
    return cred


def logIn():
    cred = getCredentials()
    driver.find_element_by_xpath(xpaths['xUser']).send_keys(cred[0])
    driver.find_element_by_xpath(xpaths['xPassword']).send_keys(cred[1])
    driver.find_element_by_xpath(xpaths['xLogIn']).click()
    sleep(3)


def follow(userNames):
    for user in userNames:
        driver.get('https://instagram.com/'+user)
        try:
            driver.find_element_by_xpath(xpaths['xFollow']).click()
        except NoSuchElem


# Xpaths to locate elements
xpaths = {
    "xUser": "//input[@name='username']",
    "xPassword": "//input[@name='password']",
    "xLogIn": "//button[@type='submit']",
    "xFollow": "//button[contains(.,'Follow')]",
    "xFollowing": '//span[@aria-label="Following"]',
    "xUnfollow": "//button[contains(.,'Unfollow')]",
}

if __name__ == "__main__":
    res = input('''Follow/Unfollo
