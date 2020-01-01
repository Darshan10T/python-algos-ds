openBrackets = ["[","{","("]
closeBrackets = ["]","}",")"]

# Function to check parentheses 
def isValid(x) -> bool:
	stack = [] 
	for i in x:
		if i in openBrackets:
			stack.append(i) 
		elif i in closeBrackets:
			pos = closeBrackets.index(i)
			if ((len(stack) > 0) and
				(openBrackets[pos] == stack[len(stack)-1])):
				stack.pop()
	print(len(stack) == 0)

# Driver code
isValid('{[]{()}}')

isValid('[{}{})(]')
