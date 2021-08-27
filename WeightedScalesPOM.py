from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

@dataclass
class Browsers:
    Chrome = webdriver.Chrome
    Firefox = webdriver.Firefox
    Safari = webdriver.Safari
    Opera = webdriver.Opera

@dataclass
class Bowls:
    left = "left"
    right = "right"

@dataclass
class Elements:
    ResetButton = (By.XPATH, '//button[contains(text(), "Reset")]')
    WeighButton = (By.ID, "weigh")
    ComparisonResultValue = (By.CSS_SELECTOR, "div.result button#reset")
    GridElem = lambda side, pos: (By.ID, f"{side}_{pos}")
    WeighingsList = (By.CSS_SELECTOR, "div.game-info li")

class ScalesPOM():
    def __init__(self, url:str, driver=Browsers.Firefox):
        self.driver = driver
        self.driver.get(url)

    def enter_grid_value(self, side:Bowls=Bowls.left, pos:int=0, value:int=0):
        self.driver.find_element(*Elements.GridElem(side,pos)).clear()
        self.driver.find_element(*Elements.GridElem(side,pos)).send_keys(str(value))
        return

    def clear_bowl(self, side:Bowls=Bowls.left):
        for i in range(9):
            id = Elements.GridElem(side, i)
            self.driver.find_element(*id).clear()

    def press_reset_button(self):
        self.driver.find_element(*Elements.ResetButton).click()
        return

    def get_result_value(self):
        return self.driver.find_element(*Elements.ComparisonResultValue).text

    def enter_values_for_bowl(self, side:Bowls=Bowls.left, values=[0,1,2]):
        self.clear_bowl(side)
        for i in range(len(values)):
            self.enter_grid_value(side, pos=i, value=values[i])
        return

    def press_weigh_button(self):
        current_list_length = len(self.driver.find_elements(*Elements.WeighingsList))
        self.driver.find_element(*Elements.WeighButton).click()
        len_comparison = lambda driver: len(self.driver.find_elements(*Elements.WeighingsList)) > current_list_length
        WebDriverWait(self.driver, 10).until(len_comparison)
        return

    def select_coin(self, coin=0):
        self.driver.find_element_by_id(f"coin_{coin}").click()
        WebDriverWait(self.driver, 10).until(EC.alert_is_present())
        alert_text = self.driver.switch_to.alert.text.lower()
        self.driver.switch_to.alert.accept()
        return alert_text

    def show_what_was_weighed(self):
        return [list_item.text for list_item in self.driver.find_elements(*Elements.WeighingsList)]

