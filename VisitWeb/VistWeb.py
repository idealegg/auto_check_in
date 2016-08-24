from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys


def getPath():
    if os.environ['PATH'].find('ChromeDriver') == -1:
        exe_dir_path = os.path.join(os.path.dirname(sys.path[0]), 'ChromeDriver')
        if os.path.isdir(exe_dir_path):
            exe_path = os.path.join(exe_dir_path, 'chromedriver.exe')
            if os.path.isfile(exe_path):
                #os.environ['PATH'] = ';'.join(exe_dir_path, os.environ['PATH'])
                return exe_path
    return 'chromedriver'


def baiduzhidao():
    browser = webdriver.Chrome(executable_path=getPath()) # Get local session of Chrome
    browser.get("https://zhidao.baidu.com/ihome") # Load page
    # elem = browser.find_element_by_id('kw') # Find the query box
    elem = browser.find_element_by_id('TANGRAM__PSP_8__userName')
    elem.send_keys("***")
    elem = browser.find_element_by_id('TANGRAM__PSP_8__password')
    elem.send_keys("***"+ Keys.RETURN)
    # elem.send_keys("seleniumhq" + Keys.RETURN)
    time.sleep(3.0) # Let the page load, will be added to the API
    div_check_in = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div");
    # use console to test xpath by:
    # $x("/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div")
    # ActionChains(browser).click(check_in_div).perform();

    ActionChains(browser).move_to_element(div_check_in).perform();
    div_check_in.click();

    time.sleep(1.0)

    browser.find_element_by_id('sign-in-btn').click();
    '''
    try:
        browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
    except NoSuchElementException:
        assert 0, "can't find seleniumhq"
    '''
    browser.close()

if __name__ == '__main__':
    baiduzhidao()