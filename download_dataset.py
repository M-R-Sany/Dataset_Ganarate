from google.colab import files

# 1. Save the dataframe as a CSV file on the Colab cloud server
df_expanded.to_csv('cyberbullying_5lakh_dataset.csv', index=False)

# 2. Trigger an automatic browser download to your computer
files.download('cyberbullying_5lakh_dataset.csv')