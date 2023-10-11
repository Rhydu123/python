def calculator(ch):
	if ch=='1':
		a=int(input("Enter no.1:"))
		b=int(input("Enter no.2:"))
		c=a+b
		print("The sum is ",c);
	
	elif ch=='2':
		a=int(input("Enter no.1:"))
		b=int(input("Enter no.2:"))
		c=a-b
		print("The diff is ",c);
	
	elif ch=='3':
		a=int(input("Enter no.1:"))
		b=int(input("Enter no.2:")) 
		c=a*b
		print("The product is ",c);
	
	elif ch=='4':
		a=int(input("Enter no.1:"))
		b=int(input("Enter no.2:"))
		c=a/b
		print("The quotient is ",c);
	elif ch=='5':
		a=int(input("Enter no.1:"))
		b=int(input("Enter no.2:"))
		c=a**b
		print("The power is ",c);	
	elif ch=='6':
		a=int(input("Enter no.1:"))
		b=int(input("Enter no.2:"))
		c=a%b
		print("The mod is ",c);
	else:
		print("Invalid option")
f='1'
while(f=='1'):
	ch=input("Enter your option:1 for add,2 for sub,3 for mul,4 for div,5 for exponent,6 for mod:")
	calculator(ch)
	f=input("Press 0 to exit:")
		
	
	
	
	
	
	
	
	
	
	
	
