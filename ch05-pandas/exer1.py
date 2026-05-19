import pandas as pd

data = {
    "Name": ["Ali", "Siti", "John"],
    "Age": [21, 22, 23],
    "Marks": [85, 90, 88]
}

df = pd.DataFrame(data)
print(df)