# -*- coding=utf-8 -*-
import requests
import logging
import logging.handlers
import time
import json
import sys
import random
from bs4 import BeautifulSoup
import smtplib
import re
from email.mime.text import MIMEText
from email.header import Header

import traceback

def setLogger(logFileName, logger):
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    file_handler = logging.handlers.RotatingFileHandler(
        logFileName, maxBytes=10485760, backupCount=5, encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


def sendMail(url, isOrder, sendTo):
    if len(sendTo) == 0 or sendTo == '$$$$$$$@qq.com':
        return

    mailRe = re.compile('^\w{1,15}@\w{1,10}\.(com|cn|net)$')
    if not re.search(mailRe, sendTo):
        return

    sendFrom = '645064582@qq.com'

    smtp_server = 'smtp.qq.com'
    if isOrder:
        msg = MIMEText(url + ' 商品已下单, 请在尽快付款', 'plain', 'utf-8')
    else:
        msg = MIMEText(url + ' 商品下单失败.', 'plain', 'utf-8')

    msg['From'] = Header(sendFrom)
    msg['To'] = Header(sendTo)
    msg['Subject'] = Header('买到啦')

    server = smtplib.SMTP_SSL(host=smtp_server)
    server.connect(smtp_server, 465)
    server.login(sendFrom, 'nkrzicfjkzznbehi')
    server.sendmail(sendFrom, sendTo, msg.as_string())
    server.quit()


def sendError(sendTo):
    if len(sendTo) == 0 or sendTo == '$$$$$$$@qq.com':
        return

    mailRe = re.compile('^\w{1,15}@\w{1,10}\.(com|cn|net)$')
    if not re.search(mailRe, sendTo):
        return

    sendFrom = '645064582@qq.com'

    # 发信服务器
    smtp_server = 'smtp.qq.com'
    # 邮箱正文内容, 第一个参数为内容, 第二个参数为格式(plain 为纯文本), 第三个参数为编码
    msg = MIMEText('main()函数出错嘞!', 'plain', 'utf-8')

    # 邮件头信息
    msg['From'] = Header(sendFrom)
    msg['To'] = Header(sendTo)
    msg['Subject'] = Header('ERROR!')
    # 开启发信服务, 加密传输
    server = smtplib.SMTP_SSL(host=smtp_server)
    server.connect(smtp_server, 465)
    server.login(sendFrom, 'nkrzicfjkzznbehi')
    server.sendmail(sendFrom, sendTo, msg.as_string())
    server.quit()


def get_tag_value(tag, key='', index=0):
    if key:
        value = tag[index].get(key)
    else:
        value = tag[index].text
    return value.strip(' \t\r\n')


def responseStatus(resp):
    if resp.status_code != requests.codes.OK:
        print('Status: %u, Url: %s' % (resp.status_code, resp.url))
        return False
    return True
def validateCookies(logger, session):
    for flag in range(1, 3):
        try:
            targetURL = 'https://order.jd.com/center/list.action'
            payload = {
                'rid': str(int(time.time() * 1000)),
            }
            resp = session.get(url=targetURL, params=payload, allow_redirects=False)
            if resp.status_code == requests.codes.OK:
                logger.info('登录成功!')
                return True
            else:
                logger.info('第[%s]次请重新获取cookie...', flag)
                time.sleep(5)
                continue
        except Exception as e:
            logger.info('第[%s]次请重新获取cookie...', flag)
            time.sleep(5)
            continue


def getUsername(logger, session):
    userName_Url = 'https://passport.jd.com/new/helloService.ashx?callback=jQuery339448&_=' + str(
        int(time.time() * 1000))
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://order.jd.com/center/list.action",
        "Connection": "keep-alive"
    }
    resp = session.get(url=userName_Url, allow_redirects=True)
    resultText = resp.text
    resultText = resultText.replace('jQuery339448(', '')
    resultText = resultText.replace(')', '')
    usernameJson = json.loads(resultText)
    logger.info('登录账号名称: ' + usernameJson['nick'])


def cancelSelectCartItem(session):
    url = "https://cart.jd.com/cancelAllItem.action"
    data = {
        't': 0,
        'outSkus': '',
        'random': random.random()
    }
    resp = session.post(url, data=data)
    if resp.status_code != requests.codes.OK:
        print('Status: %u, Url: %s' % (resp.status_code, resp.url))
        return False
    return True

def cart_detail(session, logger, isOutput=False):
    url = 'https://cart.jd.com/cart.action'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://order.jd.com/center/list.action",
        "Host": "cart.jd.com",
        "Connection": "keep-alive"
    }
    resp = session.get(url, headers=headers)
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
            logger.error("商品%s在购物车中的信息无法解析, 报错信息: %s, 该商品自动忽略", sku_id, e)

    if isOutput == True:
        logger.info('当前购物车信息: %s', cartDetail)
    return cartDetail

def change_item_num_in_cart(sku_id, vender_id, num, p_type, target_id, promo_id, session):
    url = "https://cart.jd.com/changeNum.action"
    data = {
        't': 0,
        'venderId': vender_id,
        'pid': sku_id,
        'pcount': num,
        'ptype': p_type,
        'targetId': target_id,
        'promoID': promo_id,
        'outSkus': '',
        'random': random.random(),
        # 'locationId'
    }
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "https://cart.jd.com/cart",
        "Connection": "keep-alive"
    }
    resp = session.post(url, data=data)
    return json.loads(resp.text)['sortedWebCartResult']['achieveSevenState'] == 2


