def factorial(n):
    if n == 0 or n == 1 :
        return 1
    resultado = n * factorial(n-1)
    return resultado


print(factorial(0))
print(factorial(5))
print(factorial(10))


def dfs_permutaciones(lista):
	resultado = []
	dfs([], lista, resultado )
	return resultado


def dfs(actual,restantes,resultado):
	if len(restantes)==0:
		resultado.append(actual)
		return

	for i in range(0,len(restantes)):
		siguiente = restantes[i]
		resto = restantes[:i] + restantes[i+1:]

		dfs(actual + [siguiente],resto,resultado)


perms = dfs_permutaciones([1,2,3])
print(perms)
print(len(perms))


def dfs_combinaciones(lista, r):
    resultado = []
    armar_combinaciones([], 0, lista, r, resultado)
    return resultado



def armar_combinaciones(actual, inicio, lista, r, resultado):
    if len(actual) == r:
        resultado.append(actual)
        return

    for i in range(inicio, len(lista)) :
            armar_combinaciones(actual + [lista[i]], i+1, lista, r, resultado)


combs = dfs_combinaciones([1,2,3,4], 2)
print(combs)
print( len(combs) )
