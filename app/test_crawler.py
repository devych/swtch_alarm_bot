import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from env.path import mac_chromedriver_path, mac_user_chrome_data_path

tmon = "http://www.tmon.co.kr/deal/810158162"
dwshop = "https://www.daewonshop.com/goods/goods_view.php?goodsNo=1000094791"
ssg = "http://shinsegaemall.ssg.com/item/itemView.ssg?itemId=1000035429874"
coupang = "https://www.coupang.com/vp/products/1384804427?isAddedCart="

siteList = [tmon, dwshop, ssg, coupang]


def stock_crawler(url):
    driver_path = mac_chromedriver_path

    options = Options()
    options.page_load_strategy = 'normal'
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("lang=ko_KR")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/81.0.4044.122 Safari/537.36")

    options.add_argument('--log-level=3')
    options.add_argument('--disable-loggin')
    options.add_argument(mac_user_chrome_data_path)
    driver = webdriver.Chrome(executable_path=driver_path, options=options)


    driver.get(url)
    driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
    driver.execute_script(
        "Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
    driver.execute_script(
        "const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

    time.sleep(5)

    if url is ssg:
        el_stock = driver.find_elements_by_css_selector('#oriCart')
        print(el_stock)

        el_stock = el_stock[0].get_attribute('outerHTML')
        print(el_stock)
        if 'soldout' in el_stock:
            # sendChannelMsg(f'현재 ssg에 닌텐도 스위치 동물의 숲 에디션 재고가 없습니다.\n다시 확인하고 알려드릴게요!\n{url}')
            pass
        else:
            print('ssg 재고 있음')
    elif url is coupang:
        el_stock = driver.find_elements_by_css_selector("#contents > div.prod-atf > div > div.prod-buy.sold-out.new-oos-style.not-loyalty-member.eligible-address.without-subscribe-buy-type.DISPLAY_0.only-one-delivery > div.prod-price-container")
        el_stock = el_stock[0].get_attribute('outerHTML')
        if '일시품절' in el_stock:
            # sendChannelMsg(f'현재 coupang에 닌텐도 스위치 동물의 숲 에디션 재고가 없습니다.\n다시 확인하고 알려드릴게요!\n{url}')
            pass
        else:
            print('coupang 재고 있음')



        driver.quit()

stock_crawler(ssg)