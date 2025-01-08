import numpy as np
arr= np.array([1, 2, 3, 4, 5])
print(type(arr))

a=np.array(42)
b=np.array([1, 2 ,3, 4, 5, 6])
c=np.array([[1, 2 ,3], [4, 5, 6]])
d=np.array([[[1, 2 ,3], [4, 5, 6], [1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


#Puzzle: Find the sum of elements along the diagonal and flip the matrix
matrix= np.random.randint(1, 21, (4, 4))
print("Original Matrix")
print(matrix)

#Calculate the sum of diagonal
diagonal_sum=np.trace(matrix)
print(f"\nSum of diagonal elements: {diagonal_sum}")

#flip the matrix vertically and horizontally
flipped_matrix= np.flip(matrix)
print("\nFlipped Matrix:")
print(flipped_matrix)

#Bonus: Identify positions of elements greater than 15
positions= np.argwhere(matrix>15)
print("\nPositions of elements greater than 15:")
for pos in positions:
    print(f"Row {pos[0] + 1},   Column {pos[1]+1}")


import csv
#File path for the sales tracker
file_path="sales_tracker.csv"
#Create a new csv file with headers
def create_csv():
    headers=["Date", "Products", "Quantity", "Price per Unit", "Total"]
    with open(file_path, mode="w", newline="") as file:
        writer= csv.writer(file)
        writer.writerow(headers)
    print("Sales tracker created.")
#Add a new sale record to the csv file
def add_sale(date, product, quantity, price_per_unit):
    total=quantity*price_per_unit
    with open(file_path, mode="a", newline="") as file:
        writer= csv.writer(file)
        writer.writerow([date, product, quantity, price_per_unit, total])
    print("Sale record added.")
 #Calculate total sales from the csv files
def calculate_total_sales():
    total_sales=0
    with open(file_path, mode="r") as file:
        reader= csv.DictReader(file)
        for row in reader:
            total_sales +=float(row["Total"])
        print(f"Total Sales: ${total_sales:.2f}")

create_csv()
add_sale("2025-01-08", "Laptop", 2, 1200.50)
add_sale("2025-01-06", "Mouse", 5, 25.99)
calculate_total_sales()


