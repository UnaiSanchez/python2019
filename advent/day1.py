from math import floor

def total_fuel(masses):
    totals=[]
    for mass in masses:
        total = 0
        total += calculate_fuel(mass)
        print("total",format(total))
        fuel_to_carry_fuel = calculate_fuel(total)
        while fuel_to_carry_fuel > 0:
            total += fuel_to_carry_fuel
            fuel_to_carry_fuel = calculate_fuel(fuel_to_carry_fuel)
            
        totals.append(total)
    return sum(totals)
def calculate_fuel(mass):
    return floor(mass/3)-2
    #return mass // 3 - 2

if __name__ == "__main__":
    import requests
    result = requests.get("https://adventofcode.com/2019/day/1/input",headers={"Cookie":"session=53616c7465645f5fac89cf998fac93f435284ce88ea6efc41991a4f9db153252e1661574971b0703391be2466df07592"})

    if result.status_code == 200:
        text = result.text
        split_lines = text.splitlines()

        converted = []
        for num in split_lines:
            converted.append(int(num))
        print(total_fuel(converted))
    else:
        print("Error:",result.status_code)
