FROM appium/appium

RUN apt-get update && \
    apt-get install -y python python-dev python-pip && \
    apt install -y build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev && \
    pip install --upgrade pip opencv-python Appium-Python-Client urllib3 AxmlParserPY