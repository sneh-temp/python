try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))

    if hours < 40:
        pay=hours*rate
    else:
        pay=(40*rate)+(hours-40)*1.5*rate

    print("Pay: ",pay)

except:
    print("Error! Please enter numeric input.")