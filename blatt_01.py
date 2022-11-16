# Simon Gerten, 1658115
# Jan   Lorenz, 1857469

import matplotlib.pyplot as plt
import numpy as np

import numpy as np

def aufgabe_1():
	# a)
	A = np.array([[1, 0],
		      [2, 3],
		      [0, 1]])
	B = np.array([[1, 1, 1],
		      [2, 2, 2]])
	print("A*B=")
	print(A.dot(B))
	print()
	print("B*A=")
	print(B.dot(A))
	print()
	print("A*A^T=")
	print(A.dot(A.transpose()))
	print()
	print("(komponentenweise) A*A=")
	print(np.multiply(A, A))
	print()

	# b)
	C = np.array([[2, -1, -1],
		      [0, 2, -1],
		      [0, -1, 1]])
	print("C^-1=")
	print(np.linalg.inv(C))

def aufgabe_2():
	n = int(input("Bitte geben Sie die Anzahl an gewünschten Fibonacci-Zahlen an: "))
	fibonacci = [1, 1]
	i = 0
	while i < n - 2:
	    fibonacci.append(fibonacci[i] + fibonacci[i + 1])
	    i += 1
	print("f_b= " + str(fibonacci))

def aufgabe_3():

    x1 = np.linspace(0, 10,  10) # Abstand: 1
    x2 = np.linspace(0, 10, 100) # Abstand: 0.1

    # Berechne Funktionswerte
    y1 = np.cos(x1)
    y2 = np.cos(x2)

    # Erstelle Plot mit zwei Subplots
    fig, ax = plt.subplots(2)

    # Plotte die Daten (extra hübsch!)
    ax[0].plot(x1, y1, color='red', linestyle=':')
    ax[1].plot(x2, y2, color='green', linestyle='--')

    # Let's go
    plt.show()


def aufgabe_4():
    # die Funktion
    def f(x):
        if x < -1:
            return 1
        if x > 1:
            return (x-1)**2 + 1
        return np.cos(2*np.pi*x)

    # die Werte
    x = np.linspace(-2, 2, 100)
    y = [f(z) for z in x]

    # die Tabelle
    print("X                 \t F(X)")
    for i in range(100):
        print (f"{str(x[i]).ljust(16)} \t {y[i]}")

    # der Plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


aufgabe_1()
aufgabe_2()
aufgabe_3()
aufgabe_4()
