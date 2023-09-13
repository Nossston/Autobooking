# this file will include with a class instance methods.
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

class BookingFiltration:
    def __init__(self,driver:WebDriver ):
        self.driver = driver
    
    def apply_star_rating(self,*star_values):        
        try:            
            star_filtration_box =  self.driver.find_element(By.XPATH,'//*[@data-filters-group="class"]')    
        except:
            print("Failed to find the star box, under booking_filtration")
                    
        star_child_elements = star_filtration_box.find_elements(By.CSS_SELECTOR,'*')
        try:
            for star_value in star_values:
                for star_element in star_child_elements:
                    if str(star_element.get_attribute('innerHTML')).strip() == f'{star_value} stars':
                        star_element.click()
                        time.sleep(.5) # buffer time to reload
        except:
            print("Failed to apply star rating")
        print("Succeed to click stars")
        
    def sort_price_lowest_first(self):
        time.sleep(1)
        try:
            list_option = self.driver.find_element(By.XPATH,'//*[@data-testid="sorters-dropdown-trigger"]')
            list_option.click()
            time.sleep(1)
            element = list_option.find_element(By.XPATH,'//*[@data-id="price"]')
            element.click()
        except:
            print("Failed to sort price from lowest")
        print("Succeed to sort price from lowest")

        