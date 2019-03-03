from selenium import webdriver
from framework.logger import Logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#封装driver的所有方法
logger=Logger(logger="BasePage").getLog()
class BasePage():
    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()
        logger.info("成功返回")

    def getTitle(self):
        return self.driver.title()
        logger.info("成功找到")

    def text(self,el):
        try:
            return el.text
            logger.info("找到文本",el.text)
        except Exception as e:
            logger.error("未找到文本",e)

    def getText(self,*loc):
        el=self.find_element(*loc)
        try:
            # print(el.text)
            return el.text
            logger.info("文本内容为:"+el.text)
        except Exception as e:
            logger.error("未找到文本",e)

    def open_url(self,url):
        self.driver.get(url)
        logger.info("URL为:%s" % url)

    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("已单击")
        except Exception as e:
            logger.error("单击未成功：%s " % e)

    def close(self):
        self.driver.close()
        logger.info("成功关闭当前窗口")

    def sendkeys(self,text,*loc):
        e1=self.find_element(*loc)
        # e1.clear()
        try:
            e1.send_keys(text)
            logger.info("输入内容为："+text)
        except Exception as e:
            logger.error("未输入内容：%s" % e)


    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
            logger.info("找到页面元素：%s--->"+loc)
        except Exception as e:
            logger.error("未找到%s" % e)

    def find_elements(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_elements(*loc)
            logger.info("找到一组页面元素：%s"+loc)
        except Exception as e:
            logger.error("未找到：%s" % e)

    def stopMouse(self,*loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return ActionChains(self.driver).move_to_element(loc).perform()
            logger.info("找到页面元素：%s--->" + loc)
        except Exception as e:
            logger.error("未找到頁面元素",e)

    def window_handle(self,i):
        self.driver.switch_to.window(self.driver.window_handles[i])
        try:
            logger.info("成功")
        except Exception as e:
            logger.error("失败")
    def clear(self,*loc):
        e1=self.find_element(*loc)
        try:
            e1.clear()
            logger.info("输入前清除内容")
        except Exception as e:
            logger.error("未成功",e)

    def refresh(self):
        self.driver.refresh()
        logger.info("刷新成功")




