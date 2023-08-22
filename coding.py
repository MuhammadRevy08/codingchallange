import time
# Efek Loading mas bro biar kece hehe
def loading1(seconds):
    for i in range(seconds * 10):
        print("Menghitung BMI" + "." * (i % 4), end="\r", flush=True)
        time.sleep(0.1)
    print("Done", end="\r")

print()

def loading2(seconds):
    for i in range(seconds * 10):
        print("Loading" + "." * (i % 4), end="\r", flush=True)
        time.sleep(0.1)
    print("Done", end="\r")

print()

################

def Bmi():
	# Data Udin
	Bb_Udin = 78
	Tb_Udin = 1.69
	print(f"Berat Badan Udin : {Bb_Udin} Kg")
	print(f"Tinggi Badan Udin : {Tb_Udin} M\n")

	# Data Nanang
	Bb_Nanang = 92
	Tb_Nanang = 1.95
	print(f"Berat Badan Nanang : {Bb_Nanang} Kg")
	print(f"Tinggi Badan Nanang : {Tb_Nanang} M\n")

	loading1(5)

	# Menghitung BMI
	hasilUdin = Bb_Udin / (Tb_Udin ** 2)
	hasilNanang = Bb_Nanang / (Tb_Nanang ** 2)

	BmiUdin = hasilUdin
	BmiNanang = hasilNanang

	# Proses Pembulatan angka desimal
	data_Bmi_Udin = round(BmiUdin, 2)
	data_Bmi_Nanang = round(BmiNanang, 2)

	# Output
	print(f"BMI Udin adalah : {data_Bmi_Udin}")
	print(f"BMI Nanang adalah : {data_Bmi_Nanang}\n")


	# Loading
	loading2(3)

	# Proses Perbandingan
	if(data_Bmi_Udin > data_Bmi_Nanang):
		print("BMI udin lebih tinggi dari pada BMI Nanang")
	elif(data_Bmi_Udin < data_Bmi_Nanang):
		print("BMI Nanang lebih tinggi dari pada BMI Udin")
	else:
		print("BMI mereka tinggi nya sama rata !")

Bmi()
