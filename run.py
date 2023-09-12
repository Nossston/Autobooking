from booking.booking  import Booking

with Booking() as bot:
    # needs to apply error handle
    
    bot.land_first_page()
    # bot.change_currency(currency_code="USD")
    bot.search_place_to_go(place_to_go="New York")
    # bot.search_place_to_go(input("Where do you want to go? :"))
    # bot.select_dates(check_in_date= input("What is your check in date? format is like 2023-09-01 :"),
                    #  check_out_date=input("What is your check out date? format is like 2023-09-05:"))
    # bot.select_dates(check_in_date="2023-01-01",check_out_date="2024-03-05")
    bot.select_adults(int(input("How many people? :")))
    bot.click_search()
    
    # bot.land_result_page()
    # bot.refresh()
    bot.apply_filtrations()
    bot.report_results()
    
