import pandas as pd

filename = 'old.xlsx'
df = pd.read_excel(filename)
olddf = df[df['شرح کالا'] == 'خودرو سواری']

filename = 'new.xlsx'
df = pd.read_excel(filename)
newdf = df[df['شرح کالا'] == 'خودرو سواری']

merged = olddf.merge(newdf, how='outer', indicator=True)
new_rows = merged[merged['_merge'] == 'right_only'].drop('_merge', axis=1)

filtered = 'جانبازان معزز'
filtered_rows = new_rows[new_rows['مدل و مشخصات فنی کالا'].str.contains(filtered)]
filtered_rows2 = new_rows[~new_rows['مدل و مشخصات فنی کالا'].str.contains(filtered)]

filtered_rows.to_excel('diff.xlsx')
filtered_rows2.to_excel('diff2.xlsx')

