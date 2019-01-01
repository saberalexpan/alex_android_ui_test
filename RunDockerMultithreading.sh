#!bin/bash

# 多线程，多server运行Appium
# 方法：
# 通过'lsusb'指定获取连接设备文件路径，such：/dev/bus/usb/001/002
# 使用前需要验证设备文件路径


docker build -t test_ui/test_ui .

docker run -d -p 4723:4723 --device /dev/bus/usb/001/002:/dev/bus/usb/001/002 -v ~/.android:/root/.android --name appium_1 test_ui/test_ui
docker run -d -p 4724:4723 --device /dev/bus/usb/001/003:/dev/bus/usb/001/003 -v ~/.android:/root/.android --name appium_2 test_ui/test_ui

adb kill-server

docker exec -it appium_1 adb devices
docker exec -it appium_2 adb devices
