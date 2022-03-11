# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#窗口相关
def function_set_window():
    driver.set_window_size(1024, 768)    # 设置浏览器宽1024，高768
    driver.maximize_window()    # 设置浏览器全屏显示
    driver.refresh()    # 刷新当前页面
    driver.back()    # 回退上一页
    driver.forward()    # 跳转下一页

#页面元素相关
def function_element():
    size = driver.find_element_by_id('kw').size    # 返回标签的尺寸
    text = driver.find_element_by_id('cp').text    # 返回标签的文本
    att = driver.find_element_by_id('kw').get_attribute('type')    # 返回元素属性值
    result = driver.find_element_by_id('kw').is_displayed()    # 判定元素是否可见

#输入框相关
def function_input():
    driver.find_element_by_id("kw").clear()    # 清空当前输入框内容再输入
    driver.find_element_by_id("kw").send_keys("Selenium2")
    driver.find_element_by_id("su").click()    #输入信息后，单击发送按钮
    driver.find_element_by_id("kw").submit()    # 效果同上，回车输入框

#鼠标相关操作
def function_mouse():
    right_click_element=driver.find_element_by_id("kw")    #定位元素，点击右键
    ActionChains(driver).context_click(right_click_element).perform()
    stop_element=driver.find_element_by_xpath('//div[@id="u1"]/a[text()="设置"]')    #鼠标悬停，弹出下拉菜单
    ActionChains(driver).move_to_element(stop_element).perform()
    double_click_element=driver.find_element_by_xpath('//div[@id="u1"]/a[text()="新闻"]')    #鼠标双击
    ActionChains(driver).double_click(double_click_element).perform()
    old_element=driver.find_element_by_xpath('//div[@id="u1"]/a[text()="新闻"]')    #鼠标拖动
    new_element=driver.find_element_by_id("kw")
    ActionChains(driver).drag_and_drop(old_element,new_element).perform()

#键盘相关操作
def function_keys():
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("kw").send_keys(Keys.BACK_SPACE)    #输入内容，退格
    driver.find_element_by_id("kw").send_keys(Keys.CONTROL,'a')
    driver.find_element_by_id("kw").send_keys(Keys.ENTER)

#多表单切换，页面内层级操作
def function_frame_mss():
    url_citcc="https://caigou.chinatelecom.com.cn/MSS-PORTAL/account/login.do"
    driver.get(url_citcc)
    time.sleep(3)
    iframe_element=driver.find_element_by_id("mainSubframe")
    driver.switch_to.frame(iframe_element)
    driver.find_element_by_id("loginUser").send_keys("suyb@citcc.cn")
    driver.find_element_by_id("loginPass").send_keys("CITcc67692346!!")
    randCode=input("请输入验证码:")
    driver.find_element_by_id("randCode").send_keys(randCode)
    driver.find_element_by_xpath('//*[@id="loginButton"]/img').click()

def function_wait():
    WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located((By.ID,'kw11')))#显式等待
    driver.implicitly_wait(10)#隐式等待,时间是虚数，并非真等10秒

#多窗口切换
def function_switch_window():
    driver.get("https://www.hao123.com/")
    #标记driver指向的页面
    first_windows=driver.current_window_handle
    print(driver.title)
    driver.find_element_by_id("search_logolink").click()
    #返回所有页面的列表
    all_handles=driver.window_handles

    #遍历列表，判定且将driver指向其他页面
    for i in all_handles:
        if i!=first_windows:
            driver.switch_to.window(i)
            second_windows=driver.current_window_handle
            print("进入新窗口")
            print(driver.title)
            time.sleep(1)

    for i in all_handles:
        if i==first_windows:
            driver.switch_to.window(i)
            print("进入初始窗口")
            print(driver.title)
            time.sleep(1)

#警告,Message: no such alert
def function_alert():
    link=driver.find_element_by_link_text("设置")
    ActionChains(driver).move_to_element(link).perform()

    driver.find_element_by_link_text("搜索设置").click()
    time.sleep(2)
    driver.switch_to.alert.accept()

def function_js():
    #鼠标滑到最下面
    js = "window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;"
    for i in range(5):
        time.sleep(1)
        driver.execute_script(js)

#chrome无图浏览
def function_no_images():
    chrome_opt = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_opt.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(chrome_options=chrome_opt)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    # url = "http://www.baidu.com"
    # driver.get(url)
    function_switch_window()
    time.sleep(1)
    driver.quit()