'''
Esteban Camarillo
ID number 1636095
Birthday HW
'''

c_month = input('Enter current month')
c_day = input('Enter current day')
c_year = input('Enter current year')

print('Month:', c_month)
print('Day:', c_day)
print('Year:', c_year)

b_month = input('Enter birth month')
b_day = input('Enter birth day')
b_year = input('Enter birth year')

print('Month:', b_month)
print('Day:', b_day)
print('Year:', b_year)



if (c_month == b_month) and (c_day == b_day ):
    print("Happy birthday!")

elif c_year >= b_year or c_month < b_month:
    age = int(c_year) - int(b_year)
    age = int(c_year) - int(b_year)-1

    print("You are" , age, "years old")
