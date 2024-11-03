# BOX OFFICE COLLECTION ANALYSIS
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: Box office collection by year
data = {
    'Year': [2018, 2019, 2020, 2021, 2022],
    'Box Office (in Millions)': [4000, 4500, 3000, 3500, 4800]
}

df = pd.DataFrame(data)

# Plotting the box office collection over the years
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Box Office (in Millions)'], marker='o', color='green', linewidth=3)
plt.title('Box Office Collection Over Years', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Box Office (in Millions)', fontsize=14)
plt.xticks(df['Year'])
plt.grid()
plt.tight_layout()
plt.show()

print(df)





