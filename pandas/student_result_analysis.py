import pandas as pd

df = pd.DataFrame({
    "Name": ["Ram", "Sita", "Hari", "Gita"],
    "Marks": [80, 92, 68, 88]
})

print(df)

print("\nAverage Marks:", df["Marks"].mean())

print("\nTopper:")
print(df[df["Marks"] == df["Marks"].max()])

print("\nPassed Students:")
print(df[df["Marks"] >= 40])