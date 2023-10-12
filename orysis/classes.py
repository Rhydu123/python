class cal():
	def __init__(var,a,b):
		var.a=a
		var.b=b
	def add(var):
		c=a+b
		print("Sum :",c)
	def sub(var):
		c=a-b
		print("Difference :",c)
	def mul(var):
		c=a*b
		print("Product :",c)
	def div(var):
		c=a/b
		print("Quotient:",c)
	def mod(var):
		c=a%b
		print("Modulus:",c)
	



a=int(input("Enter number 1:"))
b=int(input("Enter number 2:"))
obj=cal(a,b)
while True:
	ch=input("Enter your option:1 - add,2 - sub,3 - mul,4 -div,5-mod,0-exit:")
	if ch=='1':
		obj.add()
	elif ch=='2':
		obj.sub()
	elif ch=='3':
		obj.mul()
	elif ch=='4':
		obj.div()
	elif ch=='5':
		obj.mod()
	elif ch=='0':
		print("Exiting...")
		break;
	else:
		print("Invalid option!!!")
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
