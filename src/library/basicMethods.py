import time

from selenium.webdriver.support.wait import WebDriverWait
from src.library.getPath import getScreenShotsPath


class BasicMethods(object):

    @classmethod
    def image_filename(cls, driver):
        filename = time.strftime('%Y%m%d_%H%M%S') + '.png'
        driver.save_screenshot(getScreenShotsPath(filename))

    @classmethod
    def time_wait(cls, driver):
        return WebDriverWait(driver, 10)

    @classmethod
    def scroll_down(cls, driver):
        js_ = "var q=document.documentElement.scrollTop=10000"
        driver.execute_script(js_)
