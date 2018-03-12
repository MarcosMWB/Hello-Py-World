def imc(we, he):
    i = we / (he * he)
    return i


def ideal_weight(height, sex):
    if sex == "m" or sex == "male":
        print("Your ideal weight is: " + str((72.2 * height) - 57))
    else:
        print("Your ideal weight is: " + str((62.1 * height) - 44.7))


def weight():
    h = float(input("Enter your height: "))
    w = float(input("Enter your weight: "))
    s = input("Enter your sex: male or female ").lower()
    print("your IMC: " + str(imc(w, h)))
    if imc(w, h) < 18.5:
        print("Too low IMC!")
    elif imc(w, h) < 24.9:
       print("Normal IMC!")
    elif imc(w, h) < 29.9:
        print("High IMC!")
    elif imc(w, h) < 34.9:
        print("First degree of obesity!")
    elif imc(w, h) < 39.9:
            print("Second degree of obesity!!")
    else:
        print("Third degree of obesity!!!")
    answer = input("Would you like to see your ideal weight? ").lower()
    if answer == "yes" or answer == "y" or answer == "yep":
        ideal_weight(h, s)


weight()
