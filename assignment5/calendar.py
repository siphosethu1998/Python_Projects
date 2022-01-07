import calutils

def to_string(n, e):
        if n<1 or n>e:
                return '  '
        else:
                return '{:>2}'.format(n)
        
def row(i, s, e):
        start = i*7+s
        result=to_string(start, e)
        for column in range(start+1, start+7):
                result+=' '+to_string(column, e)  
        return result

def row_of_months(i, start_month, year):
        
        start_day=(calutils.first_day_of_month(start_month, year)-1)%7
        days=calutils.days_in_month(start_month, year)
        
        result=row(i, 1-start_day, days)

        for month in range(start_month+1, start_month+3):
                result+='   '
                start_day=(start_day+days)%7
                days=calutils.days_in_month(month, year)
                result+=row(i, 1-start_day, days)

        return result

def print_year(year):
        print('{0:^69}'.format(year))
        
def print_month_names(start_month):
        print('{0:^20}   {1:^20}   {2:^20}'.format(calutils.month_name(start_month), calutils.month_name(start_month+1), calutils.month_name(start_month+2)).title())

def print_month_days():
        week='Mo Tu We Th Fr Sa Su'
        print('{0:^20}   {1:^20}   {2:^20}'.format(week, week, week))
        
def print_months(start_month, year):
        print_month_names(start_month)
        print()
        print_month_days()
        
        for r in range(0, 6):
                print(row_of_months(r, start_month, year))
                
def main():
        year=int(input('Enter the year:\n'))
        
        print_year(year)
        print()
        print_months(1, year)
        for month in range(4, 13, 3):
                print()
                print_months(month, year)
                

if __name__ == "__main__":
        main()