def addItemToCart(sku_id, session, logger):
    url = 'https://cart.jd.com/gate.action'
    payload = {
        'pid': sku_id,
        'pcount': 1,
        'ptype': 1,
    }
    resp = session.get(url=url, params=payload)
    if 'https://cart.jd.com/cart.action' in resp.url:  # 套装商品加入购物车后直接跳转到购物车页面
        result = True
    else:  # 普通商品成功加入购物车后会跳转到提示 "商品已成功加入购物车！" 页面
        soup = BeautifulSoup(resp.text, "html.parser")
        result = bool(soup.select('h3.ftx-02'))  # [<h3 class="ftx-02">商品已成功加入购物车！</h3>]

    if result:
        logger.info('%s 已成功加入购物车', sku_id)
    else:
        logger.error('%s 添加到购物车失败', sku_id)


def get_checkout_page_detail(session, logger):
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
        resp = session.get(url=url, params=payload, headers=headers)
        if not responseStatus(resp):
            logger.error('获取订单结算页信息失败')
            return ''

        soup = BeautifulSoup(resp.text, "html.parser")
        risk_control = get_tag_value(soup.select('input#riskControl'), 'value')

        order_detail = {
            'address': soup.find('span', id='sendAddr').text[5:],  # remove '寄送至:  ' from the begin
            'receiver': soup.find('span', id='sendMobile').text[4:],  # remove '收件人:' from the begin
            'total_price': soup.find('span', id='sumPayPriceId').text[1:],  # remove '￥' from the begin
            'items': []
        }

        logger.info("下单信息: %s", order_detail)
        return order_detail
    except requests.exceptions.RequestException as e:
        logger.error('订单结算页面获取异常: %s' % e)
    except Exception as e:
        logger.error('下单页面数据解析异常: %s', e)
    return None


def submit_order(risk_control, session, logger, payment_pwd):
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
        resp = session.post(url=url, data=data, headers=headers)
        resp_json = json.loads(resp.text)

        if resp_json.get('success'):
            logger.info('订单提交成功! 订单号: %s', resp_json.get('orderId'))
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
            logger.info('订单提交失败, 错误码: %s, 返回信息: %s', result_code, message)
            logger.info(resp_json)
            return False
    except Exception as e:
        logger.error(e)
        return False


def item_removed(sku_id):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Referer": "http://trade.jd.com/shopping/order/getOrderInfo.action",
        "Connection": "keep-alive",
        'Host': 'trade.jd.com',
    }
    url = 'https://item.jd.com/{}.html'.format(sku_id)
    page = requests.get(url=url, headers=headers)
    return '该商品已下柜' not in page.text


def buyGood(sku_id, session, logger, payment_pwd):
    for count in range(1, 5):
        logger.info('第[%s/%s]次尝试提交订单', count, 3)
        cancelSelectCartItem(session)
        cart = cart_detail(session, logger)
        if sku_id not in cart:
            addItemToCart(sku_id, session, logger)
            cart_detail(session, logger, True)

        risk_control = get_checkout_page_detail(session, logger)
        if len(risk_control) > 0:
            if submit_order(risk_control, session, logger, payment_pwd):
                return True
        logger.info('等待%ss', 3)
        time.sleep(3)
    else:
        logger.info('执行结束, 提交订单失败！')
        return False

def main(sendTo, cookies_String, url):
    session = requests.session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/531.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "Connection": "keep-alive"
    }

    logFileName = 'jdAutoBuyGood.log'
    logger = logging.getLogger()
    setLogger(logFileName, logger)

    manual_cookies = {}
    for item in cookies_String.split(';'):
        # 用=号分割.
        name, value = item.strip().split('=', 1)
        manual_cookies[name] = value

    # print(manual_cookies)
    cookiesJar = requests.utils.cookiejar_from_dict(manual_cookies, cookiejar=None, overwrite=True)
    session.cookies = cookiesJar

    payment_pwd = ''
    flag = 1
    while (1):
        try:
            if flag == 1:
                validateCookies(logger, session)
                getUsername(logger, session)
            checkSession = requests.Session()
            checkSession.headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Connection": "keep-alive"
            }
            logger.info('第' + str(flag) + '次 查询...')
            flag += 1
            for i in url:
                # 商品url
                skuId = i.split('skuId=')[1].split('&')[0]
                skuidUrl = 'https://item.jd.com/' + skuId + '.html'
                response = checkSession.get(i)
                if (response.text.find('无货') > 0):
                    logger.info('[%s]商品无货.', skuId)
                else:
                    if item_removed(skuId):
                        logger.info('[%s]商品有货啦! 马上下单...', skuId)
                        if buyGood(skuId, session, logger, payment_pwd):
                            sendMail(skuidUrl, True, sendTo)
                            sys.exit(1)
                        else:
                            sendMail(skuidUrl, False, sendTo)
                        sys.exit(1)
                    else:
                        logger.info('[%s]商品有货, 但已下架.', skuId)
            time.sleep(5)
            if flag % 20 == 0:
                logger.info('校验是否还在登录...')
                validateCookies(logger, session)
        except Exception as e:
            print(traceback.format_exc())
            time.sleep(10)


if __name__ == '__main__':
    sendTo = ''
    cookies_String = ''
    fp = open("./Please fill out this document.txt", 'r', encoding='utf-8')
    cont = fp.read()
    pattern = re.compile("'(.*)'")
    contRe = pattern.findall(cont)
    if len(contRe) >= 2:
        sendTo = contRe[0]
        cookies_String = contRe[1]

    contRe = contRe[2:]

    try:
        main(sendTo, cookies_String, contRe)
    except Exception:
        sendError(sendTo)