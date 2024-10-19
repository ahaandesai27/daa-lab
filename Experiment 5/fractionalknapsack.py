import pandas as pd

class Item:
    def __init__(self, w, v, l):
        self.weight = w
        self.value = v
        self.shelf_life = l

    def __lt__(self, other):
        return (
            (self.value / (self.weight * self.shelf_life))
            < (other.value / (other.weight * other.shelf_life))
        )
    
class Reader:
    """Class to read csv file of items with value, weight and shelf life."""
    def __init__(self, file):
        self.df = pd.read_csv(file)
        self.weights = self.df['Weight'].to_list()
        self.values = self.df['Value'].to_list()
        self.shelf_lifes = self.df['Shelf Life'].to_list()
        
    def get_items_array(self):
        """Converting items in dataframe to an array of tuples."""
        items = []
        for w, v, l in zip(self.weights,  self.values, self.shelf_lifes):
            items.append(Item(w, v, l))

        return items

def fractional_knapsack(items, W):
    """Implementation of knapsack algorithm to find maximum profit among items."""
    items.sort(reverse = True)
    total_value = 0
    for item in items:
        if item.weight <= W:
            W -= item.weight
            total_value += item.value
        else:
            fraction = W / item.weight
            total_value += item.value * fraction
            break
    
    return round(total_value, 2)

def process_files(file):
    reader = Reader(file)
    items = reader.get_items_array()
    W = 200
    total_value = fractional_knapsack(items, W)
    print(f"Total value for file {file}: {total_value}")

if __name__ == '__main__':
    for i in range(1, 6):
        process_files(f"Knapsack Data/couriergoods{i}.csv")