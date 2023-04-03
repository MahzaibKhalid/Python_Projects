import pandas as pd
df= pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/articles.csv",encoding = 'latin1')
#df.to_csv("dataset.csv")

df['Number_of_Words']= df['Article'].apply(lambda n: len(n.split()))

df.to_csv("new_dataset.csv")