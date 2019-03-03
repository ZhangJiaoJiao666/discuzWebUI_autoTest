from testsuit.basecase import BaseTestCase
from pageobject.forumHomePage import ForumHomePage
import unittest

class Forum_Search(BaseTestCase):
    def test_userforum(self):
        homePage = ForumHomePage(self.driver)
        # homePage.open_url("http://127.0.0.1/forum.php?")
        homePage.login("rebecca","123456")

        homePage.defalt()
        homePage.send_forum("haotest","2019.02.02上午11：00整")
        homePage.reply_forum("2019年2月17日上午10点整！")
        self.driver.refresh()
        homePage.logout()


if __name__ == "__main__":
    unittest.main()









