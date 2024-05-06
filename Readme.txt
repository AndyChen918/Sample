#####  避免閃退的方法  ######
#####  避免閃退的方法  ######
#####  避免閃退的方法  ######

dontStopAppOnReset='true',
noReset='true',
fullReset='false'


#####  WSA    #####
how to adb connect
Advance Settings
Developer mode on
adb connect 127.0.0.1:58526


#####   Docker Andoid   #####

1. esxi vm設定
	CPU 硬體虛擬化打勾, 這樣vm的 ubuntu 才能使用kvm
2. Hyper-v
	關閉vm
	Get-VMNetworkAdapter -VMName <VMName> | Set-VMNetworkAdapter -MacAddressSpoofing On
	
# 檢查 kvm	
sudo apt install cpu-checker
kvm-ok

doagent@node03-1:~/appium$ kvm-ok
INFO: /dev/kvm exists
KVM acceleration can be used



docker run -d -p 6080:6080 -e EMULATOR_DEVICE="Samsung Galaxy S10" -e WEB_VNC=true --device /dev/kvm --name android-container budtmo/docker-android:emulator_13.0


###########  Appium   ###################

---   docker android 已內含 Appium   ---

# real device
docker run --privileged -d -p 4723:4723  -v /dev/bus/usb:/dev/bus/usb --name appium-container appium/appium

# 只有手機模擬 , 但也內含了 appium
docker run --privileged -d -p 6080:6080 \
-e EMULATOR_DEVICE="Samsung Galaxy S10" \
-e WEB_VNC=true \
--device /dev/kvm \
--name android-container \
budtmo/docker-android:emulator_13.0

# 這有 APPIUM=true 參數與上面的差別在哪 ???? appium 開放了 port 可以使用程式去操控
docker run -d -p 6080:6080 -p 4723:4723 \
-e EMULATOR_DEVICE="Samsung Galaxy S10" \
-e WEB_VNC=true \
-e APPIUM=true \
-e EMULATOR_ARGS="-memory 8192 -partition-size 8096" \
--device /dev/kvm \
--name android-container \
budtmo/docker-android:emulator_13.0


# 這是連接 selenium-hub, APPIUM=true + SELENIUM_HOST="172.21.0.2"
docker run --privileged -d -p 4723:4723 \
-e DEVICE="Samsung Galaxy S10" \
-e APPIUM=TRUE \
-e CONNECT_TO_GRID=true \
-e APPIUM_HOST="node02" \
-e APPIUM_PORT=4723 \
-e SELENIUM_HOST="node02" \
-e SELENIUM_PORT=4444 \
--name appium-container \
budtmo/docker-android:emulator_13.0


-----   adb 指令   ---------

# 手機運行的log
adb logcat 2>&1 | tee dhm.log

adb devices

# 找到裝置的結果
List of devices attached
emulator-5554   device

# 安裝  apk
adb install protocol-verifier-debug.apk

# 查詢有甚麼  appPackage
手機上執行要查詢的app
adb shell
dumpsys activity | grep mFocused
or

dumpsys window displays | grep -E mCurrentFocus
結果: mCurrentFocus=Window{a5cc897 u0 com.dlink.protocolverifier/com.dlink.protocolverifier.routerhnap.ui.MainActivity}
or

dhm tools 
appPackage = com.dlink.protocolverifier
appActivity = com.dlink.protocolverifier.routerhnap.ui.MainActivity

dumpsys window displays | grep -E mFocusedApp
結果: mFocusedApp=ActivityRecord{c689fcf u0 com.dlink.protocolverifier/.routerhnap.ui.MainActivity} t20}
appPackage = com.dlink.protocolverifier
appActivity = .routerhnap.ui.MainActivity


----  python appium  -----

pip install Appium-Python-Client

capabilities = dict(
    platformName='Android', # don't change
    automationName='uiautomator2', # don't change
    deviceName='Samsung Galaxy S10',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

-----   如何找到手機元素  -----
安裝 Appium Inspector

ip: 執行 docker 的主機ip
port: 4723
依照上面的 capabilities 設定於 Appium Inspector


-------   Appium 連接本機模擬器   -------------

1.安裝 Appium Desktop
  Config
  Adroid Home
  Java Home: C:\Program Files\Java\jre-1.8 # 會自動補上 bin
  執行後會自動偵測 Appium Inspector 連接

2. adb connect
	WSA Bluestacks,看 USB debug enable 有資訊, 通常是 127.0.0.1:port
	adb connect 127.0.0.1:port
	adb devices # 查看是否連線成功

3. Appium Inspector
127.0.0.1:4723
Remote Path /wd/hub

{
  "appium:platformName": "Android",
  "appium:automationName": "uiautomator2",
  "appium:deviceName": "127.0.0.1:58526",  # 模擬器位置
  "appium:appPackage": "com.dlink.protocolverifier",
  "appium:appActivity": ".routerhnap.ui.MainActivity",
  "appium:language": "en",
  "appium:locale": "US"
}
