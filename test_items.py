import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_product_have_add_button(browser):
    browser.get(link)

    # find and click button
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
    )
    # button = browser.find_element_by_css_selector(".btn.btn-lg.btn-primary.btn-add-to-basket")
    button.click()

    # find name of book
    book_name_element = browser.find_element_by_css_selector("h1")
    book_name = book_name_element.text

    # time.sleep(5)

    # find link to basket
    basket = browser.find_element_by_css_selector(".btn-group .btn.btn-default")
    basket_link = basket.get_attribute("href")

    # go to basket
    browser.get(basket_link)

    time.sleep(2)

    name_in_basket_element = browser.find_element_by_css_selector(".col-sm-4 a")
    name_in_basket = name_in_basket_element.text

    # print(name_in_basket)

    assert name_in_basket == book_name, "книга не была добавлена"
