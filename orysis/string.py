st=input("Enter the string:")
vow=0
con=0
for i in st:
	if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U' ):
		vow+=1
	else:
		con+=1
print("The no. of vowels in the string:",vow)
print("The no. of consonents in the string:",con)
	
