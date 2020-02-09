# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qsswindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer

import sys

import argparse
import os
import pickle
import random
import time
import json
import requests
import re
import logging
import logging.handlers
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
from email.header import Header

class Ui_QSSWindow(object):
    def setupUi(self, QSSWindow):
        QSSWindow.setObjectName("QSSWindow")
        QSSWindow.resize(680, 426)
        self.centralwidget = QtWidgets.QWidget(QSSWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.goods = QtWidgets.QHBoxLayout()
        self.goods.setObjectName("goods")
        self.labelGoods = QtWidgets.QLabel(self.groupBox)
        self.labelGoods.setObjectName("labelGoods")
        self.goods.addWidget(self.labelGoods)
        self.inputGoods = QtWidgets.QLineEdit(self.groupBox)
        self.inputGoods.setObjectName("inputGoods")
        self.goods.addWidget(self.inputGoods)
        self.verticalLayout.addLayout(self.goods)
        self.area = QtWidgets.QHBoxLayout()
        self.area.setObjectName("area")
        self.labelArea = QtWidgets.QLabel(self.groupBox)
        self.labelArea.setObjectName("labelArea")
        self.area.addWidget(self.labelArea)
        self.inputArea = QtWidgets.QLineEdit(self.groupBox)
        self.inputArea.setObjectName("inputArea")
        self.area.addWidget(self.inputArea)

        self.labelMail = QtWidgets.QLabel(self.groupBox)
        self.labelMail.setObjectName("labelMail")
        self.area.addWidget(self.labelMail)
        self.inputMail = QtWidgets.QLineEdit(self.groupBox)
        self.inputMail.setObjectName("inputMail")
        self.area.addWidget(self.inputMail)

        self.verticalLayout.addLayout(self.area)
        self.speedLayout = QtWidgets.QHBoxLayout()
        self.speedLayout.setObjectName("speedLayout")
        self.horizontalSlider = QtWidgets.QSlider(self.groupBox)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setProperty("value", 50)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setTickInterval(0)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.speedLayout.addWidget(self.horizontalSlider)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.speedLayout.addWidget(self.progressBar)
        self.verticalLayout.addLayout(self.speedLayout)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.loginBtn = QtWidgets.QPushButton(self.groupBox)
        self.loginBtn.setStyleSheet("")
        self.loginBtn.setObjectName("loginBtn")
        self.buttonLayout.addWidget(self.loginBtn)
        self.startBtn = QtWidgets.QPushButton(self.groupBox)
        self.startBtn.setStyleSheet("")
        self.startBtn.setObjectName("startBtn")
        self.buttonLayout.addWidget(self.startBtn)
        self.stopBtn = QtWidgets.QPushButton(self.groupBox)
        self.stopBtn.setStyleSheet("")
        self.stopBtn.setObjectName("stopBtn")
        self.buttonLayout.addWidget(self.stopBtn)
        self.verticalLayout.addLayout(self.buttonLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab, "")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")

        self.labelAboutMe = QtWidgets.QLabel(self.tab_1)
        # self.labelAboutMe.setGeometry(QtCore.QRect(50, 30, 280, 180))
        self.labelAboutMe.setObjectName("labelAboutMe")

        self.tabWidget.addTab(self.tab_1, "")
        self.verticalLayout_3.addWidget(self.tabWidget)
        QSSWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(QSSWindow)
        self.statusbar.setObjectName("statusbar")
        QSSWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(QSSWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 25))
        self.menubar.setObjectName("menubar")
        self.file = QtWidgets.QMenu(self.menubar)
        self.file.setObjectName("file")
        self.edit = QtWidgets.QMenu(self.menubar)
        self.edit.setObjectName("edit")
        QSSWindow.setMenuBar(self.menubar)
        self.file.addSeparator()
        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.edit.menuAction())

        self.retranslateUi(QSSWindow)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(QSSWindow)





    def retranslateUi(self, QSSWindow):
        _translate = QtCore.QCoreApplication.translate
        QSSWindow.setWindowTitle(_translate("QSSWindow", "MainWindow"))
        self.tabWidget.setToolTip(_translate("QSSWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.tabWidget.setWhatsThis(_translate("QSSWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("QSSWindow", "一定能尽快战胜疫情, 中国加油!"))
        self.labelGoods.setText(_translate("QSSWindow", "请输入商品ID(以逗号间隔):"))
        self.labelArea.setText(_translate("QSSWindow", "请输入收件地区编码:"))
        self.labelMail.setText(_translate("QSSWindow", "接受讯息邮箱:"))
        self.loginBtn.setText(_translate("QSSWindow", "扫码登录"))
        self.startBtn.setText(_translate("QSSWindow", "开始监控"))
        self.stopBtn.setText(_translate("QSSWindow", "停止监控"))

        self.labelAboutMe.setText(_translate("QSSWindow", '<h1>使用指南</h1> <a href="https://github.com/ZhangYikaii/auto-buy-Python-tool">请点击这里跳转</a> <h3>战疫情, 加油!</h3> <h4>欢迎在GitHub上加星. 谢谢!</h4>'))
        self.labelAboutMe.setOpenExternalLinks(True)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("QSSWindow", "Console"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("QSSWindow", "指南"))

        self.file.setTitle(_translate("QSSWindow", "文件"))
        self.edit.setTitle(_translate("QSSWindow", "编辑"))



class Autobuy(QtWidgets.QMainWindow, Ui_QSSWindow):
    def __init__(self):
        super().__init__()
        self.sess = requests.Session()
        self.sess.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "https://order.jd.com/center/list.action",
            "Connection": "keep-alive"
        }

        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "https://cart.jd.com/cart.action",
            "Connection": "keep-alive"
        }

        self.speed = 5000
        # self.isLogin = False
        self.cookiesString = ''
        self.cookies = {}
        self.skuidString = ''
        self.skuid = []
        self.cont = 1
        self.timer = QTimer(self)
        self.logger = logging.getLogger()
        self.loadQSS()
        self.setupUi(self)
        self.connectSign()
        self.initData()
        self.show()

    def loadQSS(self):
        file = 'window.qss'
        with open(file, 'rt', encoding='utf8') as f:
            styleSheet = f.read()
        self.setStyleSheet(styleSheet)
        f.close()

    def setLogger(self, logFileName='jdAutoBuyGood.log'):
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        file_handler = logging.handlers.RotatingFileHandler(
            logFileName, maxBytes=10485760, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)

    def initData(self):
        self.inputGoods.setText("65466451629,65437208345,7498169,7498165,1835968,7263128,7498167,17449572304,37934196731,100001086804,56657322838,56657322841,100005294853,1938795,15595191653,15595191654,45923412989,1835967,1336984,65466451629,7498169,7263128,4061438,65421329578,100005678825,100005294853,45923412989,62830056100,45006657879")
        self.inputArea.setText("16_1362_44319_51500")
        self.inputMail.setText("$$$$$$$@qq.com")
        self.horizontalSlider.setValue(50)
        self.horizontalSlider.setMaximum(100)
        self.horizontalSlider.setMinimum(0)
        self.setProgressBar()

        self.setLogger()

        if len(self.cookiesString) != 0:
            manual_cookies = {}
            for item in self.cookiesString.split(';'):
                # 用=号分割.
                name, value = item.strip().split('=', 1)
                manual_cookies[name] = value
            self.cookies = requests.utils.cookiejar_from_dict(manual_cookies, cookiejar=None, overwrite=True)
            self.sess.cookies = self.cookies

    def connectSign(self):
        self.horizontalSlider.valueChanged.connect(self.setProgressBar)
        self.horizontalSlider.valueChanged[int].connect(self.slvaluechange)

        self.loginBtn.clicked.connect(self.loginByQR)
        self.startBtn.clicked.connect(self.monitorConnect)
        self.stopBtn.clicked.connect(self.stopConnect)

    def stopConnect(self):
        self.updateStateText("已停止监控")
        self.timer.stop()

    def slvaluechange(self, val):
        # self.updateStateText("设置抢购速度: %d" % val)
        if val > 85:
            self.speed = 500
        elif val > 60:
            self.speed = 9000 - val * 100
        else:
            self.speed = 10000 - val * 100

    def setProgressBar(self):
        self.progressBar.setValue(self.horizontalSlider.value())

    def checkLogin(self):
        self.updateStateText('验证登录状态...')
        for flag in range(1, 3):
            try:
                targetURL = 'https://order.jd.com/center/list.action'
                payload = {
                    'rid': str(int(time.time() * 1000)),
                }
                resp = self.sess.get(url=targetURL, params=payload, allow_redirects=False)
                if resp.status_code == requests.codes.OK:
                    self.updateStateText('登录成功!')
                    return True
                else:
                    self.updateStateText('第 %s 次再尝试验证cookie...' % flag)
                    self.updateStateText('正在尝试从历史讯息中恢复...')
                    with open('cookie', 'rb') as f:
                        cookies = requests.utils.cookiejar_from_dict(pickle.load(f))
                    # print(cookies)
                    self.sess.cookies = cookies
                    continue
            except Exception as e:
                self.updateStateText(str(e))
                self.updateStateText('第 %s 次再尝试验证cookie...' % flag)
                continue
        self.updateStateText('请登录!')
        return False

    def loginByQR(self):
        # jd login by QR code
        try:
            self.updateStateText('请您打开京东手机客户端或微信扫一扫, 准备扫码登录')

            urls = (
                'https://passport.jd.com/new/login.aspx',
                'https://qr.m.jd.com/show',
                'https://qr.m.jd.com/check',
                'https://passport.jd.com/uc/qrCodeTicketValidation'
            )
            # step 1: open login page
            response = self.sess.get(
                urls[0],
                headers=self.headers
            )
            if response.status_code != requests.codes.OK:
                self.updateStateText(f'获取登录页失败: {response.status_code}')
                # self.isLogin = False
                return False
            # update cookies
            self.cookies.update(response.cookies)
            self.sess.cookies = response.cookies

            # step 2: get QR image
            response = self.sess.get(
                urls[1],
                headers=self.headers,
                cookies=self.cookies,
                params={
                    'appid': 133,
                    'size': 147,
                    't': int(time.time() * 1000),
                }
            )
            if response.status_code != requests.codes.OK:
                self.updateStateText(f'获取二维码失败: {response.status_code}')
                # self.isLogin = False
                return False

            # update cookies
            self.cookies.update(response.cookies)
            self.sess.cookies = response.cookies

            # save QR code
            image_file = 'qr.png'
            with open(image_file, 'wb') as f:
                for chunk in response.iter_content(chunk_size=1024):
                    f.write(chunk)

            # scan QR code with phone
            if os.name == "nt":
                # for windows
                os.system('start ' + image_file)
            else:
                if os.uname()[0] == "Linux":
                    # for linux platform
                    os.system("eog " + image_file)
                else:
                    # for Mac platform
                    os.system("open " + image_file)

            # step 3: check scan result
            self.headers['Host'] = 'qr.m.jd.com'
            self.headers['Referer'] = 'https://passport.jd.com/new/login.aspx'

            # check if QR code scanned
            qr_ticket = None
            retry_times = 1000  # 尝试1000次
            while retry_times:
                retry_times -= 1
                response = self.sess.get(
                    urls[2],
                    headers=self.headers,
                    cookies=self.cookies,
                    params={
                        'callback': 'jQuery%d' % random.randint(1000000, 9999999),
                        'appid': 133,
                        'token': self.cookies['wlfstk_smdl'],
                        '_': int(time.time() * 1000)
                    }
                )
                if response.status_code != requests.codes.OK:
                    continue
                rs = json.loads(re.search(r'{.*?}', response.text, re.S).group())
                if rs['code'] == 200:
                    self.updateStateText(f"{rs['ticket']}(Response Code: {rs['code']})")
                    qr_ticket = rs['ticket']
                    break
                else:
                    self.updateStateText(f"{rs['msg']}(Response Code: {rs['code']})")
                    time.sleep(2)

            if not qr_ticket:
                self.updateStateText("ERROR: 二维码登录失败")
                # self.isLogin = False
                return False

            # step 4: validate scan result
            self.headers['Host'] = 'passport.jd.com'
            self.headers['Referer'] = 'https://passport.jd.com/new/login.aspx'
            response = requests.get(
                urls[3],
                headers=self.headers,
                cookies=self.cookies,
                params={'t': qr_ticket},
            )
            if response.status_code != requests.codes.OK:
                self.updateStateText(f"二维码登录校验失败: {response.status_code}")
                # self.isLogin = False
                return False

            # 京东有时会认为当前登录有危险, 需要手动验证
            # url: https://safe.jd.com/dangerousVerify/index.action?username=...
            res = json.loads(response.text)
            if not response.headers.get('p3p'):
                if 'url' in res:
                    self.updateStateText(f"请进行手动安全验证: {res['url']}")
                    # self.isLogin = False
                    return False
                else:
                    self.updateStateText('登录失败, ERROR: ' + res)
                    # self.isLogin = False
                    return False

            # login succeed
            self.headers['P3P'] = response.headers.get('P3P')
            self.cookies.update(response.cookies)
            self.sess.cookies = response.cookies


            # save cookie
            with open('cookie', 'wb') as f:
                pickle.dump(self.cookies, f)

            self.updateStateText("登录成功!")
            # self.isLogin = True
            self.getUsername()
            return True

        except Exception as e:
            # self.isLogin = False
            self.updateStateText('ERROR: ' + str(e))
            raise

    def getUsername(self):
        userName_Url = 'https://passport.jd.com/new/helloService.ashx?callback=jQuery339448&_=' + str(
            int(time.time() * 1000))

        resp = self.sess.get(url=userName_Url, allow_redirects=True)
        resultText = resp.text
        resultText = resultText.replace('jQuery339448(', '')
        resultText = resultText.replace(')', '')
        usernameJson = json.loads(resultText)
        self.updateStateText('账号名称: ' + usernameJson['nick'])

    def checkStock(self):
        url = 'https://c0.3.cn/stocks'

        callback = 'jQuery' + str(random.randint(1000000, 9999999))

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "https://cart.jd.com/cart.action",
            "Connection": "keep-alive",
        }

        payload = {
            'type': 'getstocks',
            'skuIds': self.skuidString,
            'area': self.areaID,
            'callback': callback,
            '_': int(time.time() * 1000),
        }
        resp = self.sess.get(url=url, params=payload, headers=headers)
        respText = resp.text.replace(callback + '(', '').replace(')', '')
        respJson = json.loads(respText)
        inStockSkuid = []
        nohasSkuid = []
        abnormalSkuid = []
        for i in self.skuid:
            try:
                if respJson[i]['StockStateName'] != '无货':
                    inStockSkuid.append(i)
                else:
                    nohasSkuid.append(i)
            except Exception as e:
                abnormalSkuid.append(i)
        self.updateStateText('监控的 %d 个商品无货' % len(nohasSkuid))
        if len(abnormalSkuid) > 0:
            self.updateStateText('WARNING: [%s]编号商品查询异常' % ','.join(abnormalSkuid))
        return inStockSkuid

    def itemRemoved(self, sku_id):
        url = "https://c0.3.cn/stocks"

        params = {
            "skuIds": sku_id,
            "area": self.areaID,
            "type": "getstocks",
            "_": int(time.time() * 1000)
        }

        headers = {
            "Referer": f"https://item.jd.com/{sku_id}.html",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/75.0.3770.142 Safari/537.36",
        }
        try:
            response = requests.get(url, params=params, headers=headers)
            # print(response.text)    # 33: 现货    34: 无货     40: 可配货
            json_dict = json.loads(response.text)
            stock_state = json_dict[sku_id]['StockState']
            stock_state_name = json_dict[sku_id]['StockStateName']
            if stock_state != 34:
                self.updateStateText("%s 编号商品状态: %s" % (sku_id, stock_state_name))
                return True
            return False
        except Exception as e:
            self.updateStateText("itemRemoved function ERROR: %s" % str(e))

        return False



    def cart_detail(self, isOutput=False):
        url = 'https://cart.jd.com/cart.action'
        resp = self.sess.get(url, headers=self.headers)
        soup = BeautifulSoup(resp.text, "html.parser")

        cartDetail = dict()
        for item in soup.find_all(class_='item-item'):
            sku_id = item['skuid']  # 商品id
            try:
                # 例如: ['increment', '8888', '100001071956', '1', '13', '0', '50067652554']
                # ['increment', '8888', '100002404322', '2', '1', '0']
                item_attr_list = item.find(class_='increment')['id'].split('_')
                p_type = item_attr_list[4]
                promo_id = target_id = item_attr_list[-1] if len(item_attr_list) == 7 else 0

                def get_tag_value(tag, key='', index=0):
                    if key:
                        value = tag[index].get(key)
                    else:
                        value = tag[index].text
                    return value.strip(' \t\r\n')

                cartDetail[sku_id] = {
                    'name': get_tag_value(item.select('div.p-name a')),  # 商品名称
                    'verder_id': item['venderid'],  # 商家id
                    'count': int(item['num']),  # 数量
                    'unit_price': get_tag_value(item.select('div.p-price strong'))[1:],  # 单价
                    'total_price': get_tag_value(item.select('div.p-sum strong'))[1:],  # 总价
                    'is_selected': 'item-selected' in item['class'],  # 商品是否被勾选
                    'p_type': p_type,
                    'target_id': target_id,
                    'promo_id': promo_id
                }
            except Exception as e:
                self.updateStateText("ERROR: 商品%s在购物车中的信息无法解析, 报错信息: %s, 该商品自动忽略", sku_id, e)

        if isOutput == True:
            self.updateStateText('当前购物车信息: %s' % cartDetail)
        return cartDetail

    def addItemToCart(self, sku_id):
        url = 'https://cart.jd.com/gate.action'
        payload = {
            'pid': sku_id,
            'pcount': 1,
            'ptype': 1,
        }
        resp = self.sess.get(url=url, params=payload)
        if 'https://cart.jd.com/cart.action' in resp.url:  # 套装商品加入购物车后直接跳转到购物车页面
            result = True
        else:  # 普通商品成功加入购物车后会跳转到提示 "商品已成功加入购物车！" 页面
            soup = BeautifulSoup(resp.text, "html.parser")
            result = bool(soup.select('h3.ftx-02'))  # [<h3 class="ftx-02">商品已成功加入购物车！</h3>]

        if result:
            self.updateStateText('%s 编号商品已成功加入购物车' % sku_id)
        else:
            self.updateStateText('ERROR: %s 编号商品添加到购物车失败' % sku_id)

    def responseStatus(self, resp):
        if resp.status_code != requests.codes.OK:
            self.updateStateText('Status: %u, Url: %s' % (resp.status_code, resp.url))
            return False
        return True

    def getCheckoutPageDetail(self):
        url = 'http://trade.jd.com/shopping/order/getOrderInfo.action'
        # url = 'https://cart.jd.com/gotoOrder.action'
        payload = {
            'rid': str(int(time.time() * 1000)),
        }
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "https://cart.jd.com/cart.action",
            "Connection": "keep-alive",
            'Host': 'trade.jd.com',
        }
        try:
            resp = self.sess.get(url=url, params=payload, headers=headers)

            if not self.responseStatus(resp):
                self.updateStateText('ERROR: 获取订单结算页信息失败')
                return None
            soup = BeautifulSoup(resp.text, "html.parser")

            order_detail = {
                'address': soup.find('span', id='sendAddr').text[5:],
                'receiver': soup.find('span', id='sendMobile').text[4:],
                'total_price': soup.find('span', id='sumPayPriceId').text[1:],
                'items': []
            }

            self.updateStateText("下单信息: %s" % order_detail)
            return order_detail
        except requests.exceptions.RequestException as e:
            self.updateStateText('ERROR: 订单结算页面获取异常: %s' % e)
        except Exception as e:
            self.updateStateText('ERROR: 下单页面数据解析异常: %s' % e)
        return None

    def submit_order(self, risk_control, payment_pwd):
        url = 'https://trade.jd.com/shopping/order/submitOrder.action'
        # js function of submit order is included in https://trade.jd.com/shopping/misc/js/order.js?r=2018070403091

        # overseaPurchaseCookies:
        # vendorRemarks: []
        # submitOrderParam.sopNotPutInvoice: false
        # submitOrderParam.trackID: TestTrackId
        # submitOrderParam.ignorePriceChange: 0
        # submitOrderParam.btSupport: 0
        # riskControl:
        # submitOrderParam.isBestCoupon: 1
        # submitOrderParam.jxj: 1
        # submitOrderParam.trackId:

        data = {
            'overseaPurchaseCookies': '',
            'vendorRemarks': '[]',
            'submitOrderParam.sopNotPutInvoice': 'false',
            'submitOrderParam.trackID': 'TestTrackId',
            'submitOrderParam.ignorePriceChange': '0',
            'submitOrderParam.btSupport': '0',
            'riskControl': risk_control,
            'submitOrderParam.isBestCoupon': 1,
            'submitOrderParam.jxj': 1,
            'submitOrderParam.trackId': '9643cbd55bbbe103eef18a213e069eb0',  # Todo: need to get trackId
            # 'submitOrderParam.eid': eid,
            # 'submitOrderParam.fp': fp,
            'submitOrderParam.needCheck': 1,
        }

        def encrypt_payment_pwd(paymentPwd):
            return ''.join(['u3' + x for x in paymentPwd])

        if len(payment_pwd) > 0:
            data['submitOrderParam.payPassword'] = encrypt_payment_pwd(payment_pwd)

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
            "Referer": "http://trade.jd.com/shopping/order/getOrderInfo.action",
            "Connection": "keep-alive",
            'Host': 'trade.jd.com',
        }

        try:
            resp = self.sess.post(url=url, data=data, headers=headers)
            resp_json = json.loads(resp.text)

            if resp_json.get('success'):
                self.updateStateText('订单提交成功! 订单号: %s' % resp_json.get('orderId'))
                return True
            else:
                message, result_code = resp_json.get('message'), resp_json.get('resultCode')
                if result_code == 0:
                    # self._save_invoice()
                    message = message + '(下单商品可能为第三方商品, 将切换为普通发票进行尝试)'
                elif result_code == 60077:
                    message = message + '(可能是购物车为空或未勾选购物车中商品)'
                elif result_code == 60123:
                    message = message + '(未配置支付密码)'
                self.updateStateText('订单提交失败, 错误码: %s, 返回信息: %s' % (result_code, message))
                self.updateStateText(resp_json)
                return False
        except Exception as e:
            self.updateStateText("ERROR: " + str(e))
            return False

    def cancelSelectCartItem(self):
        url = "https://cart.jd.com/cancelAllItem.action"
        data = {
            't': 0,
            'outSkus': '',
            'random': random.random()
        }
        resp = self.sess.post(url, data=data)
        if resp.status_code != requests.codes.OK:
            self.updateStateText('cancelSelectCartItem() function WARNING: %u, Url: %s' % (resp.status_code, resp.url))
            return False
        return True

    def buyGoods(self, sku_id):
        for i in range(1, 2):
            self.updateStateText('第[%d/%d]次尝试提交订单...' % (i, 2))
            self.cancelSelectCartItem()
            cart = self.cart_detail()
            if sku_id not in cart:
                self.addItemToCart(sku_id)
                self.cart_detail(True)

            risk_control = self.getCheckoutPageDetail()
            if risk_control != None:
                if self.submit_order(risk_control, ''):
                    return True
            time.sleep(1)
        else:
            self.updateStateText('执行结束，提交订单失败！')
            return False

    def monitorConnect(self):
        if self.checkLogin() == False:
            return False
        self.skuidString = self.inputGoods.text()
        pattern = re.compile(",|，")
        self.skuid = pattern.split(self.skuidString)

        self.areaID = self.inputArea.text()

        self.timer.timeout.connect(self.monitorMain)
        self.updateStateText("当前轮询速度为 %f 秒/次" % (self.speed / 1000))
        self.timer.start(self.speed)  # 设置计时间隔并启动
        return True

    def sendMail(self, url, isOrder):
        sendTo = self.inputMail.text()
        if len(sendTo) == 0 or sendTo == '$$$$$$$@qq.com':
            return

        mailRe = re.compile('^\w{1,15}@\w{1,10}\.(com|cn|net)$')
        if not re.search(mailRe, sendTo):
            return

        sendFrom = '645064582@qq.com'

        smtp_server = 'smtp.qq.com'
        if isOrder:
            msg = MIMEText('您抢购的 ' + url + ' 商品已下单, 请在尽快付款.', 'plain', 'utf-8')
        else:
            msg = MIMEText('您抢购的 ' + url + ' 商品下单失败.', 'plain', 'utf-8')

        msg['From'] = Header(sendFrom)
        msg['To'] = Header(sendTo)
        msg['Subject'] = Header('京东商品自动购买程序提示讯息')

        server = smtplib.SMTP_SSL(host=smtp_server)
        server.connect(smtp_server, 465)
        server.login(sendFrom, 'nkrzicfjkzznbehi')
        server.sendmail(sendFrom, sendTo, msg.as_string())
        server.quit()

    def monitorMain(self):
        try:
            checkSession = requests.Session()
            checkSession.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Connection": "keep-alive"
            }
            self.updateStateText('第 ' + str(self.cont) + ' 次查询:')
            self.cont += 1
            inStockSkuid = self.checkStock()
            skuidUrl = 'https://item.jd.com/'
            for skuId in inStockSkuid:
                if self.itemRemoved(skuId):
                    self.updateStateText('%s 编号商品有货啦! 马上下单' % skuId)
                    skuidUrl = 'https://item.jd.com/' + skuId + '.html'
                    if self.buyGoods(skuId):
                        self.sendMail(skuidUrl, True)
                        self.stopConnect()
                    else:
                        self.sendMail(skuidUrl, False)
                else:
                    self.updateStateText('%s 编号商品有货，但已下柜商品' % skuId)

            if self.cont % 300 == 0:
                self.checkLogin()
        except Exception as e:
            import traceback
            self.updateStateText(traceback.format_exc())

    def updateStateText(self, stateText):
        # print(stateText)
        self.logger.info(stateText)
        self.textEdit.moveCursor(QtGui.QTextCursor.End)
        self.textEdit.insertPlainText(f'{time.ctime()} > ' + stateText + '\n')

def main():
    app = QApplication(sys.argv)
    test = Autobuy()
    sys.exit(app.exec_())



if __name__ == '__main__':
    main()