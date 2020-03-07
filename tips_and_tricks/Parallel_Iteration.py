x_coords = [23,64,27,67]
y_coords = [23,56,3,10]
z_coords = [12,54,62,11]

for x,y,z in zip(x_coords,y_coords,z_coords):
    print(x,y,z)


print()
monthly_profit = [52300,48800,57100,41100,62800]
monthly_costs = [43200,56000,26030,41100,12222]

for profit,costs in zip(monthly_profit,monthly_costs):

    print(f"Net profit: {profit-costs}")