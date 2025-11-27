import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("data/news.xlsx.csv", low_memory=False)

print("Columns:\n", df.columns)
df.head()
