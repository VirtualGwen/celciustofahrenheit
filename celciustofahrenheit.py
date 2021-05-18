def c_to_f(temp_c):
    temp_f = temp_c * (9/5) + 32
    return temp_f

temp_c = float(input('Enter temperature in Celsius: '))
temp_f = None

temp_f = c_to_f(temp_c)



print('\nFahrenheit:' , temp_f)
