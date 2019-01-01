# Android UI 自动化测试框架--python

*****

## 框架简介：

测试框架是以Selenium为底层，基于appium，OpenCV搭建，框架设计模式是 Page Object。

参考资料：
* https://www.seleniumhq.org/
* http://appium.io/
* http://airtest.netease.com/
* https://airtest.readthedocs.io/zh_CN/latest/_modules/airtest/report/report.html
* https://github.com/JennyHui/appiumDemo/tree/master/pythonDemo%20v1.0/PO
*****
*****

## 测试框架设计理念：Page object
整套测试框架采用Page Object（以下简称‘PO’）设计.

* 框架分层：
* 根据PO设计理念，对自动化测试框架进行分层，本框架分层如下：
    * Base Function层(基础方法层)，该层存放所有测试中会用到的基础方法(包含查找元素，点击，输入...)
    * 项目层,测试框架的base function层适用且兼容Android移动端，web网页端的测试；项目层下包含：
        * 元素层（ELement）存放元素
        * 页面层（Page Action）使用base层跟元素层组成可复用的操作层
        * 组装层（Build Cases）使用Page层的操作组成所需的自动化测试用例（此层不设计运行代码）
        * 用例层（Test Cases）运行BuildCases里面的测试用例（python unittest）
    * Report(报告层)，用于存放测试报告
    * TestEnvironment（环境层），存放移动端跟web端的测试环境
    * 测试组件run_case.py：该层运用HTMLTestRunner运行所有测试用例，并生成测试报告
    
*****
*****

## 测试框架安装/部署/运行

### 本地安装/运行

#### Linux/Mac

##### Linux

* 安装nodejs,npm
  * `sudo apt-get install nodejs`
  * `sudo apt-get install npm`
* 安装 python，pip
  * `sudo apt-get install python python-dev python-pip`
  * 使用pip安装测试所需要用到的依赖包：`pip install opencv-python Appium-Python-Client urllib3 AxmlParserPY`
* 安装Android SDK,ADB
  * 安装java
    * `sudo apt-get install openjdk-8-jre`
  * 下载，安装，配置Android SDK
    * `cd ~`
    * `wget http://dl.google.com/android/android-sdk_r24.4.1-linux.tgz`
    * `tar xvzf android-sdk_r24.4.1-linux.tgz`
    * `sudo rm android-sdk_r24.4.1-linux.tgz`
    * `vi ~/.profile`
  * 把SDK，platform-tools添加为环境变量
    * `source ~/.profile`
  * 安装adb
    * `sudo apt-get install adb`
      * 验证adb是否启动
         * 插入USB设备，开启USB调试
         * `adb devices`若显示设备状态为device，则证明adb安装并启动成功（adb监听本机5037端口，linux可以通过sudo lsof -i查到）
* 安装 OpenCV
  * 安装依赖包`apt install -y build-essential cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev`
  * 安装OpenCV 
    * `mkdir opencv`
    * `cd opencv`
    * `git clone https://github.com/opencv/opencv.git`
    * `mkdir build`
    * `cd build`
    * `cmake -D CMAKE_BULLD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ../opencv`
    * `make`
    * `make install`
* 使用npm 安装appium
    * `sudo npm install -g appium@latest`
    * 启动appium:命令行输入`appium`(appium加具体参数，具体详见`appium --help`)

*****
            
##### MAC
* 安装homebrew
    * `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`
* 通过brew 安装nodejs，npm
    * `brew install node`
* 使用mac自带的python，pip安装依赖包
    * `pip install opencv-python Appium-Python-Client urllib3 AxmlParserPY`
* 安装Android SDK
    * `brew update`
    * `brew install android-sdk`
* 安装OpenCV
    * `sudo brew install cmake`
    * `git clone https://github.com/opencv/opencv.git`
    * `cd opencv`
    * `mkdir build`
    * `cd build`
    * `cmake ..`
    * `make`
    * `sudo make install`
* npm 安装appium
    * `sudo npm install -g appium@latest`
    * 启动appium:命令行输入`appium`(appium加具体参数，具体详见`appium --help`)
    
*****
    
### 远程部署
#### 关键词：Jenkins，docker，AWS codecommitt

#### Docker 部署

##### Linux
* OpenCV,python安装详见‘本地安装/运行--linux’
* docker 安装
    * `sudo snap install docker`
* docker appium运行
    * `docker pull appium/appium`
    * `docker run --privileged -d -p 4723:4723  -v /dev/bus/usb:/dev/bus/usb --name <container name> appium/appium`
    * 验证appium是否运行
        * `curl http://localhost:4723`若appium已运行则返回`The URL '/' did not map to a valid resource`
    
*****
    
