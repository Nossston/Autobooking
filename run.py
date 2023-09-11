from booking.booking  import Booking

with Booking() as bot:
    # needs to apply error handle
    
    bot.land_first_page()
    bot.change_currency(currency_code="USD")
    bot.search_place_to_go(input("Where do you want to go? :"))
    bot.select_dates(check_in_date= input("What is your check in date? :"),
                     check_out_date=input("What is your check out date? :"))
    bot.select_adults(int(input("How many people? :")))
    bot.click_search()
    
    # bot.land_result_page()
    # bot.refresh()
    bot.apply_filtrations()
    bot.report_results()
    
