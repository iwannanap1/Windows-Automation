from qrlib.QRComponent import QRComponent
from RPA.Browser.Selenium import Selenium
from RPA.Windows import Windows
from RPA.Desktop import Desktop
import json
import time


xpaths = {
    "title_xpath": '//h2[@id="Historic_evolution"]',
    "para1_xpath": '//div[contains(@class, "mw-content-ltr")]/p[4]',
    "para2_xpath": '//div[contains(@class, "mw-content-ltr")]/p[5]',
    "para3_xpath": '//div[contains(@class, "mw-content-ltr")]/p[6]',
    "title2_xpath": '//h3[@id="RPA_actual_use"]',
    "list_xpath": '//*[@id="mw-content-text"]/div[1]/ul[1]/li',
}


class WesbsiteComponent(QRComponent):
    def __init__(self):
        super().__init__()
        self.browser = Selenium()
        self.windows = Windows()
        self.desktop = Desktop()
        self.data = {}

    def open_website(self):
        url = "https://en.wikipedia.org/wiki/Robotic_process_automation"
        try:
            self.browser.open_available_browser(url=url, headless=False)
        except Exception as e:
            raise e

    def get_data(self):
        try:
            # title_element = self.browser.find_element(title_xpath)
            title_element = self.browser.find_element(xpaths["title_xpath"])
            title = title_element.text.strip()

            para1_element = self.browser.find_element(xpaths["para1_xpath"])
            para1 = para1_element.text.strip()

            para2_element = self.browser.find_element(xpaths["para2_xpath"])
            para2 = para2_element.text.strip()

            para3_element = self.browser.find_element(xpaths["para3_xpath"])
            para3 = para3_element.text.strip()

            title2_element = self.browser.find_element(xpaths["title2_xpath"])
            title2 = title2_element.text.strip()

            list_element = self.browser.find_elements(xpaths["list_xpath"])
            list_items = [item.text.strip() for item in list_element]
            self.data = {
                "title": title,
                "para1": para1,
                "para2": para2,
                "para3": para3,
                "title2": title2,
                "list_items": list_items,
            }
            return self.data

        except Exception as e:
            self.logger.error("Could't find data")
            raise e

    # def save_data(self, filename="output.json"):
    #     try:
    #         data = self.get_data()
    #         with open(filename, "w", encoding="utf-8") as file:
    #             json.dump(data, file, ensure_ascii=False, indent=4)
    #         self.logger.info("Data saved successfully")
    #     except Exception as e:
    #         self.logger.error("failed to save data")
    #         raise e

    def open_word(self):
        self.windows.windows_run("winword")
        self.windows.control_window("name:Name Word")

    def open_blank_doc(self):
        self.windows.click("name:Name Blank document")
        time.sleep(2)

    def write_to_word(self,title,para1,para2,para3,title2,list_items):
        self.windows.control_window("name:Name Document1 - Word")
        self.desktop.click("header_locator")

        self.windows.send_keys(keys=title)
        self.windows.send_keys(keys="{Enter}")

        self.windows.send_keys(keys=para1)
        self.windows.send_keys(keys="{Enter}")
        self.windows.send_keys(keys=para2)
        self.windows.send_keys(keys="{Enter}")
        self.windows.send_keys(keys=para3)
        self.windows.send_keys(keys="{Enter}")

        self.desktop.click("header_locator")
        self.windows.send_keys(keys=title2)
        self.windows.send_keys(keys="{Enter}")

        self.desktop.click("bullet_locator")
        for index, items in enumerate(list_items):
            self.windows.send_keys(keys=items)
            if index < len(list_items) - 1:  # Only send Enter if NOT the last item
                self.windows.send_keys(keys="{Enter}")

    def format_doc(self):
        self.windows.send_keys(keys="{Ctrl}a")
        self.desktop.click("justify_locator")
        self.desktop.click("font_locator")
        self.windows.send_keys(keys="Times New Roman")
        self.windows.send_keys(keys="{Enter}")
    
    def save_doc(self):
        self.windows.click("name:Name Save")
        self.windows.send_keys(keys="RPA Windows automation")
        self.windows.click("name:Name Save")

    
    def close_word(self):
        self.windows.close_current_window()
