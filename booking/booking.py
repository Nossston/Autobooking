from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.booking_filtration import BookingFiltration
from booking.booking_report import BookingReport
from prettytable import PrettyTable
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
import booking.constants as const
import time 

class Booking(webdriver.Chrome):

    def __int__(self,teardown=False):
        super(Booking,self).__init__()
        
    def __exit__(self, exc_type, exc_val,exc_tb):
        None
                
    def land_first_page(self):
        try:
            self.get(const.BASE_URL)
            self.maximize_window()
            # WebDriverWait(self,3).until(
            self.find_element(By.XPATH,'//*[@aria-label="Dismiss sign-in info."]').click()
            # )
        except:
            print("Error happens when landing booking.com")
        print("Succeed to land booking.com")

    def land_result_page(self):
        try:
            self.get(const.RESULT_URL)
            self.maximize_window()
            time.sleep(1)
            self.find_element(By.XPATH,'//*[@aria-label="Dismiss sign in information."]').click()
        except:
            print("Failed to land booking.com")     
        print("Succeed to land booking.com")
         
    def change_currency(self):
        time.sleep(1)
        try:
            self.find_element(By.XPATH,'//*[@data-testid="header-currency-picker-trigger"]').click()
            time.sleep(.5)
            self.find_element(By.XPATH,'//*[@class="a83ed08757 aee4999c52 ffc914f84a c39dd9701b ac7953442b"]').click()
            print("Succeed to change currency to USD")
        except:
            print("Error happens when changing currency to USD")
        time.sleep(.5)
        
    def search_place_to_go(self,place_to_go):
        search_field = self.find_element(By.XPATH,'//*[@id=":re:"]')
        search_field.clear()
        search_field.send_keys(place_to_go)
        time.sleep(.8)
        first_result = self.find_element(By.CSS_SELECTOR,'#indexsearch > div.hero-banner-searchbox > div > form > div.ffb9c3d6a3.db27349d3a.cc9bf48a25 > div:nth-child(1) > div > div > div.a7631de79e > div > ul > li:nth-child(1) > div')
        first_result.click() 
        
    def select_dates(self,check_in_date,check_out_date):
        # handle formating
        check_in_date = datetime.strptime(check_in_date,'%Y-%m-%d').date()
        check_out_date = datetime.strptime(check_out_date,'%Y-%m-%d').date()
        thisyear = datetime.now().year
        thismonth = datetime.now().month
        
        # check-in section
        try:
            check_in_advance = ((check_in_date.year - thisyear) * 12 + check_in_date.month - thismonth)
            # print( f'months ahead:{check_in_advance}' )
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
            # print( f'check out months ahead:{check_out_advance}' )
            next_button = self.find_element(By.XPATH, '//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 f671049264 deab83296e f4552b6561 dc72a8413c f073249358"]')
            if check_out_advance > 1:
                for _ in range(int(check_out_advance)):
                    next_button.click()
        except Exception as e:
            print(f"error happens: {e}")            
        check_out_element = self.find_element(By.CSS_SELECTOR,f'span[data-date="{check_out_date}"]')
        check_out_element.click()
        
    def select_adults(self,count):
        selection_element = self.find_element(By.XPATH, '//*[@data-testid="occupancy-config"]')
        selection_element.click()
        default_adutl = int( self.find_element(By.XPATH,'.//*[@class="d723d73d5f"]').get_attribute('innerHTML').strip())
        
        if count < default_adutl:
            decrease_adult = self.find_element(By.XPATH,'//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 e91c91fa93"]')
            for _ in range(default_adutl - count):
                decrease_adult.click()
        else:
            increase_adult = self.find_element(By.XPATH,'//*[@class="a83ed08757 c21c56c305 f38b6daa18 d691166b09 ab98298258 deab83296e bb803d8689 f4d78af12a"]')
            for _ in range(count - default_adutl):
                increase_adult.click()
        print("succeed to select adults")
        time.sleep(2)
        
    def click_search(self):
        self.find_element(By.CSS_SELECTOR,'button[type=submit]').click()
        time.sleep(2)
        
    def apply_filtrations(self):
        filtration = BookingFiltration(driver=self)
        filtration.apply_star_rating(3,4,5)
        filtration.sort_price_lowest_first()
        
    def report_results(self):
        hotel_boxes = self.find_element(By.CLASS_NAME,'d4924c9e74')
        report = BookingReport(hotel_boxes)
        
        table = PrettyTable(
            field_names=["Hotel Name", "Hotel Price", "Hotel Score"]
        )
        table.add_rows(report.pull_deal_box_attributes())
        print(table)
        
        