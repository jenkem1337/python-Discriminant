import math
import cmath

while True:
	print("Hoşgeldiniz lütfen ax2+bx+c denklemide a b ve c yi giriniz")

	a = float(input("Lütfen a değerini giriniz : "))
	b = float(input("Lütfen b değerini giriniz : "))
	c = float(input("Lütfen c değerini giriniz : "))

	delta = b*b-4*a*c


	if delta > 0:
	    x1 = -b+math.sqrt(delta)/2*a
	    x2 = -b-math.sqrt(delta)/2*a
	    print("x1 değeri : ",x1)
	    print("x2 değeri : ",x2)
	elif delta == 0:
	    y = -b/2*a
	    print("Delta sıfır olduğundan kökler eşittir : ",y)

	elif delta < 0:
	    z = complex(delta)
	    print("Sıfırdan küçük olduğu için reel kök yoktur : ",z)    
	else:
	    print("yanlış bir şey tuşladınız")

