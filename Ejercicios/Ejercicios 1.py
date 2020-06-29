def validacion_num():
    print("Ingrese un numero para validarlo")
    num_val = input()

    if int(num_val) > 0:
        f_num = "El numero: " + num_val + " es positivo"
    elif int(num_val) < 0:
        f_num = "El numero: " + num_val + " es negativo"
    elif int(num_val) == 0:
        f_num = "El numero: " + num_val + " es Cero"
    return f_num


def par_impar():
    print("Ingrese un numero para ver si es par o impar")
    num = input()

    if int(num) % 2:
        var = 'El numero: ' + num + ' es Impar'
    else:
        var = 'El numero: ' + num + ' es Par'

    return var

def primos():
    print("Ingrese un numero para ver si es primo")
    num = input()

    band = 0
    for i in range(1, int(num) + 1):
        if (int(num) % i) == 0:
            band = band + 1
    if band == 2:
        res = 'El numero: ' + num + ' es Primo'
    else:
        res = 'El numero: ' + num + ' no es Primo'
    return res

def bisiesto():
    print("Ingrese un anio para ver si es bisiesto")
    anio = input()

    if (int(anio) % 4 == 0) & (int(anio) % 100 != 0):
        res_anio = 'El anio: ' + anio + ' es visiesto'
    else:
        res_anio = 'El anio: ' + anio + ' no es visiesto'
    return res_anio

if __name__ == '__main__':

    print(validacion_num())
    print(par_impar())
    print(primos())
    print(bisiesto())

