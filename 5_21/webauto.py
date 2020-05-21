from selenium import webdriver

wd = webdriver.Chrome()

# 设置最大等待时长为 10秒
wd.implicitly_wait(10)

wd.get('https://www.baidu.com')

wd.find_element_by_id('kw').send_keys('周深\n')

wd.find_element_by_id('su').click()

element = wd.find_element_by_id('4')

print(element.get_attribute('class'))

wd.quit()
