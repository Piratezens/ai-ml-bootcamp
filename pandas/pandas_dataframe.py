import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Hari"],
    "Age": [20, 21, 22],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data)

print(df)