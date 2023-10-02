current_population = 7.9e9 # Current world population
growth_rate = 0.0105 # Annual population growth rate

print("Year\tWorld Population\tIncrease")
for year in range(1, 101):
    population_increase = current_population * growth_rate
new_population = current_population + population_increase
print(f"{year}\t{new_population:.2e}\t{population_increase:.2e}")
current_population = new_population