
"""
-recieves input of a list of tuple(s) for both borrowed amount and payment amount and payment day.
-tuples in payment list are formatted as such (amount payed, day payed)
-tuples in borrowed list are formatted as such (amount borrowed, day borrowed)
-the input for scenario 2 in the problem would look as following:
	credit_line([(500,0),(100,25)],[(200,15)])
-the default apr is 35%. This can be adjusted.
-the default limit is $1000. This can be adjusted.
"""


def credit_line(borrow,pay=(0,0),apr=.35,limit=1000):
	c=1
	total=0
	g=0
	line=[]
	for i in borrow:
	    line.append(i)
	if pay != (0,0):
		for (a,b) in pay:
			a*=-1
			line.append((a,b))
	line.sort(key=lambda tup: tup[1])
	for i,(a,b) in enumerate(line):
	    if c < len(line):
	        c+=1
	        days=line[i+1][1]-b
	        g+=a
	        if g>limit:
	        	#exits code if it goes over the limit
	        	raise ValueError('Sorry you are over the credit limit')
	        t=g*apr/365*days
	        total+=t
        
	days_left=30-line[-1][1]
	total_pay=g+line[-1][0]
	if total_pay>limit:
		#exits code if it goes over the limit
		raise ValueError('Sorry you are over the credit limit')
	tt=(g+line[-1][0])*apr/365*days_left
	total+=tt
	ftotal=round(total,2)
	print 'Total owed interest is $%s. Total payment should be $%s.' %(ftotal, total_pay+ftotal)
