#write a progeam to o convert the month name to a number of days
x=input("Enter the name of a month:")
if x=='January' or x=='Jan' or x=='jan' or x=='january' or x=='Mar' or x=='mar' or x=='March' or x=='march' or x=='May' or x=='may' or x=='Jul' or x=='jul' or x=='July' or x=='july' or x=='Aug' or x=='aug' or x=='August' or x=='august' or x=='Oct' or x=='oct' or x=='October' or x=='october' or x=='Dec' or x=='dec' or x=='december' or x=='December':
   print(f"{x} month has 31 days")
elif x=='Feb' or x=='feb' or x=='Febuary' or x=='febuary':
   print(f"{x} month has 28 days")
else:
    print(f"{x} month has 30 days")
