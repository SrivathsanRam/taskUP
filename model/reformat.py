import pandas as pd
from helper import get_postalcode
from helper import get_age

df = pd.read_csv('model/resale_dataset.csv')


df.drop(columns=['month', 'lease_commence_date','flat_model'], inplace=True)
df = df.tail(13080)
df = df.sample(n=5000, random_state=1)
df['postal_code'] = df.apply(lambda row: get_postalcode(row['block']+" "+row['street_name']), axis=1)
df['lease'] = df.apply(lambda row: get_age(row['remaining_lease']), axis = 1)

df.drop(columns=['block', 'street_name', 'remaining_lease'], inplace=True)


output_file = 'model/modified_data_2.csv'
df.to_csv(output_file, index=False)
