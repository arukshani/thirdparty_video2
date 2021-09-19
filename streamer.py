import argparse
import Constant as c 
from selenium import webdriver
import time
import os
import subprocess

def run_netflix(driver):
    print("run netflix")
    #Remove cache except for login info
    cmd = './remove_cache.sh'
    process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')
    driver.get(c.NETFLIX_BBB)
    print(driver.current_url)
    time.sleep(5)
    driver.find_element_by_css_selector(".NFPlayer.nf-player-container").click()
    driver.get_screenshot_as_file('startplay.png')
    time.sleep(60)

    driver.get_screenshot_as_file('playing.png')
    driver.close()
    driver.quit()

    cmd = './remove_cache.sh'
    process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')

def login_once(driver):
    cmd = './remove_cache.sh'
    process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')
    print("login")
    loginURL = c.NETFLIX_LOGIN
    driver.get(c.NETFLIX_LOGIN)
    if driver.current_url == loginURL.replace('Login', 'browse'):
        print('Was already logged in!')
        driver.get_screenshot_as_file('already_logged_in.png')
    else:
        driver.find_element_by_name('userLoginId').send_keys('')
        time.sleep(0.5)
        driver.find_element_by_name('password').send_keys('')
        time.sleep(0.5)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(0.5)
        driver.get_screenshot_as_file('login.png')

def get_driver(args):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('disable-quic')
    chromeOptions.add_argument('ssl-key-log='+args["ssl"])
    chromeOptions.add_argument('user-data-dir='+c.USER_PROFILE) #cache enabled
    chromeOptions.add_argument('window-size=1920x1080')
    # chromeOptions.add_argument('load-extension=/opt/video_collection/extension')
    driver = webdriver.Chrome(executable_path=c.DRIVER, chrome_options=chromeOptions)
    return driver

def parse_args():
    """Parse commandline arguments"""
    parser = argparse.ArgumentParser(description='Streaming Netflix')
    parser.add_argument('-f', '--folder', type=str, required=False, default="", help="Folder where data is stored")
    parser.add_argument('-o', '--open', type=int, required=False, default=0, help="Open setup page")
    parser.add_argument('-s', '--ssl', type=str, required=False, default="", help="Open setup page")
    args = vars(parser.parse_args())
    

    if args["open"] > 0:
        print("open")
        driver = get_driver(args)
        login_once(driver)
    else:
        print("start streaming...")
        driver = get_driver(args)
        run_netflix(driver)

if __name__ == '__main__':
    parse_args()