import argparse
import Constant as c 
from selenium import webdriver
import time
import os
import subprocess
# from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import hashlib
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
import json 
# import Command
# from expscontrol.cmd_exec import RemoteNode,RemoteCommand,Command
# import Command
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import zipfile

# Default port used by the extension to 
server_port = 19282
runs = []
user = 'test_user'
ts = str(int(time.time()))
runs.append({'expname': user+'_'+'1'+'_netflix.run'+ts, 'url': c.NETFLIX_4K, 'netem': None, 'length': 4 * 60})

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            print(file)
            ziph.write(os.path.join(root, file))

def run_netflix(driver, cc_expname, netflix_folder):
    print("run netflix")
    driver.get(c.NETFLIX_4K)
    print(driver.current_url)
    time.sleep(5)
    # try:
    #   myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.VideoContainer')))
    #   print("Page is ready!")
    # except TimeoutException:
    #   print("Loading took too much time!")
    # driver.switch_to.default_content()
    # driver.find_element_by_css_selector(".NFPlayer.nf-player-container").click()
    # driver.find_element_by_css_selector(".AkiraPlayer").click()
    # driver.find_element_by_xpath("//*[@id='netflix-player']/a").click()
    # time.sleep(5)
    start_filename = netflix_folder + cc_expname + "-startplay.png"
    driver.get_screenshot_as_file(start_filename)
    # action = ActionChains(driver)
    # action.key_down(Keys.SHIFT)
    # action.send_keys(Keys.ALT)
    # action.key_up(Keys.SHIFT)
    # action.perform()

    # Chrome was only taking this at time of writing question.
    # ActionChains(driver).send_keys(Keys.SHIFT +Keys.ALT +Keys.CONTROL +"d").perform()
    # win = driver.find_element_by_css_selector(".NFPlayer.nf-player-container")
    # win.send_keys(Keys.SHIFT +Keys.ALT +Keys.CONTROL +"d")
    # driver.get_screenshot_as_file('playing.png')
    time.sleep(240)
    end_filename = netflix_folder + cc_expname + "-playing.png"
    driver.get_screenshot_as_file(end_filename)
    # driver.get("chrome://extensions/?id=gomdmfbijbkpbnakokccljfhjanjdpo")
    # time.sleep(0.5)
    # driver.get_screenshot_as_file('extension1.png')

    for entry in driver.get_log('browser'):
      print(entry)
    # for entry in driver.get_log('performance'):
    #   # print(entry)
    #   log = json.loads(entry["message"])["message"]
    #   if (
    #       # "Network.response" in log["method"]
    #       "Network.request" in log["method"]
    #       # or "Network.webSocket" in log["method"]
    #   ):
    #     print(log)
      # exit 

    # driver.get_screenshot_as_file('playing.png')
    driver.get('http://google.com')
    # Make sure the extension uploads the file
    time.sleep(3) #make sure files are uploaded
    driver.quit()
    # driver.close()
    # driver.quit()

    # cmd = './remove_cache.sh'
    # process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')

def login_once(driver):
    # cmd = './remove_cache.sh'
    # process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')
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
    for entry in driver.get_log('browser'):
      print(entry)


def get_driver(args):
    

    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument('disable-quic')
    chromeOptions.add_argument('ssl-key-log='+args["ssl"])
    chromeOptions.add_argument('user-data-dir='+c.USER_PROFILE) #cache enabled
    chromeOptions.add_argument('window-size=3840x2160')
    # chromeOptions.add_argument("--window-size=3840,2160")
    chromeOptions.add_argument('force-dev-mode-highlighting')
    # chromeOptions.add_argument('load-extension=/opt/video_collection/extension,/opt/netflix-1080p-1.19')
    chromeOptions.add_argument('load-extension=/opt/video_collection/extension')
    # chromeOptions.add_extension('/opt/netflix-1080p-v1.19.crx')
    
    chromeOptions.add_argument('autoplay-policy=no-user-gesture-required')
    # chromeOptions.add_argument('load-extension=/opt/chrome-csp-disable-master')
    # chromeOptions.add_extension("/opt/chrome-csp-disable-master.crx")
    # chromeOptions.add_argument('disable-extensions-file-access-check')
    # chromeOptions.add_argument('disable-extensions')
    # chromeOptions.add_argument('force-empty-corb-allowlist')
    # chromeOptions.add_argument('enable-features=OutOfBlinkCors,CorbAllowlistAlsoAppliesToOorCors')
    # chromeOptions.add_argument('disable-popup-blocking')
    # chromeOptions.add_argument("disable-xss-auditor")
    # chromeOptions.add_argument("disable-web-security")
    # chromeOptions.add_argument("allow-running-insecure-content")
    # chromeOptions.add_argument("allow-file-access-from-files")
    # chromeOptions.add_argument("disable-gpu")
    # chromeOptions.add_argument("disable-site-isolation-trials")
    chromeOptions.add_argument("enable-video-player-chromecast-support")
    chromeOptions.add_argument('load-media-router-component-extension')
    excludeList = [
      'disable-default-apps',
    ]
    chromeOptions.add_experimental_option('excludeSwitches', excludeList)
    
    d = DesiredCapabilities.CHROME
    # d['goog:loggingPrefs'] = { 'performance':'ALL' }
    d['loggingPrefs'] = { 'browser':'ALL' }
   
    # chromeOptions.add_argument('allow-ra-in-dev-mode')
    # chromeOptions.add_argument('--enable-logging --v=1')
    # chromeOptions.add_argument('disable-web-security')
    chromeOptions.add_argument('enable-logging')
    driver = webdriver.Chrome(executable_path=c.DRIVER, chrome_options=chromeOptions, desired_capabilities=d)
    driver.get("chrome://extensions")
    # time.sleep(1)
    # driver.find_element_by_xpath('//span[2]').click()
    # driver.find_element_by_css_selector(".cr-toggle").click()
    time.sleep(0.5)
    driver.get_screenshot_as_file('extension.png')
    return driver

