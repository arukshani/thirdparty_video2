import argparse
import Constant as c 
from selenium import webdriver
import time
import os
import subprocess

def login(driver):
    
    #Remove cache except for login info
    cmd = './remove_cache.sh'
    process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')

    loginURL = c.NETFLIX_LOGIN
    driver.get(c.NETFLIX_LOGIN)
    if driver.current_url == loginURL.replace('Login', 'browse'):
        print('Was already logged in!')
        # driver.get_screenshot_as_file('logged_in.png')
    else:
        driver.find_element_by_name('userLoginId').send_keys('')
        time.sleep(0.5)
        driver.find_element_by_name('password').send_keys('')
        time.sleep(0.5)
        driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(0.5)
        driver.get_screenshot_as_file('login.png')

    driver.get(c.NETFLIX_VIDEO1)
    print(driver.current_url)
    time.sleep(0.5)
    # driver.find_element_by_xpath("//*[@id='netflix-player']/a").click()
    # driver.find_element_by_xpath('//button[@class="button continue-playing"]')
    # button-nfplayerPlay
    # driver.find_element_by_css_selector(".PlayerControlsNeo__bottom-controls .nfp-button-control").click()
    time.sleep(60)
    driver.get_screenshot_as_file('playing.png')
    driver.close()
    driver.quit()

    # os.chdir('/tmp/ruk/user-prof')
    # process = subprocess.call(['cd /tmp/ruk/user-prof && rm !(*Default*)'], shell=True, executable="/bin/bash")
    cmd = './remove_cache.sh'
    process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')

def start_streamer():
    print("")

def parse_args():
    """Parse commandline arguments"""
    parser = argparse.ArgumentParser(description='Streaming Netflix')
    parser.add_argument('-f', '--folder', type=str, required=False, default="", help="Folder where data is stored")
    parser.add_argument('-o', '--open', type=int, required=False, default=0, help="Open setup page")
    parser.add_argument('-s', '--ssl', type=str, required=False, default="", help="Open setup page")
    args = vars(parser.parse_args())
    
    if args["open"] > 0:
        print("open")
        # login()
    else:
        print("folder")
        # start_streamer()
    return args

def main(args):
    print(args)
    # driver = webdriver.Chrome(c.DRIVER)
    chromeOptions = webdriver.ChromeOptions()
    # options.binary_location = 'google-chrome'
    # options.add_argument('headless')

    # if userDir:
    #   if userDir == 'tmp':
    #     userDir = '/tmp/tmpUserDir'
    #   args += ['--user-data-dir={}'.format(userDir)]
    # else:
    #   chromeOptions.add_experimental_option('excludeSwitches', ['user-data'])

    # if dataDir:
    #   if dataDir == 'tmp':
    #     dataDir = '/tmp/tmpDataDir'
    #   args += ['--data-path={}'.format(dataDir)]
    # else:
    #   chromeOptions.add_experimental_option('excludeSwitches', ['data-path'])

    # cmd = '#!/bin/bash && shopt -s extglob && cd /tmp/ruk/user-prof && rm !(*Default*)'

    # print(args["ssl"])
    chromeOptions.add_argument('disable-quic')
    # chromeOptions.add_argument('ssl-key-log='+args["ssl"])
    chromeOptions.add_argument('user-data-dir='+c.USER_PROFILE) #cache enabled
    chromeOptions.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(executable_path=c.DRIVER, chrome_options=chromeOptions)
    login(driver)

if __name__ == '__main__':
    args = parse_args()
    main(args)