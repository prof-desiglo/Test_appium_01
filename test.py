import unittest
from appium import webdriver
#from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
import time

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='emulator-5554',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)

appium_server_url = 'http://localhost:4723'
#appium_server_url = 'http://127.0.0.1:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, capabilities)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        #el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
        el = self.driver.find_element(by=By.XPATH, value='//*[@text="Battery"]')
        el.click()
        time.sleep(5)
        text = self.driver.current_activity
        print(text)
        #self.driver.refresh()
        el2 = self.driver.find_element(by=By.XPATH, value="//*[@resource-id='com.android.settings:id/usage_summary']")
        #el2 = self.driver.find_element(by=By.ID, value='usage_summary')
        text = el2.text
        print(text)
        pass

if __name__ == '__main__':
    unittest.main()
