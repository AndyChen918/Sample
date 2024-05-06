import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import Appium UiAutomator2 driver for Android platforms (AppiumOptions)
from appium.options.android import UiAutomator2Options

# vars
appium_server = '127.0.0.1:4723'
print(f"appium_server = {appium_server}")


### Control Android
capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Samsung Galaxy S10',
    appPackage='com.dlink.protocolverifier',
    appActivity='.routerhnap.ui.MainActivity',
    language='en',
    locale='US',
    dontStopAppOnReset='true',
    noReset='true',
    fullReset='false'
)

app_id = capabilities['appPackage']

# Converts capabilities to AppiumOptions instance
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
driver = webdriver.Remote(command_executor=appium_server,options=capabilities_options)
##################################################################################################

checkbox_1 = driver.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar")
checkbox_1.send_keys("Python programming")

checkbox_2 = driver.find_element(AppiumBy.ID, "com.android.chrome:id/url_bar")
checkbox_2.send_keys(Keys.ENTER)
print(f"Click HTTP")
time.sleep(2)

