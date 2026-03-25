import numpy as np
import pandas as pd

marks = [85, 90, 78, 88]
print("List of Marks:", marks)

arr = np.array([1, 2, 3, 4, 5])
print("\nArray Elements:", arr)

data = {
 'Name': ['Ram', 'Sita', 'Ravi'],
 'Marks': [85, 92, 78]
}
df = pd.DataFrame(data)
print("\nDataFrame:\n", df)

matrix = np.array([[1, 2], [3, 4]])
print("\nMatrix:\n", matrix)