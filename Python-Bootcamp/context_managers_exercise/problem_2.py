
with open("temperatures_c.txt","r") as f, open("temperatures_f.txt","w") as file:
    temperatures = f.read().splitlines()
    temperature_in_fahrenheit = []
    for c in temperatures:
        f = (float(c) * 9/5 + 32)
        temperature_in_fahrenheit.append(f)
    for c in temperature_in_fahrenheit:
        file.write(str(c) + "\n")


