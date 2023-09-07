import csv
import matplotlib.pyplot as plt

# Read data from CSV file
x_data = []
y_data = []
with open('data4.csv', newline='') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
        x_data.append(float(row[1]))
        y_data.append(float(row[2]))

# Plot data as a line graph
plt.plot(x_data, y_data)
plt.xlabel('X Distance')
plt.ylabel('Y Distance')
plt.grid()
plt.title('90 degree mouse movement ')
plt.show()
