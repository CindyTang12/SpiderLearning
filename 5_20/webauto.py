from selenium import webdriver


wd = webdriver.Chrome()
wd.get('https://baidu.com')
# 根据id选择元素，返回的就是该元素对应的WebElement对象
element = wd.find_element_by_id('kw')
# 通过该 WebElement对象，就可以对页面元素进行操作了
# 比如输入字符串到 这个 输入框里
element.send_keys('白月黑羽\n')
pass
