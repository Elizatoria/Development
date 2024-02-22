import pandas as pd  # Import for Pandas Library  # pip install pandas

animals = ['Lions', 'Tigers', 'Bears', 'Dogs', 'Cats']  # List Collection

df = pd.DataFrame(animals)  # Covert our List to a Format to which Pandas can use

print(df)

# df.to_csv('output.csv')  # This will give us our Output