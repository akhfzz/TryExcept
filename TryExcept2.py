listi = []
while True:
	try:
		In = int(input("masukan bilangan bulat: "))
		listi.append(In)
		Stj = str(input("masukkan lagi ga?y/n:"))
		if Stj == "n":
			average = sum(listi)/len(listi)
			print(average)
			break
	except ValueError:
		print("bukan bilangan bulatt")
