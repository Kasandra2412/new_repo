import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_excel("Mantamonis_bacterial_contamination_analysis.xlsx") #reading the data

counts = df["Preliminary Verdict:"].value_counts() #count the values

#making the bar chart
plt.figure(figsize=(8,6))
counts.plot(kind="bar", color="pink", edgecolor="black")

plt.title("The number of Eukaryotes and Prokaryotes")
plt.xlabel ("Type of Cell")
plt.ylabel("Count")
plt.tight_layout()

#saving the databar as png
plt.savefig("preliminary_classification.png")

