import time #For calculating the execution time of the program

def fibonacci(n):
	#First two base conditions
	if n==1:
		return 1
	elif n==2:
		return 1
	#End of base conditions
	return fibonacci(n-1) + fibonacci(n-2) #Recursive call to fibonacci function


if __name__ == '__main__':
	
	n = int(input("Please enter the number of Fibonacci numbers to generate: "))

	startTime = time.time() #Get start time
	for x in range(1,n+1): #Generate 'n' Fibonacci number
		number = fibonacci(x) #Get x-th Fibonacci number
		print("%s : \t %s " % (x,number))
    
	endTime = time.time() #Get end time

	print("Execution Time: %s" % (endTime-startTime)) #Print execution time