#!/bin/bash

docker build -t test_ui/test_ui .

docker run --privileged -d -p 4723:4723  -v /dev/bus/usb:/dev/bus/usb --name appium_test test_ui/test_ui
