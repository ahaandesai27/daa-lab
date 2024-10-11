import csv
import random

def generate_csv(filename, num_rows):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Weight", "Value", "Shelf Life"])
        
        for i in range(1, num_rows + 1):
            weight = round(random.uniform(50, 150), 2)
            value = round(random.uniform(200, 500), 2)
            shelf_life = round(random.uniform(1, 6), 2)
            writer.writerow([i, weight, value, shelf_life])

for i in range(1,6):
    generate_csv(f'Knapsack Data/couriergoods{i}.csv', 100)