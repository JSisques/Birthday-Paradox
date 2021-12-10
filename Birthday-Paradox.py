def main():

    #Numero de dias en un año
    DAYS_OF_YEAR = 365

    #Empezaremos a descontar numeros desde 365, 364, 363...
    currentDay = DAYS_OF_YEAR

    #Cantidad de gente en el grupo
    numberOfPeople = int(input("Introduce el número de personas del grupo: "))

    # Se busca sacar el porcentaje de personas que NO cumplen años el mismo dia
    # Luego esa probabilidad se la restaremos al 100% para sacar la probabilidad de que haya 2 personas que cumplan años el mismo dia
    # 100% - % de no cumplir años el mismo dia x personas

    # Si el numero de personas es menor que el numero de dias en un año
    if(numberOfPeople < DAYS_OF_YEAR):

        result = 1

        # Vamos calculando la probabilidad de la siguiente forma
        # 365/365 X (365 - 1)/365 X (365 - 2)/365 así hasta que el número que resta sea igual al número de personas en el grupo
        for i in range(0, numberOfPeople):
            # Calculamos la probabilidad
            result *= calculateProbability(currentDay, DAYS_OF_YEAR)

            currentDay -= 1

        # Sacamos el porcentaje ((1 - x) * 100) y lo rendondeamos a 2 decimales
        result = ((1 - result) * 100).__round__(2)

        # Imprimimos el resultado
        printResult(numberOfPeople, result)
    else:
        # Si el número de personas es mayor o igual que el número de días que tiene un año entonces la probabilidad será de un 100%
        # Esto se conoce como principio del palomar o principio de las cajas donde se indica lo siguiente:
        # Si se distribuyen n palomas (en este caso personas) en m cajas (en este caso dias del año) habrá obligatoriamente (como mínimo) 1 paloma en cada caja (1 persona en cada dia del año)
        # En nuestro caso querrá decir que 1 día tendrá obligatoriamente 2 personas (como mínimo) nacidas ese día
        result = 100

        # Imprimimos el resultado
        printResult(numberOfPeople, result)


def calculateProbability(favorableCases, posibleCases):
    # Se va a utilizar la tecnica de casos favorables entre casos posibles (CF/CP)
    return float(favorableCases) / float(posibleCases)


def printResult(numberOfPeople, result):
    print("Hay un " + str(result) + "% de probabilidades de que 2 personas cumplan años el mismo dia en un grupo de " +
          str(numberOfPeople) + " personas")


if __name__ == '__main__':
    main()
