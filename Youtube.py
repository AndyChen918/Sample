import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized") # 視窗放到最大
options.add_experimental_option("detach", True)  # 保持浏览器的打开状态
driver = webdriver.Chrome(options=options)

# 變數
url = 'https://www.youtube.com/'

driver.get(url)

##################################################################################################
# 1.按下登入按鈕
login_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.yt-spec-button-shape-next")))
login_button.click()

# 2.找到帳號輸入框，並輸入帳號
username = 'prodigy0417@gmail.com'
username_input = driver.find_element(By.ID, "identifierId")
username_input.send_keys(username) 

# 3.點擊「下一步」按鈕
next_button = driver.find_element(By.ID, "identifierNext")
next_button.click()

# 4. 等候 5 秒後關閉瀏覽器
time.sleep(5)
driver.close()
driver.quit() 
##################################################################################################






#  [B] 搜尋特定串流
# 1.找到搜尋框元素
# search_box = driver.find_element(By.XPATH, "//input[@id='search']")

# 2.在搜尋框中輸入文字
# search_box.send_keys("Python programming")  # 在這裡替換為你想要搜索的內容

# 3.模擬按下 Enter 鍵執行搜索
# search_box.send_keys(Keys.ENTER)

# 4.等待幾秒，讓搜索結果頁面加載完成
# driver.implicitly_wait(5)







