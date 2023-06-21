#!/usr/bin/python3

def main():
	n=6
	for i in range(n):
		for j in range(0,i+1):
			print("*",end="")
		print("\n")

if __name__=='__main__':
	main()
