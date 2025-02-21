#!/usr/bin/python3.7

import random
import sys

# coefficients for MT19937
(w, n, m, r) = (32, 624, 397, 31)
a = 0x9908B0DF
(u, d) = (11, 0xFFFFFFFF)
(s, b) = (7, 0x9D2C5680)
(t, c) = (15, 0xEFC60000)
l = 18
f = 1812433253


# make a arry to store the state of the generator
MT = [0 for i in range(n)]
index = n+1
lower_mask = 0xFFFFFFFF #int(bin(1 << r), 2) - 0b1
upper_mask = 0x00000000 #int(str(-~lower_mask)[-w:])


# initialize the generator from a seed
def mt_seed(seed):
	# global index
	# index = n
	MT[0] = seed
	for i in range(1, n):
		temp = f * (MT[i-1] ^ (MT[i-1] >> (w-2))) + i
		MT[i] = temp & 0xffffffff


# Extract a tempered value based on MT[index]
# calling twist() every n numbers
def extract_number():
	global index
	if index >= n:
		twist()
		index = 0

	y = MT[index]
	y = y ^ ((y >> u) & d)
	y = y ^ ((y << t) & c)
	y = y ^ ((y << s) & b)
	y = y ^ (y >> l)

	index += 1
	return y & 0xffffffff


# Generate the next n values from the series x_i
def twist():
	for i in range(0, n):
		x = (MT[i] & upper_mask) + (MT[(i+1) % n] & lower_mask)
		xA = x >> 1
		if (x % 2) != 0:
			xA = xA ^ a
		MT[i] = MT[(i + m) % n] ^ xA


if __name__ == '__main__':
	flag = "CCC{tRu3_R4nd0mn3sS_1s_H4rd}"
	while(1):
		# print("Connected")
		mt_seed(random.randint(1,1000000))
		seed = (extract_number()%1000000)
		# print(seed)
		random.seed(seed)
		expected = random.randint(1,10000000)
		try:
			user_input = input("Insert a number : ")
			# print(user_input)
			sys.stdin.flush()
			# print(user_input)
			if(expected == int(user_input)):
				print("Correct")
				sys.stdout.flush()
				print("Here is the flag : " + flag)
				sys.stdout.flush()
				break
			else:
				print("Wrong, expected number was : " + str(expected))
				sys.stdout.flush()
		except ValueError:
			continue
		except KeyboardInterrupt:
			print ("")
			break