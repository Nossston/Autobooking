# this file will include with a class instance methods.
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

class BookingFiltration:
    def __init__(self,driver:WebDriver ):
        self.driver = driver
    
    def apply_start_rating(self,*star_values):        
        try:            
            star_filtration_box =  self.driver.find_element(By.XPATH,'//*[@data-filters-group="class"]')    
        except:
            star_filtration_box =  self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div[1]/div[3]/div[10]')
            print("failed to find the star box, under booking_filtration")
            
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR,'*')
        
        for star_value in star_values:
            for star_element in star_child_elements:
                if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                    star_element.click()
        print("Succeed to click stars")
        
    def sort_price_lowest_first(self):
        time.sleep(1)
        list_option = self.driver.find_element(By.XPATH,'//*[@data-testid="sorters-dropdown-trigger"]')
        list_option.click()
        time.sleep(1)
        element = list_option.find_element(By.XPATH,'//*[@data-id="price"]')
        element.click()
        time.sleep(1)   