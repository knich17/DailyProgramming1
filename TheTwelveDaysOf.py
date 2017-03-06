gifts = ['Partridge in a Pear Tree',
'Turtle Doves',
'French Hens',
'Calling Birds',
'Golden Rings',
'Geese a Laying',
'Swans a Swimming',
'Maids a Milking',
'Ladies Dancing',
'Lords a Leaping',
'Pipers Piping',
'Drummers Drumming']

days = ['first', 
'second', 
'third', 
'fourth', 
'fifth', 
'sixth',
'seventh',
'eighth',
'ninth',
'tenth',
'eleventh',
'twelfth']

lyric = 'On the %s day of Christmas my true love sent to me:'

if __name__ == '__main__':
	for day in range(1, len(gifts)+1):					#day is the current day of christmas (starting at one, ending at 12)
		print lyric % (days[day-1])

		for i in range(day,1,-1):						#i is the day used in the inner loop, from the current day down till and not including the first day
			print str(i) + ' ' + gifts[i-1]	
		else:
			print ('and a ' if day != 1 else 'A ') + gifts[0] + '\n'		#once the inner loop is complete, print the first days gift with an and if it isn't the first day