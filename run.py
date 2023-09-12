from booking.booking  import Booking

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency()
    bot.search_place_to_go(input("Where do you want to go? :"))
    bot.select_dates(check_in_date= input("What is your check in date?(format:YYYY-mm-dd) :"),
                     check_out_date=input("What is your check out date?(format:YYYY-mm-dd) :"))
    bot.select_adults(int(input("How many people? :")))
    bot.click_search()
    
    # bot.land_result_page()
    # bot.refresh()
    bot.apply_filtrations()
    bot.report_results()
    
