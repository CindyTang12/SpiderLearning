import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select  # 导入Select包
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标事件包
from time import sleep
import time
import pymysql
from selenium.webdriver.common.keys import Keys


class Spider:

    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.maximize_window()
        self.wd.get("http://data.eastmoney.com/futures/sh/data.html?date=2020-05-20&ex=069001005&va=RB&ct=rb2010")
        self.wd.implicitly_wait(10)
        self.varietyls = [{'s1_text': '上海期货交易所', 's1_value': '069001005', 's2_text': '螺纹钢', 's2_value': 'RB'},
                          {'s1_text': '大连商品期货交易所', 's1_value': '069001007', 's2_text': '铁矿石', 's2_value': 'I'},
                          {'s1_text': '郑州商品交易所', 's1_value': '069001008', 's2_text': '郑煤', 's2_value': 'ZC'}]
        self.ids = ['dt', 'kt']
        self.numdict = {'永安期货': '80102901',
                        '中信期货': '80050220',
                        '银河期货': '80103797',
                        '一德期货': '80102904',
                        '方正中期期货': '80066668'}
        self.future_link_dict = {'螺纹钢': 'http://quote.eastmoney.com/center/gridlist2.html#futures_113_7',
                                 '铁矿石': 'http://quote.eastmoney.com/center/gridlist2.html#futures_114_13'}

    def getHTML(self, infodict):
        s1 = self.wd.find_element_by_id("futures_exchange")  # 这里先找到select的标签的id
        Select(s1).select_by_visible_text(infodict['s1_text'])  # 通过文本值定位
        Select(s1).select_by_value(infodict['s1_value'])  # 通过value值定位
        sleep(2)
        # 选择该交易所需要的品种
        s2 = self.wd.find_element_by_id("futures_variety")  # 这里先找到select的标签的id
        Select(s2).select_by_visible_text(infodict['s2_text'])  # 通过文本值定位
        Select(s2).select_by_value(infodict['s2_value'])  # 通过value值定位
        sleep(2)

    def getEachInfo(self, id, num):
        if id == 'dt':
            suffix = '_2'
        elif id == 'kt':
            suffix = '_3'
        path = "//li[@id=\"" + num + suffix + "\"]/span[@class=\"IFe3\"]"
        element = self.wd.find_element_by_xpath(path)
        result = element.text
        return result

    def connectToMySQL(self, host, port, user, password, dbname, charset):
        try:
            self.conn = pymysql.connect(host=host,
                                        port=port,
                                        user=user,
                                        password=password,
                                        db=dbname,
                                        charset=charset)
            self.cur = self.conn.cursor()
        except:
            print('连接不成功')
        sql = """
        CREATE TABLE IF NOT EXISTS future_info(
        date Date,
        location CHAR(10) NOT NULL,
        name CHAR(10) NOT NULL,
        multi_quantity INT NOT NULL,
        empty_quantity INT NOT NULL
        )ENGINE=innodb DEFAULT CHARSET=utf8;
        """
        # 执行SQL语句
        self.cur.execute(sql)

    def insertInfo(self):
        cow_close = self.wd.find_element_by_css_selector('#intellcontclose')
        ActionChains(self.wd).move_to_element(cow_close).click().perform()
        for infodict in self.varietyls:
            try:
                date = time.strftime("%Y-%m-%d", time.localtime())
                location = infodict['s1_text']
                self.getHTML(infodict)
                search_botton = self.wd.find_element_by_css_selector('[onclick="searchData(false)"]')
                search_botton.click()
                sleep(2)
                for name, num in self.numdict.items():
                    multi_quantity = self.getEachInfo('dt', num)
                    empty_quantity = self.getEachInfo('kt', num)
                    info = [date, location, name, multi_quantity, empty_quantity]
                    sql = "INSERT INTO future_info(date, location, name, multi_quantity, empty_quantity) values(%s, %s, %s, %s, %s)"
                    self.cur.execute(sql, tuple(info))
                    self.conn.commit()
            except selenium.common.exceptions.NoSuchElementException:
                print('没有抓取到相关数据，是不是还没到时间？')
                continue
        self.wd.quit()


if __name__ == '__main__':
    spider = Spider()
    spider.connectToMySQL("localhost", 3306, "root", "12345678", "test", "utf8")
    spider.insertInfo()
