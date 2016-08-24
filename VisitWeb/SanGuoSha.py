# _*_ coding:UTF-8 _*_
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
import os
import sys
from VisitWeb.WinKeyMouse import *
from VisitWeb.MyTimer import *


def getpath():
    if os.environ['PATH'].find('ChromeDriver') == -1:
        exe_dir_path = os.path.join(os.path.dirname(sys.path[0]), 'ChromeDriver')
        if os.path.isdir(exe_dir_path):
            exe_path = os.path.join(exe_dir_path, 'chromedriver.exe')
            if os.path.isfile(exe_path):
                #os.environ['PATH'] = ';'.join(exe_dir_path, os.environ['PATH'])
                return exe_path
    return 'chromedriver'


def sanguoshacheckin():
    browser = webdriver.Chrome(executable_path=getpath()) # Get local session of Chrome
    browser.get("http://web.sanguosha.com/") # Load page
    # elem = browser.find_element_by_id('kw') # Find the query box
    #time.sleep(5.0)
    browser.switch_to.frame('loginIframe')
    elem = browser.find_element_by_id('ptname')
    #elem = browser.find_element_by_class_name("ptname inputtxt")
    #elem = browser.find_element_by_name("ptname")
    #elem = browser.find_element_by_xpath('//*[@id="ptname"]')
    #elem = browser.find_element_by_id('loginIframe') #336*180
    #print elem.location
    #print browser.find_element_by_class_name('top_menu1').location
    #ActionChains(browser).move_to_element(elem).perform()
    #ActionChains(browser).move_by_offset(200, -170).click().send_keys("idealegg")
    elem.send_keys("idealegg")
    elem = browser.find_element_by_id('ptpwd')
    elem.send_keys("hd19881204"+ Keys.RETURN)
    #ActionChains(browser).move_by_offset(0, 50).click().send_keys("hd19881204"+ Keys.RETURN)
    # elem.send_keys("seleniumhq" + Keys.RETURN)
    time.sleep(3.0)
    browser.switch_to_default_content()
    browser.switch_to.frame('loginIframe')
    elem = browser.find_element_by_class_name("svr_btn")
    #time.sleep(3.0) # Let the page load, will be added to the API
    #div_check_in = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div");
    # use console to test xpath by:
    # $x("/html/body/div[1]/div[1]/div[2]/div/div[1]/div/div[2]/div")
    # ActionChains(browser).click(check_in_div).perform();
    ActionChains(browser).move_to_element(elem).perform()
    elem.click()

    mt = MyTimer()
    mt.start(1, hello)
    time.sleep(42.0)
    #browser.switch_to_default_content()
    #time.sleep(10.0)
    mt.stop()
    mt.start(1, hello)
    mouse_click(528, 623) # 确定
    time.sleep(3.0)
    mouse_click(506, 580) # 允许
    mt.stop()
    mt.start(1, hello)
    time.sleep(50.0)
    mouse_click(372, 519) # //身份场
    mt.stop()
    mt.start(1, hello)
    time.sleep(3.0)
    mouse_click(542, 710) # 进入大厅
    mt.stop()
    mt.start(1, hello)
    time.sleep(60.0)
    mouse_click(62, 302) # 签到
    mt.stop()
    mt.start(1, hello)
    time.sleep(5.0)

    mouse_click(459, 622)
    mouse_click(559, 622)
    mouse_click(659, 622)
    mouse_click(759, 622)
    mouse_click(859, 622)
    mouse_click(161, 710)

    #browser.find_element_by_id('sign-in-btn').click();
    '''
    >>> windll.user32.GetCursorPos(byref(po))
    1
    >>> ("(%i, %i)")%(po.x, po.y)
    '(528, 623)' // seting
    >>> windll.user32.GetCursorPos(byref(po))
    1
    >>> ("(%i, %i)")%(po.x, po.y)
    '(506, 580)'//setting
    >>> windll.user32.GetCursorPos(byref(po))
    1
    >>> ("(%i, %i)")%(po.x, po.y)
    '(372, 519)'//身份场
    >>> windll.user32.GetCursorPos(byref(po))
    1
    >>> ("(%i, %i)")%(po.x, po.y)
    '(542, 710)'//进入大厅
    >>> windll.user32.GetCursorPos(byref(po))
    1
    >>> ("(%i, %i)")%(po.x, po.y)
    '(62, 302)' //签到
    try:
        browser.find_element_by_xpath("//a[contains(@href,'http://seleniumhq.org')]")
    except NoSuchElementException:
        assert 0, "can't find seleniumhq"
    '''
    #browser.close()


if __name__ == '__main__':
    sanguoshacheckin()
