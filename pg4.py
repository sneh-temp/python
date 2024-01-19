try:
    hrs = input("Enter Hours:")
    h = float(hrs)
    rate = input("Enter Rate:")
    r = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

def computepay(h,r):
    if h <= 40:
        pay = h*r
    else:
        pay = (40*r)+(h-40)*1.5*r
    return pay

print("Your Pay is: ",computepay(h,r))