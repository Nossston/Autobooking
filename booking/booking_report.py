# This file is going to include methods that will parse 
# the specific data that we need from each one of the deal boxes
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time

class BookingReport:
    def __init__(self,boxes_section_element:WebDriver) -> None:
        self.boxes_section_element = boxes_section_element
        self.deal_boxes = self.pull_deal_boxes()
    
    def pull_deal_boxes(self):
        return self.boxes_section_element.find_elements(By.CLASS_NAME,'b978843432')
        # return self.boxes_section_element.find_elements(By.XPATH,'//*[@data-testid="property-card"]')
        
        
    def pull_deal_box_attributes(self):
        collection = []
        
        for deal_box in self.deal_boxes:
            try:
                # Pull name
                hotel_name = deal_box.find_element(By.XPATH,'.//*[@data-testid="title"]').get_attribute('innerHTML').strip()
                # Pull price
                hotel_price = deal_box.find_element(By.XPATH,'.//*[@data-testid="price-and-discounted-price"]').get_attribute('innerHTML').strip()
                # Pull score
                a = (deal_box.find_element(By.XPATH,'.//div[contains(@aria-label,"Scored")]'))
                hotel_score = a.text
                collection.append( [hotel_name,hotel_price,hotel_score])
            except:
                print("Error with finding hotel's info")
                time.sleep(2)
        
        return collection
        