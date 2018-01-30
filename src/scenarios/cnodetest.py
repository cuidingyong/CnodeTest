import unittest
import time

from src.scenarios.cnodejs import CnodeJS
from src.library.getData import get_csv_data
from src.library.basicMethods import BasicMethods

from selenium import webdriver


driver = webdriver.Chrome()
class CnodeTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        driver.maximize_window()

    def setUp(self):
        self.url, self.username, self.password, self.re_password, self.email, self.expect\
            = get_csv_data('cnode_data.csv')[0]
        self.tab, self.title, self.content, self.re_content = get_csv_data('topic_data.csv')[0]

    # def test_00register(self):
    #     assert_alert = CnodeJS().register(driver, self.url, self.username, self.password, self.re_password, self.email)
    #     self.assertIn(self.expect, assert_alert)

    # def test_01active(self):
    #     assert_active = CnodeJS().active(self.username)
    #     print(assert_active)
    #     self.assertEqual(True, assert_active)

    def test_02login(self):
        assert_login = CnodeJS().login(driver, self.url, self.username, self.password)
        self.assertEqual(self.username, assert_login)

    # 发布帖子
    def test_03_post_topic(self):
        # CnodeJS().login(driver, self.url, self.username, self.password)
        CnodeJS().create_a_topic(driver, self.url, self.tab, self.title, self.content)
        assert_image = CnodeJS().upload_image(driver)
        self.assertIn('g', assert_image)
        assert_issue = CnodeJS().click_submit(driver)
        self.assertEqual(self.title, assert_issue)

    # 删除帖子
    def test_06_deleteTopic(self):
        # CnodeJS().login(driver, self.url, self.username, self.password)
        assert_before = CnodeJS().personal_center(driver, self.url)
        CnodeJS().delete_a_topic(driver)
        assert_after = CnodeJS().personal_center(driver, self.url)
        self.assertNotEqual(assert_before, assert_after)

    def test_05_reply_topic(self):
        # CnodeJS().login(driver, self.url, self.username, self.password)
        CnodeJS().find_topic(driver, self.url)
        CnodeJS().reply_topic(driver, self.re_content)

    def tearDown(self):
        BasicMethods().image_filename(driver)
        time.sleep(1)

    @classmethod
    def tearDownClass(cls):
        # pass
        driver.quit()


# def main():
#     unittest.main()
#
# if __name__ == '__main__':
#     main()