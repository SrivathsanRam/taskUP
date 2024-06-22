import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsRegressor

def calculate_similarity_scores(user_previous_errands, errand_list):
    # Create DataFrame for user's previous errands
    previous_df = pd.DataFrame(user_previous_errands, columns=['duration', 'proximity', 'tag'])
    
    # Create DataFrame for new errands to be scored
    errands_df = pd.DataFrame(errand_list, columns=['duration', 'proximity', 'tag'])
    
    # Define preprocessing for numeric features: scaling
    numeric_features = ['duration', 'proximity']
    numeric_transformer = StandardScaler()
    
    # Define preprocessing for categorical features: one-hot encoding
    categorical_features = ['tag']
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    
    # Create the column transformer with the specified transformations
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    # Create a pipeline with preprocessing and k-nearest neighbors regressor
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('regressor', KNeighborsRegressor(n_neighbors=3))
    ])
    
    # Fit the model on the user's previous errands
    X_train = previous_df
    y_train = np.random.rand(len(previous_df))  # Use random scores for training for now
    model.fit(X_train, y_train)
    
    # Predict similarity scores for the new errands
    X_test = errands_df
    similarity_scores = model.predict(X_test)
    
    return similarity_scores.tolist()

# Example usage
user_previous_errands = [
    [5, 3, "gardening"], [5, 2, "gardening"], [5, 1, "gardening"], [5, 2, "gardening"], 
    [5, 0, "gardening"], [5, 2, "gardening"], [5, 1, "gardening"], [5, 0, "gardening"], 
    [5, 3, "share food"], [5, 2, "gardening"]
]

errand_list = [
    {'id': 1, 'proximity': 0, 'description': 'need help cleaning my gate at #05-113', 'tag': 'cleaning', 'duration': 5}, 
    {'id': 2, 'proximity': 1, 'description': 'need help to pick up buns from blk 824 corner shop. will collect at lift lobby', 'tag': 'pick-up', 'duration': 10}, 
    {'id': 3, 'proximity': 1, 'description': 'need help watering my snake plant at #07-154', 'tag': 'gardening', 'duration': 5}, 
    {'id': 4, 'proximity': 2, 'description': 'would appreciate any food for dinner tonight. collect at lift lobby', 'tag': 'share food', 'duration': 10}, 
    {'id': 5, 'proximity': 6, 'description': 'need help watering and pruning my hydrangeas and roses at #02-128', 'tag': 'gardening', 'duration': 20}
]

# Extract relevant fields from errand_list
errand_list_relevant = [
    {'duration': errand['duration'], 'proximity': errand['proximity'], 'tag': errand['tag']}
    for errand in errand_list
]

similarity_scores = calculate_similarity_scores(user_previous_errands, errand_list_relevant)
print(similarity_scores)
