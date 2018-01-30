
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from pymongo import MongoClient

from src.library.getElement import *
from src.library.getPath import *
from src.library.basicMethods import *


class CnodeJS(object):

    def __init__(self):
        pass

    # def timewait(self, driver):
    #     return WebDriverWait(driver, 10)

    @classmethod
    def register(cls, driver, url, username, password, re_password, email):
        driver.get(url)
        # wait = CnodeJS().timewait(driver)
        wait = BasicMethods().time_wait(driver)
        wait.until(MainPageElement.zhuce).click()
        wait.until(RegisterElement.username).send_keys(username)
        wait.until(RegisterElement.password).send_keys(password)
        wait.until(RegisterElement.repassword).send_keys(re_password)
        wait.until(RegisterElement.email).send_keys(email)
        wait.until(RegisterElement.register_button).click()
        return wait.until(RegisterElement.checkpoint).text

    @classmethod
    def active(cls, username):
        client = MongoClient('mongodb://118.31.19.120:27017/')
        db = client.get_database('node_club_dev')
        users = db.get_collection('users')
        users.find_one_and_update({"loginname": username},{"$set": {"active": True}})
        return users.find_one({"loginname": username})['active']

    @classmethod
    def login(cls, driver, url, username, password):
        driver.get(url)
        # wait = CnodeJS().timewait(driver)
        wait = BasicMethods().time_wait(driver)
        wait.until(MainPageElement.denglu).click()
        wait.until(LoginElement.username).send_keys(username)
        wait.until(LoginElement.password).send_keys(password)
        wait.until(LoginElement.login_button).click()
        return wait.until(LoginElement.checkpoint).text

    @classmethod
    def choose_tab(cls, driver, tab):
        # wait = CnodeJS().timewait(driver)
        wait = BasicMethods().time_wait(driver)
        if tab == 'share' or tab == '分享':
            wait.until(IssueElement.share).click()
        elif tab == 'ask' or tab == '问答':
            wait.until(IssueElement.ask).click()
        elif tab == 'job' or tab == '招聘':
            wait.until(IssueElement.job).click()

    @classmethod
    def create_a_topic(cls, driver, url, tab, title, content):
        driver.get(url)
        # wait = CnodeJS().timewait(driver)
        wait = BasicMethods().time_wait(driver)
        wait.until(MainPageElement.fabuhuati).click()
        wait.until(IssueElement.xuanzhebankuai).click()
        CnodeJS().choose_tab(driver, tab)
        wait.until(IssueElement.title).send_keys(title)
        contents = wait.until(IssueElement.zhengwen)
        to_element = CnodeJS().find_element(contents)
        to_element.click()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('b').key_up(Keys.CONTROL).perform()
        ActionChains(driver).key_down(Keys.CONTROL).send_keys('i').key_up(Keys.CONTROL).perform()
        ActionChains(driver).move_to_element(to_element).send_keys(content).perform()

    @classmethod
    def upload_image(cls, driver):
        wait = BasicMethods().time_wait(driver)
        wait.until(IssueElement.shangchuan).click()
        wait.until(IssueElement.shangchuantupian).send_keys(getUploadPath('1.jpeg'))
        return wait.until(IssueElement.checkpoint_tupian).text

    @classmethod
    def click_submit(cls, driver):
        wait = BasicMethods().time_wait(driver)
        time.sleep(3)
        submits = wait.until(IssueElement.tijiao)
        submit_button = CnodeJS().find_element(submits)
        submit_button.click()
        return wait.until(IssueElement.checkpoint_tijiao).text

    @classmethod
    def personal_center(cls, driver, url):
        driver.get(url)
        wait = BasicMethods().time_wait(driver)
        wait.until(MainPageElement.my_mainpage).click()
        return wait.until(PersonalElement.first_topic).text

    @classmethod
    def delete_a_topic(cls, driver):
        wait = BasicMethods().time_wait(driver)
        wait.until(PersonalElement.first_topic).click()
        wait.until(PersonalElement.delete_topic).click()
        Alert(driver).accept()

    @classmethod
    def find_topic(cls, driver, url):
        driver.get(url)
        wait = BasicMethods().time_wait(driver)
        time.sleep(2)
        all_topic = wait.until(MainPageElement.all_topic)
        for topic in all_topic:
            if topic.text == r'人生苦短，我用Python':
                topic.click()
                break

    @classmethod
    def reply_topic(cls, driver, re_content):
        wait = BasicMethods().time_wait(driver)
        BasicMethods().scroll_down(driver)
        time.sleep(3)
        contents = wait.until(IssueElement.zhengwen)
        content = CnodeJS().find_element(contents)
        content.click()
        ActionChains(driver).move_to_element(content).send_keys(re_content).perform()
        CnodeJS().click_submit(driver)

    @classmethod
    def find_element(cls, elements):
        x = []
        for i in elements:
            x.append(i)
        return x[-1]




