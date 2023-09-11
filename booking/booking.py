from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
import time 
from prettytable import PrettyTable

class Booking(webdriver.Chrome):
    def __int__(self,teardown=False):
        super(Booking,self).__init__()
        
    def __exit__(self, exc_type, exc_val,exc_tb):
        None
                
    def land_first_page(self):
        self.get(const.BASE_URL)
        self.maximize_window()
        time.sleep(1.5)
        print("waiting to close")
        time.sleep(1)
        close_but = self.find_element(By.XPATH,'//*[@aria-label="Dismiss sign in information."]')
        close_but.click()
    
    # for result page testing
    def land_result_page(self):
        self.get(const.RESULT_URL)
        self.maximize_window()
        print("waiting to close")
        time.sleep(1)
        close_but = self.find_element(By.XPATH,'//*[@aria-label="Dismiss sign in information."]')
        close_but.click()
         
    def change_currency(self,currency_code):
        button = self.find_element(By.XPATH,'//*[@id="b2indexPage"]/div[2]/div/header/nav[1]/div[2]/span[1]/button/span')
        button.click()
        time.sleep(.8)
        #  USD is on the row12, col4th
        select_currency = self.find_element(By.CSS_SELECTOR,'#b2indexPage > div.b9720ed41e.cdf0a9297c > div > div > div > div > div.f7c2c6294c > div > div:nth-child(3) > div > div > ul:nth-child(12) > li:nth-child(4) > button')
        select_currency.click()
        # check text, a= sele.text.equals(USD)
        print("change")
        time.sleep(2)
        
    def search_place_to_go(self,place_to_go):
        search_field = self.find_element(By.XPATH,'//*[@id=":re:"]')
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(.8)
        first_result = self.find_element(By.CSS_SELECTOR,'#indexsearch > div.hero-banner-searchbox > div > form > div.ffb9c3d6a3.db27349d3a.cc9bf48a25 > div:nth-child(1) > div > div > div.a7631de79e > div > ul > li:nth-child(1) > div')
        first_result.click() 
    def select_dates(self,check_in_date,check_out_date):
        time.sleep(.5)
        check_in_element = self.find_element(By.CSS_SELECTOR,f'span[data-date="{check_in_date}"]')
        check_in_element.click()
        time.sleep(.8)
        check_out_element = self.find_element(By.CSS_SELECTOR,f'span[data-date="{check_out_date}"]')
        check_out_element.click()
        time.sleep(.8)
        
    def select_adults(self,count):
        selection_element = self.find_element(By.CSS_SELECTOR,'#indexsearch > div.hero-banner-searchbox > div > form > div.ffb9c3d6a3.db27349d3a.cc9bf48a25 > div:nth-child(3) > div > button')
        selection_element.click()
        time.sleep(.8)
        # 2 is magic, default number
        if count<2:
            while True:
                decrease_adult = self.find_element(By.CSS_SELECTOR,'#indexsearch > div.hero-banner-searchbox > div > form > div.ffb9c3d6a3.db27349d3a.cc9bf48a25 > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.bfb38641b0 > button.a83ed08757.c21c56c305.f38b6daa18.d691166b09.ab98298258.deab83296e.bb803d8689.e91c91fa93')
                decrease_adult.click()
                adults_value_element = self.find_element(By.ID,'group_adults')
                adults_value = adults_value_element.get_attribute('value')

                if int(adults_value) == count:
                    break
        else:
            increase_adult = self.find_element(By.CSS_SELECTOR,'#indexsearch > div.hero-banner-searchbox > div > form > div.ffb9c3d6a3.db27349d3a.cc9bf48a25 > div:nth-child(3) > div > div > div > div > div:nth-child(1) > div.bfb38641b0 > button.a83ed08757.c21c56c305.f38b6daa18.d691166b09.ab98298258.deab83296e.bb803d8689.f4d78af12a')
            for _ in range(count - 2):
                increase_adult.click()
        print("suc")
        time.sleep(2)
        
    def click_search(self):
        search_but = self.find_element(By.CSS_SELECTOR,'button[type=submit]')
        search_but.click()
        time.sleep(3)
        
    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_start_rating(3,4,5)
        filtration.sort_price_lowest_first()
        
    def report_results(self):
        hotel_boxes = self.find_element(By.CLASS_NAME,'d4924c9e74')
        report = BookingReport(hotel_boxes)
        
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
        
        