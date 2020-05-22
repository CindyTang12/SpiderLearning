from selenium import webdriver
from selenium.webdriver.support.select import Select  # 导入Select包
from selenium.webdriver.common.action_chains import ActionChains  # 导入鼠标事件包
from time import sleep

wd = webdriver.Chrome()
wd.maximize_window()
wd.get("http://data.eastmoney.com/futures/sh/data.html?date=2020-05-20&ex=069001005&va=RB&ct=rb2010")
wd.implicitly_wait(10)
ls = [{'s1_text': '上海期货交易所', 's1_value': '069001005', 's2_text': '螺纹钢', 's2_value': 'RB'},
      {'s1_text': '大连商品期货交易所', 's1_value': '069001007', 's2_text': '铁矿石', 's2_value': 'I'},
      {'s1_text': '郑州商品交易所', 's1_value': '069001008', 's2_text': '郑煤', 's2_value': 'ZC'}]


def getHTML(infodict):
    s1 = wd.find_element_by_id("futures_exchange")  # 这里先找到select的标签的id
    # 格式 Select(对应元素).select_by_对应方法("方法的对应值")
    # Select(s).select_by_index("1") #通过索引定位(从0开始计数)
    Select(s1).select_by_visible_text(infodict['s1_text'])  # 通过文本值定位
    Select(s1).select_by_value(infodict['s1_value'])  # 通过value值定位
    sleep(2)

    s2 = wd.find_element_by_id("futures_variety")  # 这里先找到select的标签的id
    Select(s2).select_by_visible_text(infodict['s2_text'])  # 通过文本值定位
    Select(s2).select_by_value(infodict['s2_value'])  # 通过value值定位
    sleep(2)


def getINFO():
    pass


def main():
    for infodict in ls:
        getHTML(infodict)
        getINFO()


if __name__ == '__main__':
    main()
wd.quit()
