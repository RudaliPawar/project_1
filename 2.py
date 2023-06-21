#!/usr/bin/python3

def main():
	n=5
	for i in range(n):
		for j in range(0,i+1):
			print("*",end="")
		print()

if __name__=='__main__':
	main()
