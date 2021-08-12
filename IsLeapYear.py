# Python program to check leap year
# or not in a single line

def leapYear(year):

	# Return true if year is a multiple
	# of 4 and not multiple of 100.
	# OR year is multiple of 400.
	return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0));

# Driver Code
year = 2000
if(leapYear(year)):
	print("Leap Year")
else:
	print("Not a Leap Year")
	
# This code is contributed by geekforgeeks
