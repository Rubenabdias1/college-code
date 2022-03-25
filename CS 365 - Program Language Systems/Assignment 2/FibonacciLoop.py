import time #For calculating the execution time of the program

# Ruben Nunez
# CS 365
# Assignment 2
# Fib with a loop

def fibonacci(n):

	fibonacciSeries = [0, 1]
	#First two base conditions
	if n==1:
		return 1
	elif n==2:
		return 1
	
	for i in range(2, n):
		#next elment in series = sum of its previous two numbers
		nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
		fibonacciSeries.append(nextElement)	

	return fibonacciSeries[n-1]


if __name__ == '__main__':
	
	n = int(input("Please enter the number of Fibonacci numbers to generate: "))

	startTime = time.time() #Get start time
	for x in range(1,n+1): #Generate 'n' Fibonacci number
		number = fibonacci(x) #Get x-th Fibonacci number
		print("%s : \t %s " % (x,number))
    
	endTime = time.time() #Get end time

	print("Execution Time: %s" % (endTime-startTime)) #Print execution time