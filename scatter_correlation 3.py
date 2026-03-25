import pandas as pd
import matplotlib.pyplot as plt

data = {'Marks': [55, 60, 65, 70, 72, 74, 78, 80, 82, 85, 88, 90, 92, 95, 98]}
df = pd.DataFrame(data)

plt.figure(figsize=(6,4))
plt.hist(df['Marks'], bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(4,5))
plt.boxplot(df['Marks'], patch_artist=True, boxprops=dict(facecolor='lightgreen'))
plt.title('Box Plot of Marks')
plt.ylabel('Marks')
plt.show()