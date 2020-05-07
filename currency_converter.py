# ASK THE USER HOW MUCH ORIGINAL CURRENCY NEEDS TO BE CONVERTED, APPLY SPECIFIC CONVERSION RATE AND FINALLY TELL THE USER RESULT OF CONVERSION IN THE DESIRED CURRENCY.

def convert_currency(fro,to,rate):
    print("Welcome to currency convertor. Read carefully: Here, you need to pass the original currency as first argument, the desired currency as second argument and finally currency convertion rate as third argument.")
    user_value = input("How many {} needs to be converted? ".format(fro))
    amount = float(user_value)
    conversion = amount*rate
    print("{} {} is equal to {} {}".format(user_value,fro,conversion,to))
    return("Thank you. Please use me again. See ya!")


ALL_RATES = {
    ("rupee","dollar"): 0.013,
    ("dollar","rupee"): 75,
    ("euro","rupee"):81,
    ("rupee","euro"): 0.012
    # Add as many as desirable
}


print(convert_currency("dollar","rupees",81)) # 1 Dollar = 75 rupees
print(convert_currency("euro","rupees",81)) # 1 euro = 81 rupees
# Always make sure to always change the rate accordingly.