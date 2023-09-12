from selenium import webdriver
from selenium.webdriver.common.by import By
import booking.constants as const
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
import time 
from prettytable import PrettyTable
from datetime import datetime


class Booking(webdriver.Chrome):
    def __int__(self):
        super(Booking,self).__init__()
        
    def __exit__(self, exc_type, exc_val,exc_tb):
        None
                
    def land_first_page(self):
        try:
            self.get(const.BASE_URL)
            self.maximize_window()
        except:
            print("fail to open landing page")
    
        try:
            close_but = self.find_element(By.XPATH,'//*[@aria-label="Dismiss sign-in info."]')
            close_but.click()
        except:
            print("fail to click close button")
    
        print("succeed to land booking.com")
        
    # for result page testing
    def land_result_page(self):
        self.get(const.RESULT_URL)
        self.maximize_window()
        print("waiting to close")
        time.sleep(1)
        close_but = self.find_element(By.XPATH,'//*[@aria-label="Dismiss sign in information."]')
        close_but.click()
         
    def change_currency(self):
        try:
            # button = self.find_element(By.XPATH,'//*[@id="b2indexPage"]/div[2]/div/header/nav[1]/div[2]/span[1]/button/span')
            button = self.find_element(By.XPATH,'//*[@data-testid="header-currency-picker-trigger"]')
            button.click()
            time.sleep(.5)
            select_currency = self.find_element(By.XPATH,'//*[@class="aaee4e7cd3 e7a57abb1e fb60b9836d"]')
            select_currency.click()
            print("change the currency to USD")
        except:
            print("Failed to change currency to USD")
        
    def search_place_to_go(self,place_to_go):
        try:
            search_field = self.find_element(By.XPATH,'//*[@id=":re:"]')
            search_field.clear()
            search_field.send_keys(place_to_go)
            time.sleep(.5)
            first_result = self.find_element(By.XPATH,'//*[@tabindex="-1"]')
            first_result.click()
        except:
            print("Failed to search place to go.") 
        
    def select_dates(self,check_in_date,check_out_date):
        # handle formating
        check_in_date = datetime.strptime(check_in_date,'%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out_date,'%Y-%m-%d').date()
        thisyear = datetime.now().year
        thismonth = datetime.now().month
        
        # check-in section
        try:
            check_in_advance = ((check_in_date.year - thisyear) * 12 + check_in_date.month - thismonth)
            print( f'months ahead:{check_in_advance}' )
            next_button = self.find_element(By.XPATH, '//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 f671049264 deab83296e f4552b6561 dc72a8413c f073249358"]')
            if check_in_advance > 1:
                for _ in range(int(check_in_advance)):
                    next_button.click()
        except Exception as e:
            print(f"error happens: {e}")
        check_in_element = self.find_element(By.CSS_SELECTOR,f'span[data-date="{check_in_date}"]')
        check_in_element.click()
        
        # check-out section
        time.sleep(.5)
        try:
            check_out_advance = ((check_out_date.year - check_in_date.year) * 12 + check_out_date.month - check_in_date.month)
            print( f'check out months ahead:{check_out_advance}' )
            next_button = self.find_element(By.XPATH, '//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 f671049264 deab83296e f4552b6561 dc72a8413c f073249358"]')
            if check_out_advance > 1:
                for _ in range(int(check_out_advance)):
                    next_button.click()
        except Exception as e:
            print(f"error happens: {e}")            
        check_out_element = self.find_element(By.CSS_SELECTOR,f'span[data-date="{check_out_date}"]')
        check_out_element.click()
        
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
        
        