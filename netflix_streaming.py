import argparse
import Constant as c 
from selenium import webdriver
import time
import os
import subprocess
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
# from fake_useragent import UserAgent

# driver = None 

def wait_for_elem_by_xpath(xp, driver):
    elem = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xp)))
    return elem

def login_once(driver):
    cmd = './remove_cache.sh'
    process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')
    print("login")
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
        # username = wait_for_elem_by_xpath('//*[@id="id_userLoginId"]', driver)
        # username.send_keys('')
        # driver.get_screenshot_as_file('username.png')
        # pwd = wait_for_elem_by_xpath('//*[@id="id_password"]', driver)
        # time.sleep(30)
        # pwd.send_keys('')
        # driver.get_screenshot_as_file('pwd.png')
        # time.sleep(30)
        # btn = wait_for_elem_by_xpath('//button[@type="submit"]', driver)
        # btn.click()
        # driver.get_screenshot_as_file('btn.png')
        # driver.find_element_by_name('userLoginId').send_keys('')
        # time.sleep(5)
        # driver.find_element_by_name('password').send_keys('')
        # time.sleep(5)
        # driver.get_screenshot_as_file('setpw.png')
        # # driver.find_element_by_xpath("//button[@type='submit']").send_keys(Keys.ENTER)
        # driver.find_element_by_xpath("//button[@type='submit']").click()
        # driver.get_screenshot_as_file('click.png')
        # time.sleep(5)
        # driver.get_screenshot_as_file('login.png')
        # run_netflix(driver)
    return driver

def run_netflix(driver):
    print("run netflix")
    #Remove cache except for login info
    # cmd = './remove_cache.sh'
    # process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')
    driver.get(c.NETFLIX_BBB)
    print(driver.current_url)
    time.sleep(5)
    driver.get_screenshot_as_file('startplay.png')
    driver.find_element_by_css_selector(".NFPlayer.nf-player-container").click()
    
    time.sleep(60)

    driver.get_screenshot_as_file('playing.png')
    driver.close()
    driver.quit()

    # cmd = './remove_cache.sh'
    # process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')


#Check whether the user has logged in everytime before an experiment. DEPRECATED 
def login_old(driver):
    
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

    driver.get(c.NETFLIX_BBB)
    print(driver.current_url)
    time.sleep(5)
    # driver.find_element_by_xpath("//*[@id='netflix-player']/a").click()
    # driver.find_element_by_xpath('//*[@id="appMountPoint"]').click()
    # button-nfplayerPlay
    driver.find_element_by_css_selector(".NFPlayer.nf-player-container").click()
    # driver.find_element_by_xpath("//*[@id='netflix-player']/a").click()
    
    time.sleep(240)
    driver.get_screenshot_as_file('playing.png')
    driver.close()
    driver.quit()

    # os.chdir('/tmp/ruk/user-prof')
    # process = subprocess.call(['cd /tmp/ruk/user-prof && rm !(*Default*)'], shell=True, executable="/bin/bash")
    cmd = './remove_cache.sh'
    process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')

def start_streamer():
    print("")

def get_driver(args):
    # chromeOptions = webdriver.ChromeOptions()
    # # chromeOptions.debugger_address = "127.0.0.1:9222"
    # print(args["ssl"])
    # chromeOptions.add_argument('disable-quic')
    # chromeOptions.add_argument('ssl-key-log='+args["ssl"])
    # chromeOptions.add_argument('user-data-dir='+c.USER_PROFILE) #cache enabled
    # chromeOptions.add_argument('window-size=1920x1080')
    # # chromeOptions.add_experimental_option("excludeSwitches", ["enable-automation"])
    # # chromeOptions.add_experimental_option('useAutomationExtension', False)
    # # chromeOptions.add_argument('disable-blink-features=AutomationControlled')
    # # chromeOptions.add_argument("--disable-blink-features")
    # chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
    
    # driver = webdriver.Chrome(executable_path=c.DRIVER, chrome_options=chromeOptions)
    # # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    # # print(driver.execute_script("return navigator.userAgent;"))

    # ua = UserAgent()
    # userAgent = ua.random
    # print(userAgent)

    # options = webdriver.ChromeOptions() 
    # # options.add_argument("start-maximized")
    # # options.add_argument("--disable-blink-features=AutomationControlled")
    # # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # # options.add_argument('disable-blink-features=AutomationControlled')
    # # options.add_argument("disable-infobars")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
    # # options.add_argument('user-agent='+userAgent)
    # options.add_experimental_option('useAutomationExtension', False)
    # driver = webdriver.Chrome(options=options, executable_path=r'/opt/thirdparty_video/chromedriver')
    # print(driver.execute_script("return navigator.webdriver;"))
    # Setting user agent as Chrome/83.0.4103.97
    # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'})
    # print(navigator.driver)
    # driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    # driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
    # print(driver.execute_script("return navigator.userAgent;"))
    # driver.get('https://www.httpbin.org/headers')

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('disable-quic')
    # chromeOptions.add_argument('ssl-key-log='+args["ssl"])
    chromeOptions.add_argument('user-data-dir='+c.USER_PROFILE) #cache enabled
    chromeOptions.add_argument('window-size=1920x1080')
    driver = webdriver.Chrome(executable_path=c.DRIVER, chrome_options=chromeOptions)
    return driver

# def get_driver(args):
#     chromeOptions = webdriver.FirefoxOptions()
#     print(args["ssl"])
#     chromeOptions.add_argument('disable-quic')
#     chromeOptions.add_argument('ssl-key-log='+args["ssl"])
#     chromeOptions.add_argument('user-data-dir='+c.USER_PROFILE) #cache enabled
#     chromeOptions.add_argument('window-size=1920x1080')
#     driver = webdriver.Firefox(firefox_options = chromeOptions, executable_path=r'/opt/thirdparty_video/geckodriver')
#     return driver


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
    # return args

# def main(args):
#     print(args)
#     # driver = webdriver.Chrome(c.DRIVER)
#     chromeOptions = webdriver.ChromeOptions()
#     # options.binary_location = 'google-chrome'
#     # options.add_argument('headless')

#     # if userDir:
#     #   if userDir == 'tmp':
#     #     userDir = '/tmp/tmpUserDir'
#     #   args += ['--user-data-dir={}'.format(userDir)]
#     # else:
#     #   chromeOptions.add_experimental_option('excludeSwitches', ['user-data'])

#     # if dataDir:
#     #   if dataDir == 'tmp':
#     #     dataDir = '/tmp/tmpDataDir'
#     #   args += ['--data-path={}'.format(dataDir)]
#     # else:
#     #   chromeOptions.add_experimental_option('excludeSwitches', ['data-path'])

#     # cmd = '#!/bin/bash && shopt -s extglob && cd /tmp/ruk/user-prof && rm !(*Default*)'

#     print(args["ssl"])
#     chromeOptions.add_argument('disable-quic')
#     chromeOptions.add_argument('ssl-key-log='+args["ssl"])
#     chromeOptions.add_argument('user-data-dir='+c.USER_PROFILE) #cache enabled
#     chromeOptions.add_argument('window-size=1920x1080')
#     driver = webdriver.Chrome(executable_path=c.DRIVER, chrome_options=chromeOptions)
#     login(driver)

if __name__ == '__main__':
    parse_args()
    # main(args)