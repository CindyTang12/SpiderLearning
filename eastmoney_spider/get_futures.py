import selenium
from selenium import webdriver
from selenium.webdriver.support.select import Select  # 导入Select包
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标事件包
from time import sleep
import time


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

wd = webdriver.Chrome()
wd.maximize_window()
wd.get("http://data.eastmoney.com/futures/sh/data.html?date=2020-05-20&ex=069001005&va=RB&ct=rb2010")
wd.implicitly_wait(10)
varietyls = [{'s1_text': '上海期货交易所', 's1_value': '069001005', 's2_text': '螺纹钢', 's2_value': 'RB'},
             {'s1_text': '大连商品期货交易所', 's1_value': '069001007', 's2_text': '铁矿石', 's2_value': 'I'},
             {'s1_text': '郑州商品交易所', 's1_value': '069001008', 's2_text': '郑煤', 's2_value': 'ZC'}]
ids = ['dt', 'kt']
numdict = {'永安期货': '80102901',
           '中信期货': '80050220',
           '银河期货': '80103797',
           '一德期货': '80102904',
           '方正中期期货': '80066668'}


def getHTML(infodict):
    # 选择交易所
    s1 = wd.find_element_by_id("futures_exchange")  # 这里先找到select的标签的id
    Select(s1).select_by_visible_text(infodict['s1_text'])  # 通过文本值定位
    Select(s1).select_by_value(infodict['s1_value'])  # 通过value值定位
    sleep(2)
    # 选择该交易所需要的品种
    s2 = wd.find_element_by_id("futures_variety")  # 这里先找到select的标签的id
    Select(s2).select_by_visible_text(infodict['s2_text'])  # 通过文本值定位
    Select(s2).select_by_value(infodict['s2_value'])  # 通过value值定位
    sleep(2)


def getINFO(id, num):
    if id == 'dt':
        suffix = '_2'
    elif id == 'kt':
        suffix = '_3'
    path = "//li[@id=\"" + num + suffix + "\"]/span[@class=\"IFe3\"]"
    element = wd.find_element_by_xpath(path)
    result = element.text
    return result


def main():
    for infodict in varietyls:
        try:
            print("============" + infodict['s1_text'] + "============")
            getHTML(infodict)
            for id in ids:
                if id == 'dt':
                    print("---多单量---")
                elif id == 'kt':
                    print("---空单量---")
                for num in numdict:
                    result = getINFO(id, numdict[num])
                    print(num + ":" + result)
        except selenium.common.exceptions.NoSuchElementException:
            print('没有抓取到相关数据呢，是不是还没到时间？')
            continue
    wd.quit()


if __name__ == '__main__':
    main()
