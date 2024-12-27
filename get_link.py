
#TODO add type casting, comments, automatic year calc,

import requests

class Date:

    def __init__(self, month: str, day: str, year: str):
        self.month = month
        self.day = day
        self.year = year
    
    def test_valid_str_md(self,date):

        return_value = False    #return values
        return_info = ""

        if len(date) > 2:  #if string is to long

            return_value = False
            return_info = "String Entered is to long"
            return (return_value,return_info)
        
        try:                #test if input is a int

            int(date[0])
            int(date[1])

        except:

            return_value = False
            return_info = "Input is not a valid month number, mm instead of m"
            return (return_value,return_info)

        return(True, "VALID")

    def is_month_valid(self,date): #Function to check if month is valid indvidually

        
        return_value = False    #return values
        return_info = ""

        rval = self.test_valid_str_md(date)

        if rval[0] == False:
            return rval
        
        x = int(date[0])

        if  (0 > x > 1):       #test if input is a valid month

            return_value = False
            return_info = "Input is not a valid month"
            return (return_value,return_info)

        return_value = True
        return_info = "VALID"
        
        return (return_value,return_info)

    def is_year_valid(self,year):


        try:
            x = int(year)
        except:
            return (False,"Not a Number")
        
        current_year = 2025 #TODO Update to automatically get this...

        if (x < 1945 or x > current_year):
             return (False,"Not a valid year")
        
        return(True,"VALID")

    def is_leap_year(self, year: int) -> bool:
        """Check if the provided year is a leap year."""
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True
        return False

    def get_month_days(self, year: int) -> dict:
        """Return a dictionary with months (as strings) and their corresponding number of days for the given year."""
        month_days = {
            "01": 31,
            "02": 29 if self.is_leap_year(year) else 28,
            "03": 31,
            "04": 30,
            "05": 31,
            "06": 30,
            "07": 31,
            "08": 31,
            "09": 30,
            "10": 31,
            "11": 30,
            "12": 31
        }
        return month_days
    
    
    def is_day_valid(self,day, month, year):

        rval = self.test_valid_str_md(day)
        if rval[0] == False:
            return rval
        

        x = self.get_month_days(int(year))

        days = x[month]

        if int(day) > days or int(day) < 1:
            return(False,"Invalid amount of days")
        
        return(True,"VALID")


    def is_valid_date(self):

        rval = []

        rval.append(self.is_month_valid(self.month))
        
        if rval[0][0] == False:
            rval.append((False,"INVALID MONTH"))
            rval.append(self.is_year_valid(self.year))
            return rval
        
        year = self.is_year_valid(self.year)

        if year[0] == False:
            rval.append((False,"INVALID YEAR"))
            rval.append(year)
        else:
            rval.append(self.is_day_valid(self.day,self.month,self.year))
            rval.append(year)

        return rval

        

def get_link(date1, date2):
    ##Sample link https://www.nba.com/stats/players/traditional?DateFrom=&DateTo=&Season=2023-24&PerMode=Totals

    year1 = date1.year
    year2 = date2.year

    if year1 != year2:
        link_year = f"{year1}-{year2[2:]}"
    else:
        year2_end = str(int(year2[2:]) + 1)
        print(len(year2_end))
        if len(year2_end) == 1:
            year2_end = '0' + year2_end
        link_year = f"{year1}-{year2_end}"
    
    x = f"https://www.nba.com/stats/players/traditional?DateFrom=&DateTo=&Season={link_year}&PerMode=Totals"

    return x

def get_page(link):
    pass

def main():
    x = Date('05', '07', '2000')
    y = Date('05', '07', '2000')
    get_link(x,y)

if __name__ == '__main__':
    main()