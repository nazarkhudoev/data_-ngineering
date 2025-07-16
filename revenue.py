import pandas as pd 

# Sample data extraction
data = {
    'Date': ['2025-07-01', '2025-07-02', '2025-07-03', '2025-07-01', '2025-07-02'],
    'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple'],
    'Sales': [10, 20, 15, 25, 30],
    'Price': [1.5, 0.5, 1.5, 0.5, 1.5]
}

df = pd.DataFrame(data)

# Calculate total revenue
df['Revenue'] = df['Sales'] * df['Price']

# Group by product and sum sales and revenue
summary = df.groupby('Product').agg({'Sales': 'sum', 'Revenue': 'sum'})

print(summary)


###    Sales  Revenue
#Product
#Apple       55     82.5
#Banana      45     22.5 