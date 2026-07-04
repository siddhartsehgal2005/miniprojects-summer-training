import pandas as pd

df = pd.read_csv("students.csv")

df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

print(df)
print("\nTopper:", df.loc[df["Total"].idxmax(), "Name"])