import random
tebak = 0
bil = random.randint(1,30)
def TebakAngka():
	try:
		global tebak
		print("hayo coba tebak angka berapa: ", end="")
		tebak = int(input())
		if tebak > bil:
			print("tebakan anda terlalu tinggi")
		elif tebak < bil :
			print("tebakan anda masih lebih rendah")
		else:
			print("selamat kamu benarrr..")
	except ValueError:
		print("Maaf seharusnya bilangan bulat, Invalid input nih!")
while True:
	TebakAngka()
	if tebak == bil:
		break
