import pandas as pd

#reading the excel dataset into a database df
df = pd.read_excel("Mantamonis_bacterial_contamination_analysis.xlsx")

#only taking two columns
df = df[["contig ID","Seq Coverage"]]

#sorting
df.sort_values(by=["Seq Coverage"], ascending=False, inplace=True) #sorting in descending order

df.to_excel("output.xlsx", sheet_name="filter_mantamonis", index=False)