##### MAC
* OpenCV,python安装详见‘本地部署--Mac’
* docker 安装
    * 详见链接[dockerMac安装](https://docs.docker.com/docker-for-mac/install/)
* 下载并安装virtualbox，下载链接[VirtualBox_Download](https://download.virtualbox.org/virtualbox/5.2.22/VirtualBox-5.2.22-126460-OSX.dmg)
* 启动docker
* docker appium 在MAC环境下运行
    * `docker-machine create --driver virtualbox <your machine name>`
    * `docker-machine stop <your machine name>`
    * `vboxmanage modifyvm <your machine name> --usb on --usbehci on`
    * `docker-machine <your machine name>`
    * virtualbox 需要安装最新版本的[Extension Pack](https://download.virtualbox.org/virtualbox/5.2.22/Oracle_VM_VirtualBox_Extension_Pack-5.2.22.vbox-extpack)
    * 将本机的adb server关掉`adb kill-server`
    * `docker-machine ssh <your machine name>`
    * `docker run --privileged -d -p 4723:4723  -v /dev/bus/usb:/dev/bus/usb --name <container name> appium/appium`
    * 验证docker容器是否运行`docker exec -it <container name> adb devices`
        * 注：Mac上运行docker容器，appium webdriver地址为容器ip地址+端口4723（自定义端口）

*****

#### Jenkins + AWS code commit部署自动化测试项目

>暂未支持Jenkins在docker下appium/selenium框架部署（定制专用dockerfile后再补充相应文档）
>Jenkins AWScodecommit配置参照官方blog：[aws codecommitt Jenkins配置](https://aws.amazon.com/cn/blogs/devops/integrating-aws-codecommit-with-jenkins/)
* linux
    * [JenkinsLinux安装](https://jenkins.io/doc/book/installing/#debianubuntu)
    * 其他插件安装详见本地部署或docker部署
* Mac
    * [JenkinsMac安装](https://jenkins.io/doc/book/installing/#macos)
    * 其他插件安装详见本地部署或docker部署
 
 ##### 在Jenkins运行UI自动化测试

* linux/mac 运行`sudo service jenkins start`
* 在有GUI界面的设备上进入Jenkins主页
    * 若Jenkins为新安装，在特定文件内找到第一次登陆密码，插件按照Jenkins默认安装
* 在系统管理-->插件管理-->可选插件安装`AWS CodeCommit URL Helper`
* 在凭据中添加`Username with password`跟`aws credentials`这两个全局凭据
* 新建一个自由风格的Jenkins项目，Jenkins项目配置如下
    * 源码管理内选择`git`,URL为aws codecommit的https地址
        * 	Additional Behaviours新增`AWS Codecommit URL Helper`并配置凭据中的`aws credentials`
    * 新建定时构建，时间为`H 18 * * *`
    * 添加构建内容,使用shell脚本执行`python run_cases.py`(若出现找不到文件路径的报错，则在`python run_cases.py`前添加一句`cd your-project-file`)
    * 应用配置
* 执行构建
>这一块会随着调试更新

*****
*****

## 框架API

### BaseMethod

* 查找元素：`find_element`
    * 基于Selenium, Appium的`By`,`MobileBy`两个模块对`find_element`进行重新定义；
    * 对元素进行定位，以便进行下一步操作（Base类里面最基础的方法，涉及元素的操作都需要用到`find_element`）
    * ``find_element(attribute, loc)``
        * `attribute`:查找元素的方法/渠道（通过什么方法），方法支持的渠道有：id,xpath,android_UiAutoMATOR
        * `loc`:元素属性值    
        * return ``webElement``

* 点击元素：``click_element``
    * 使用``find_element``进行元素定位，定位成功后进行点击事件

* 输入文本：``input_text``
    * 使用``find_element``进行元素定位，输入框定位
    * 点击输入框（有输入属性的元素）
    * 清除输入框内原有的文字，避免影响输入
    * 向输入框输入测试文本
    * 在web测试中，元素属性带有`input`标签的，`input_text`可以用于上传文件（`value`参数输入文件路径）

* 获取元素/窗口/屏幕大小（size/bound）
    * `get_element_size`，通过`find_element`获取元素，使用`size`获取元素`weigh`,`height`
    * `get_windows_size`, 手机端获取手机分辨率；web端获取浏览器的`weigh`,`height`
    
* 发送键盘事件
    * `keyboard`：web自动化专用，通过selenium向系统发送组合按钮事件，如`curl + c`复制
    * `key_code`：Android自动化专用，向手机发送按钮事件，如按返回键

* 获取截图（OpenCV方法需要获取屏幕截图）
    * `get_original_image`：获取一张截图并保存到指定目录
    * `__SavePicture__`：通过webDriver进行截图，并通过`__CustomPicturePath__`方法创建图片保存路径
    * `__CustomPicturePath__`：创建图片路径

* `__findElement__`对`find_element`的补充：
    * 该方法通过selenium的WebDriverWait(显示等待)对元素进行定位
    
* `__data__`,`__localtime__`, `__ReturnWordFile__`:获取本地时间，返回当前文件工作路径

*****

### Assert

> 继承于BaseMethod,对测试预期结果断言模块
* 元素文本断言
    * 对指定元素的文本进行断言
    * ``element_text_assert(self, attribute, loc, text=None)``

* 元素存在
    * 指定元素是否存在于dom上（元素可以为不显示，但必须存在于dom上面）
    
* 元素不存在
    * 指定元素不存在dom上（元素不能为隐藏元素）
    
*****

### BaseCV, CVActionMethod

> 方法设计背景：自动化测试用完成编码后,某一模块大范围出现'NOT FOUND ELEMENT'报错，经排查发现该模块的核心元素没有属性，无法使用'find element'定位
> 方法设计参考air test测试框架

#### BaseCV

* ``image(original_image, target_image, precision=0.9, image_method=cv2.TM_CCOEFF_NORMED)``
    * 方法所需参数：
        * 素材原图
        * 目标图片（元素的UI位置）
        * 相关匹配值（默认为0.9，取值范围[0, 1]）
        * 图片匹配模式（默认TM_CCOEFF_NORMED{归一化相关系数匹配法}，若需要更改匹配模式，则需要修改"相关匹配值"）
    * 返回值（返回内容）
        * 目标元素的三组坐标（左上角坐标， 右下角坐标， 中心点左边）

*****

#### CVActionMethod

> 继承于BaseCV

* 点击图片`click_image(self, original, target, precision=None)`
    * 获取目标元素的中心点坐标
    * 点击坐标`driver.tap(bound)`
    
* 输入文本`input_text(self, original, target, value, precision=None)`
    * 获取目标元素中心坐标
    * 通过`os`模块向系统发送`adb shell`文本输入命令
