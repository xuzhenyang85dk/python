
my_data = [el for el in range(25)]
my_data3 = [el **2 for el in range(50)]
my_data4 = [el **3 for el in range(50)]
print(my_data)

%matplotlib notebook
import matplotlib.pyplot as plt

input_values = list(range(10,16))
my_data2 = [el **2 for el in input_values]

plt.plot(input_values,my_data2)

plt.title("Square Numbers", fontsize = 12)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize =10)
# Set size of tick labels
plt.tick_params(axis = 'both', labelsize = 10)

%matplotlib inline

plt.scatter(input_values,my_data2, s= 100)

%matplotlib inline
list(zip(input_values,my_data2))

count = 0
data ={}

import kkdata

print(kkdata.STATISTICS[2015])

my_data= kkdata.STATISTICS[2015]
for city, age in my_data.items():
    for age, nationalities in age.items():
        age_index = age
        for value in nationalities.values():
            count = data.get(age_index, 0)
            count += value
            data[age_index] = count

plt.bar(data.keys(), data.values())
plt.title("Distribution of CPH Citizens", fontsize = 12)
plt.xlabel("Ages", fontsize = 10)
plt.ylabel("A", fontsize =10)
plt.savefig("1.svg")
