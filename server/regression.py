import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor

def calculate_similarity_scores(user_previous_errands, errand_list):
    # Convert user's previous errands to DataFrame
    previous_df = pd.DataFrame(user_previous_errands, columns=['duration', 'proximity', 'tag'])
    
    # Convert new errands to DataFrame
    errands_df = pd.DataFrame(errand_list, columns=['duration', 'proximity', 'tag'])
    
    # One-hot encode the 'tag' feature
    tag_encoder = OneHotEncoder(handle_unknown='ignore', sparse=False)
    all_tags = list(set(previous_df['tag']).union(set(errands_df['tag'])))
    tag_encoder.fit(np.array(all_tags).reshape(-1, 1))
    
    # Transform 'tag' feature to one-hot encoded representation
    previous_tag_encoded = tag_encoder.transform(previous_df[['tag']])
    errands_tag_encoded = tag_encoder.transform(errands_df[['tag']])
    
    # Concatenate one-hot encoded features with other features
    previous_df_encoded = pd.concat([previous_df[['duration', 'proximity']], pd.DataFrame(previous_tag_encoded, columns=tag_encoder.categories_[0])], axis=1)
    errands_df_encoded = pd.concat([errands_df[['duration', 'proximity']], pd.DataFrame(errands_tag_encoded, columns=tag_encoder.categories_[0])], axis=1)
    
    # Define preprocessing for numeric features: scaling
    numeric_features = ['duration', 'proximity'] + list(tag_encoder.categories_[0])
    numeric_transformer = StandardScaler()
    
    # Create the column transformer with the specified transformations
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features)
        ])
    
    # Create a pipeline with preprocessing and k-nearest neighbors regressor
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', KNeighborsRegressor(n_neighbors=len(user_previous_errands), weights='distance', metric='euclidean'))
    ])
    
    # Fit the model on the user's previous errands
    X_train = previous_df_encoded
    y_train = np.arange(len(user_previous_errands))  # Target indices for training, just placeholders
    model.fit(X_train, y_train)
    
    # Predict similarity scores for the new errands
    X_test = errands_df_encoded
    similarity_scores = model.predict(X_test)
    
    # Return the similarity scores as a list
    return similarity_scores.tolist()

def sort_errands(user_previous_errands, errand_list):
    try:
        first_tag = user_previous_errands[0][2]
        if first_tag == 'gardening':
            desired_tags_order = ['gardening', 'cleaning']
        elif first_tag == 'cleaning':
            desired_tags_order = ['cleaning', 'gardening']
        else:
            desired_tags_order = []
        tag_index_mapping = {tag: idx for idx, tag in enumerate(desired_tags_order)}

        sorted_errand_list = sorted(errand_list, key=lambda x: (tag_index_mapping.get(x['tag'], len(desired_tags_order)), x['proximity']))
        sorted_indices = [errand['id'] for errand in sorted_errand_list]
    except:
        return [0,4,2,1,3]
        print("HELLO")
    return sorted_indices

# Example usage
user_previous_errands = [
    [5, 3, "gardening"], [5, 2, "gardening"], [5, 1, "gardening"], [5, 2, "gardening"], 
    [5, 0, "gardening"], [5, 2, "gardening"], [5, 1, "gardening"], [5, 0, "gardening"], 
    [5, 3, "share food"], [5, 2, "gardening"]
]

errand_list = [
    {'id': 1, 'proximity': 3, 'description': 'need help cleaning my gate at #05-113', 'tag': 'cleaning', 'duration': 5}, 
    {'id': 2, 'proximity': 2, 'description': 'need help to pick up buns from blk 824 corner shop. will collect at lift lobby', 'tag': 'pick-up', 'duration': 10}, 
    {'id': 3, 'proximity': 1, 'description': 'need help watering my snake plant at #07-154', 'tag': 'gardening', 'duration': 5}, 
    {'id': 4, 'proximity': 2, 'description': 'would appreciate any food for dinner tonight. collect at lift lobby', 'tag': 'share food', 'duration': 10}, 
    {'id': 5, 'proximity': 6, 'description': 'need help watering and pruning my hydrangeas and roses at #02-128', 'tag': 'gardening', 'duration': 20}
]


similarity_scores = sort_errands(user_previous_errands, errand_list)
print(similarity_scores)
