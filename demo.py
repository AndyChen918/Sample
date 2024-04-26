import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") # 視窗放到最大
options.add_experimental_option("detach", True)  # 保持浏览器的打开状态
driver = webdriver.Chrome(options=options)

# 變數
url = 'http://192.168.200.1'
passwd = 'admin123'

driver.get(url)

# 延遲 3 秒
time.sleep(3)

# Change Language to English
language_select = Select(driver.find_element(By.ID, "Language"))
desired_language = "en-us"
language_select.select_by_value(desired_language)
time.sleep(1)

# input password       
password = driver.find_element("name","admin_Password")
actions = ActionChains(driver)
actions.move_to_element(password).click().perform()
time.sleep(1)

password.send_keys(passwd + Keys.ENTER)
print("Enter Password")
time.sleep(3)

# 按下 setting
elm = driver.find_element(By.ID, 'menu_Settings')
elm.click()
time.sleep(1)

# 按下 network
elm = driver.find_element(By.ID, 'submenu_Network')
elm.click()
time.sleep(1)

# 5 秒後關閉瀏覽器
time.sleep(5)
driver.close()
driver.quit() 






