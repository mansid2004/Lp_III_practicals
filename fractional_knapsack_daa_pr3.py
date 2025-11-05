class Item:
    def __init__(self, value, weight):
        self.value=value
        self.weight= weight
        self.ratio= value/weight

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value=0.0
    remaining_capacity= capacity

    for item in items:
        if item.weight<= remaining_capacity:
            total_value+= item.value
            remaining_capacity-= item.weight
        else:
            total_value+= item.ratio*remaining_capacity
            break
    return total_value

n= int(input("Enter number of items:"))
items=[]

for i in range(n):
    value=int(input(f"Enter value of items{i+1}:"))
    weight=int(input(f"Enter weight of item:{i+1}:"))
    items.append(Item(value, weight))

capacity=int(input("Enter knapsack capacity:"))
max_value=(fractional_knapsack(items,capacity))

print("Fractional knapsack is:", max_value)