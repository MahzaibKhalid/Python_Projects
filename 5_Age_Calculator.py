import datetime

def Age_Calculator(y,m,d):
    today= datetime.datetime.now().date()
    dob = datetime.date(y,m,d)
    age = int((today-dob).days/365.25)
    print(age)
    
    
Age_Calculator(2000,1,15)