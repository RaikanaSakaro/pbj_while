#Get variables from user
bread = int(raw_input('How many slices of bread do you have? '))
pb = int(raw_input ('How many tablespoons of peanut butter do you have? '))
jelly = int(raw_input ('How many tablespoons of jelly do you have? '))

#Initialize variable for number of sandwiches
sandwiches = 0

#Create while loop for sandwiches
while bread/2 >= 1 and pb >= 1 and jelly >= 1:
	sandwiches = sandwiches + 1
	print "I have enough bread for {0} sandwiches, enough peanut butter for {1} sandwiches, and enough jelly for {2} sandwiches.".format(bread/2, pb, jelly)
	print "I'm making sandwich #{0}".format(sandwiches)
	bread = bread - 2
	pb = pb - 1
	jelly = jelly - 1
if bread < 2:
	print "I've run out of bread!"
if pb < 1:
	print "I've run out of peanut butter!"
if jelly < 1:
	print "I've run out of jelly!"
