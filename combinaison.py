
"""
	Factionriel n s'ecrit
	n!
	exemple 
	4! = 1 * 2 * 3 * 4 = 24
"""
def factorille(nombre):
	i = 1
	answer = i 
	while i <= nombre:
		answer *= i 
		i += 1
	return answer

"""
	Nombre de combinaison 
	de p possible dans n
	n!/p!(n-p)!
	combinaison de 2 dans 4
	response C 4 ! / 2!(4-2)!
"""

def combinaison(p,n):
	response = factorille(n)//(factorille(p) * factorille(n-p))
	return response

def generate_account(number):
	"""
	str_pad(1,5) : 00001
	"""
	return f"{number:04}"

n = int(input("Entre un nombre : "))

print(generate_account(n))
