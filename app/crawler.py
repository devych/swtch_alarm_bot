import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.alarm import sayBuy, sayWait

dwshop = "https://www.daewonshop.com/goods/goods_view.php?goodsNo=1000094791"
tmon = "http://www.tmon.co.kr/deal/810158162"

driver_path = "../chromedriver/chromedriver"

options = Options()
options.add_argument( '--headless' )
options.add_argument("lang=ko_KR")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36")
options.add_argument( '--log-level=3' )
options.add_argument( '--disable-loggin' )

driver = webdriver.Chrome(executable_path=driver_path, options=options)

driver.get(tmon)

driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 1060 OpenGL Engine';}return getParameter(parameter);};")

time.sleep(3)

el_stock = driver.find_elements_by_css_selector('#_wrapDealContents > div.tmde-template-wrapper.review_opt.r4._summaryOptionList > div > div:nth-child(1) > a > span.tmde-opt-thmb > div > span')
el_title = driver.find_elements_by_css_selector('#_wrapDealContents > div.tmde-template-wrapper.review_opt.r4._summaryOptionList > div > div:nth-child(1) > a > span.tmde-opt-info > cite')


el_stock = el_stock[0].get_attribute('outerHTML')[13:21]
el_title = el_title[0].get_attribute('innerHTML')

print(el_stock)
print(el_title)


driver.quit()