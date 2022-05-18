import os

import pandas as pd
from numpy import arange

file = 'EagleShare Bookings'

abs_path = os.path.abspath(os.path.join('C:', 'Users', 'Lee', 'Downloads', file + '.xlsx'))
df = pd.read_excel(abs_path, usecols="A:D", engine="openpyxl")

# Replace the column headers with numbers from 0 to number of columns
df.columns = arange(0, len(df.columns))

grand_total_df = df[df[0].str.contains("GRAND TOTAL", na=False)]
grand_total = grand_total_df[3].values[0]

print(grand_total)
