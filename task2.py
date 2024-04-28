from collections import deque
       
def is_palindrome(string):
	q = deque()
	for character in string.lower().replace(" ", ""):
		q.append(character)
	match = True
	while(len(q) > 1 and match):
		front = q.pop()
		rear = q.popleft()
		if front != rear :
			match = False
	return match
    

print(is_palindrome('Radar'))
print(is_palindrome('abcd'))
print(is_palindrome('Raddar'))
print(is_palindrome('R a d d A r'))
