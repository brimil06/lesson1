print "What is the name of your server?",
name = raw_input()
print "What is the amount of your meal?: $",
meal = float(raw_input())
print "What is the tax rate?",
tax = (.01*float(raw_input()))*meal
print "What percentage do you want to tip?",
tip = (.01*int(raw_input()))*meal
total = meal+tax+tip
print "The tip amount is: $" + str(tip)
print "The total amount for my meal is: $" + str(total)
print "Thanks for your service " + name
