#—*—coding=utf-8

import requests
from bs4 import BeautifulSoup
import MySQLdb
import time
import sys
import urllib2,urllib
from D_get_proxyip import get_proxy
import random

def insert_db(comments):
    now = time.strftime('%Y-%m-%d %H:%M:%S')
    shop_name = comments[0]
    commentator = comments[1]
    comments_info = comments[2]
    comments_time = comments[3]
    try:
        connetion = MySQLdb.connect(host='192.168.1.155', user='root',passwd='a12345', db='dzdp_ly', port = 3306, charset = 'utf8')
        cursor=connetion.cursor()  #获取操作游标
    except:
        print "Error to open database%"

    for i in range(len(commentator)):
        try:
            insert_db = '''
            INSERT INTO o_comments (insert_time,shop_name,commentator,comments_info,comments_time) VALUES ('%s','%s','%s','%s','%s');
            ''' % (now,shop_name,commentator[i],comments_info[i],comments_time[i])
            # 执行sql语句
            cursor.execute(insert_db)
            #提交到数据库执行
            connetion.commit()
        except:
            continue
    # 关闭游标
    cursor.close()
    # 关闭连接
    connetion.close()

def open_comments_url(url):
    time.sleep(5)
    hearder = {
        'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Cookie':'_lx_utm=utm_source%3DBaidu%26utm_medium%3Dorganic; _lxsdk_cuid=1612c48f4159b-02072e3af9fa0f-4323461-1fa400-1612c48f416c8; _lxsdk=1612c48f4159b-02072e3af9fa0f-4323461-1fa400-1612c48f416c8; _hc.v=5fb748a1-5a92-c225-1a8a-d9ddd7223ed3.1516866434; cy=2; cye=beijing; s_ViewType=10; _lxsdk_s=1612c48f418-360-087-9ad%7C%7C118; cityid=1; msource=default; default_ab=shop%3AA%3A1'
    }
    proxies = {'http':'61.135.217.7:80'}

    # # 将数据库中的代理ip全部导入
    # proxy_pool = get_proxy()
    # #随机选择一个代理ip
    # proxy_ip = random.choice(proxy_pool)
    # #随机选择一个user-agent
    # u_agent = random.choice(user_agent)

    #发起一次请求
    # response = requests.get(url,headers={'User-Agent':u_agent,'Cookie':Cookie},proxies={'http': proxy_ip})
    # response = requests.get(url,proxies={'http': proxy_ip})
    # response = requests.get(url,headers=hearder)

    #发起一次请求
    response = requests.get(url,headers=hearder,proxies=proxies)

    while response.status_code != 200 :
        try:
            # #随机选择一个user-agent
            # u_agent= random.choice(user_agent)
            # #随机选择一个代理ip
            # proxy_ip = random.choice(proxy_pool)
            #发起一次请求
            response = requests.get(url,headers=hearder,proxies=proxies)
            continue
        except:
            continue
    #使用lxml解析
    soup = BeautifulSoup(response.text,'lxml')
    return soup

def get_comments(soup):
    # soup = BeautifulSoup(html,'lxml')
    #获取门店名称
    shop_name = soup.find('div',class_='review-list-header').find('a').text
    #获取所有评论员
    commentator =  [i.text.replace('\r\n\t','').strip() for i in soup.find_all('a',attrs={'class':'name'})]
    #获取所有评论信息
    comments_info= [i.text.replace('\r\n\t','').replace(u'收起评论','').strip() for i in soup.find_all('div',attrs={'class':'review-words'})]
    #获取所有评论时间
    comments_time =[i.text.replace('\r\n\t','').strip()[-16:] for i in soup.find_all('span',attrs={'class':'time'})]

    return (shop_name,commentator,comments_info,comments_time)


def next_page(html):
    base_url = 'https://www.dianping.com'
    try:
        nextpage = html.find('a',attrs={'class':'NextPage'})['href']
        if nextpage:
            #拼接评论详情页url
            comments_url = base_url+nextpage
            #发起一次请求
            comments_html = open_comments_url (comments_url)
        else:
            print  u'已经翻到最后一页'
            return
    except:
        print  u'已经翻到最后一页'
        return
    return comments_html

class Get_comments:
    def __init__(self,url):
        self.url = url
        #发起一次请求
        comments_html = open_comments_url(self.url)
        #获取评论详情，数据存入列表
        comments = get_comments(comments_html)
        #插入数据库
        insert_db(comments)

        #判断是否存在下一页，存在-则爬取，不存在则退出
        next_html = next_page(comments_html)
        while next_html:
            #获取评论详情，数据存入列表
            insert_comments = get_comments(next_html)
            #插入数据库
            insert_db(insert_comments)
            next_html = next_page(next_html)
            if next_html:
                #获取评论详情，数据存入列表
                insert_comments = get_comments(next_html)
                #插入数据库
                insert_db(insert_comments)
                continue
            else:
                return

comments_url = 'http://www.dianping.com/shop/91031726/review_more/p1'
comments = Get_comments(comments_url)