class S(BaseHTTPRequestHandler):

  def do_GET(self):
    if self.path == '/close':
      self.send_response(200)
      self.send_header('Content-type', 'text/html')
      self.end_headers()
    else:
      print("Received unkown get request", self.path)
      self.send_response(404)

  def do_POST(self):
    if self.path.endswith('.json') or self.path.endswith('.pcap'):
      fname = self.path.split('/')[-1]
      length = self.headers['content-length']
      data = self.rfile.read(int(length))

      with open(self.server.folder+fname, 'w') as fh:
        fh.write(data.decode())

      self.send_response(200)
    else:
      self.send_response(400)

class POSTHTTPServer(HTTPServer):
  """
  Extend a normal python HTTP server. This will let us to manage various stuffs
  """
  def __init__(self, folder, *args):
    HTTPServer.__init__(self, *args)
    self.folder = folder
    self.stopped = False

  def serve_forever_with_stop(self):
    while not self.stopped:
      self.handle_request()

  def force_stop(self):
    self.stopped = True
    self.create_dummy_request()
    self.server_close()

  def create_dummy_request(self):
    print("Creating dummy request:","http://127.0.0.1:"+str(server_port)+"/close")
    # wget = Command()
    # wget.setCmd("wget http://127.0.0.1:"+str(server_port)+"/close")
    # wget.runSync()
    cmd = "curl http://127.0.0.1:"+str(server_port)+"/close"
    subprocess.check_output(cmd, shell=True)

  def update_folder(self, folder):
    self.folder = folder

def start_server_only(folder, driver, cc_expname):
  server_address = ('', server_port)
  # S = None 
  httpd = POSTHTTPServer(folder, server_address, S)
  server_thread = threading.Thread(target=httpd.serve_forever_with_stop)
  server_thread.start()
#   httpd.serve_forever_with_stop()

  for run in runs:
    print('Run experiment', run['expname'])
    m = hashlib.md5()
    # hashlib.sha256("a".encode('utf-8')).hexdigest()
    # m = hashlib.sha256(run['expname'].encode('utf-8'))
    m.update(run['expname'].encode('utf-8'))
    n = m.hexdigest()
    # n = run['expname']
    if not os.path.exists(folder+"/"+n):
      os.makedirs(folder+"/"+n)
      text_file = open(folder+"/"+n+'/'+"exp.txt", "w")
      text_file.write(run['expname'])
      text_file.close()
    netflix_folder = folder+"/"+n+'/'
    httpd.update_folder(netflix_folder)
    # collect_video(folder+"/"+n+'/', run['url'], length=run['length'], netem=run['netem'])
    run_netflix(driver, cc_expname, netflix_folder)

  httpd.force_stop()

def parse_args():
    """Parse commandline arguments"""
    parser = argparse.ArgumentParser(description='Streaming Netflix')
    parser.add_argument('-f', '--folder', type=str, required=False, default="", help="Folder where data is stored")
    parser.add_argument('-o', '--open', type=int, required=False, default=0, help="Open setup page")
    parser.add_argument('-s', '--ssl', type=str, required=False, default="", help="Log ssl session key")
    parser.add_argument('-l', '--server', type=str, required=False, default="", help="Start upload server")
    parser.add_argument('-n', '--name', type=str, required=False, default="", help="Experiment name")
    args = vars(parser.parse_args())
    

    if args["open"] > 0:
        print("open")
        # cmd = './remove_cache.sh'
        # process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')
        driver = get_driver(args)
        login_once(driver)
    elif args["server"]:
        #Remove cache except for login info
        cmd = './remove_cache.sh'
        process = subprocess.check_output(cmd, shell=True, executable='/bin/bash')
        driver = get_driver(args)
        cc_expname = args["name"]
        start_server_only("/users/rukshani/upload", driver, cc_expname)
        # zip_path = "/users/rukshani/upload" + "nflx-" + cc_expname + ".zip"
        zip_path = "/users/rukshani/upload/"+ cc_expname + ".zip"
        print(zip_path)
        zf = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
        for dirname, subdirs, files in os.walk("/users/rukshani/upload"):
            zf.write(dirname)
            print(dirname)
            for filename in files:
                print(filename)
                zf.write(os.path.join(dirname, filename))
        zf.close()
        # zipf = zipfile.ZipFile('test.zip', 'w', zipfile.ZIP_DEFLATED)
        # zipdir('/users/rukshani/upload', zipf)
        # zipf.close()
    # else:
    #     print("start streaming...")
    #     driver = get_driver(args)
    #     run_netflix(driver)

if __name__ == '__main__':
    parse_args()