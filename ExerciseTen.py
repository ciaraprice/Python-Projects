import getpass
# supplied_pin = input("Enter your pin: ")
# pincode = "4444"
# # while pincode != supplied_pin:
# #     print ("fail")
# #     if input("ReEnter pin: ") == pincode:
# #         print ("Success")
# #         break #make sure you put the break after the print success


supplied_pin = ""
pincode = "4444"
attempts= 1
while (supplied_pin != pincode) and (attempts <= 3):
    supplied_pin = getpass.getpass(prompt='Enter your pin')  # give supplied pin the input variable !!

    stars= "" #create empty string of stars to minic characters typed in by user
    for character in range(len(supplied_pin)): #going from 0 to length of the supplied pin
        stars= stars + "*" #everytime loop runs, adding a star to the stars.
    print(stars)

    if supplied_pin == pincode:
        print ("Success")
    else:
        print ("fail")

    print ("Attempts: " + str(attempts))
    attempts = attempts + 1
    if attempts > 3:
        print("locked")
