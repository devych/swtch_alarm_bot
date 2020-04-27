import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.telegram_bot import sendChannelMsg
from env.path import win_chromedriver_path, win_user_chrome_data_path

tmon = "http://www.tmon.co.kr/deal/810158162"
dwshop = "https://www.daewonshop.com/goods/goods_view.php?goodsNo=1000094791"
ssg = "http://shinsegaemall.ssg.com/item/itemView.ssg?itemId=1000035429874"
coupang = "https://www.coupang.com/vp/products/1384804427?isAddedCart="
sofrano = "https://sofrano.com/product/detail.html?product_no=555"
siteList = [tmon, dwshop, ssg, coupang, sofrano]


def stock_crawler(url):
    driver_path = win_chromedriver_path

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
    options.add_argument(win_user_chrome_data_path)
    driver = webdriver.Chrome(executable_path=driver_path, options=options)

    try:
        driver.get(url)
        driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
        driver.execute_script(
            "Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
        driver.execute_script(
            "const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")

        time.sleep(5)

        if url is tmon:
            is_tmon_stock = False

            for i in range(0, 10):
                el_stock = driver.find_elements_by_css_selector(
                    f'#_wrapDealContents > div.tmde-template-wrapper.review_opt.r4._summaryOptionList > div > div:nth-child({i + 1}) > a')
                el_stock = el_stock[0].get_attribute('outerHTML')
                if f'data-order="{i}"' in el_stock and 'sold_out' in el_stock:
                    # sendChannelMsg(f'현재 티몬에 닌텐도 스위치 동물의 숲 에디션 재고가 없습니다.\n다시 확인하고 알려드릴게요!\n{url}')
                    pass
                else:
                    is_tmon_stock = True
                    print('tmon 재고 있음')
                    break
            if is_tmon_stock:
                sendChannelMsg(f'닌텐도 스위치가 입고되었습니다.\n아래 링크로 접속하여 구매하세요.\n{url}')

        elif url is dwshop:
            el_stock = driver.find_elements_by_css_selector('#frmView > div > div.btn')
            el_stock = el_stock[0].get_attribute('outerHTML')

            if '구매 불가' in el_stock and 'soldout' in el_stock:
                # sendChannelMsg(f'현재 대원샵에 닌텐도 스위치 동물의 숲 에디션 재고가 없습니다.\n다시 확인하고 알려드릴게요!\n{url}')
                pass
            else:
                print('대원샵 재고 있음')
                sendChannelMsg(f'지금 닌텐도 스위치 동물의 숲 에디션이 입고되었습니다.\n아래 링크로 접속하여 구매하세요.\n{url}')

        elif url is ssg:
            el_stock = driver.find_elements_by_css_selector('#oriCart')
            el_stock = el_stock[0].get_attribute('outerHTML')
            if '품절' in el_stock and 'soldout' in el_stock:
                # sendChannelMsg(f'현재 ssg에 닌텐도 스위치 동물의 숲 에디션 재고가 없습니다.\n다시 확인하고 알려드릴게요!\n{url}')
                pass
            else:
                print('ssg 재고 있음')
                sendChannelMsg(f'지금 닌텐도 스위치 동물의 숲 에디션이 입고되었습니다.\n아래 링크로 접속하여 구매하세요.\n{url}')
        elif url is coupang:
            el_stock = driver.find_elements_by_css_selector("#contents > div.prod-atf > div > div.prod-buy.sold-out.new-oos-style.not-loyalty-member.eligible-address.without-subscribe-buy-type.DISPLAY_0.only-one-delivery > div.prod-price-container")
            el_stock = el_stock[0].get_attribute('outerHTML')
            if '일시품절' in el_stock:
                # sendChannelMsg(f'현재 coupang에 닌텐도 스위치 동물의 숲 에디션 재고가 없습니다.\n다시 확인하고 알려드릴게요!\n{url}')
                pass
            else:
                print('coupang 재고 있음')
                sendChannelMsg(f'지금 닌텐도 스위치 동물의 숲 에디션이 입고되었습니다.\n아래 링크로 접속하여 구매하세요.\n{url}')
        elif url is sofrano:
            el_stock = driver.find_elements_by_css_selector('#contents > div.xans-element-.xans-product.xans-product-detail > div.detailArea > div.infoArea > span.icon')
            el_stock = el_stock[0].get_attribute('outerHTML')
            if '일시품절' in el_stock:
                # sendChannelMsg(f'현재 소프라노몰에 닌텐도 스위치 동물의 숲 에디션 재고가 없습니다.\n다시 확인하고 알려드릴게요!\n{url}')
                pass
            else:
                print('sofrano 재고 있음')
                sendChannelMsg(f'지금 닌텐도 스위치 동물의 숲 에디션이 입고되었습니다.\n아래 링크로 접속하여 구매하세요.\n{url}')

    except:
        print('에러 발생')
        sendChannelMsg(f'에러가 발생했습니다.\n하지만 무언가 바뀌었다는건 재고가 들어왔다는 의미일수도 있어요.\n아래 url로 접속해보세요!\n{url}')

    finally:
        driver.quit()


def crawler():
    show_time()
    for site in siteList:
        print(site, 'crawling-')
        stock_crawler(site)


def show_time():
    get_time = time.ctime()
    print(f'{get_time[8:10]}일 {get_time[11:19]} 현재 크롤링 진행중')

