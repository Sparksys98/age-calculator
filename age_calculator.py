from datetime import datetime,date
def check_birthdate(year, month, day):
    birth_date = datetime(year, month, day)
    date_now = datetime.now()
    current_date=datetime(date_now.year, date_now.month, date_now.day)
    if(birth_date<current_date):
        return True
    else:
        return False
def calculate_age(year, month, day):
    birth_date = datetime(year,month,day)
    date_now = datetime.now()
    current_date=datetime(date_now.year, date_now.month, date_now.day)
    age = current_date - birth_date
    print("age is: ", age/365)


def main():
    year=int(input("Enter Year: "))
    month=int(input("Enter Month: "))
    day=int(input("Enter Day: "))
    check_birthdate(year,month,day)
    if(check_birthdate(year,month,day)==True):
        calculate_age(year,month,day)
    else:
        print("invalid")

if __name__ == '__main__':
    main()
