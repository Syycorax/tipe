import matplotlib.pyplot as plt
safeness_table = [
            0.3125,
            0.625,
            0.625,
            0.875,
            0.8125,
            0.875,
            0.375,
            0.375,
            0.375,
            0.4375]

#plot each value by index+1
# remove the first value and put it at the end
temp = safeness_table.pop(0)
safeness_table.append(temp)
plt.plot([i+1 for i in range(10)], safeness_table)
label = [str(i+2) for i in range(9)]+["as"]
plt.xticks([i+1 for i in range(10)], label)
plt.ylabel("Safeness")
plt.xlabel("Première carte du croupier")
plt.show()
