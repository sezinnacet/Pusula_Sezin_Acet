import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import KNNImputer

def load_data(file_path):
    # Loading the data
    return pd.read_excel(file_path)

def handle_missing_data_with_knn(data):

    categorical_columns = ['Cinsiyet', 'Uyruk', 'Il', 'Kan Grubu']
    numerical_columns = ['Kilo', 'Boy']
    
    encoder = OneHotEncoder(sparse_output=False)
    encoded_data = pd.DataFrame(encoder.fit_transform(data[categorical_columns]))
    
    # Merging numerical and categorical columns
    combined_data = pd.concat([encoded_data, data[numerical_columns].reset_index(drop=True)], axis=1)
    combined_data.columns = combined_data.columns.astype(str)
    
    imputer_knn = KNNImputer(n_neighbors=5)
    imputed_data = pd.DataFrame(imputer_knn.fit_transform(combined_data), columns=combined_data.columns)
    
    # Assigning the filled numerical data back to the original dataset
    data[numerical_columns] = imputed_data.iloc[:, -2:]  # The last two columns are the numerical data
    
    return data

def encode_categorical(data):
    
    categorical_columns = ['Cinsiyet', 'Uyruk', 'Il', 'Kan Grubu']
    encoder = OneHotEncoder(sparse_output=False, drop='first')
    encoded_data = pd.DataFrame(encoder.fit_transform(data[categorical_columns]), 
                                columns=encoder.get_feature_names_out(categorical_columns))
    
    # Merging the data
    data = data.drop(categorical_columns, axis=1)
    data = pd.concat([data, encoded_data], axis=1)
    return data

def standardize_data(data):
    
    scaler = StandardScaler()
    data[['Kilo', 'Boy']] = scaler.fit_transform(data[['Kilo', 'Boy']])
    return data

def visualize_data_with_original(data_original, data_encoded):
    # Gender distribution 
    plt.figure(figsize=(6,4))
    sns.countplot(data=data_original, x='Cinsiyet')
    plt.title("Gender Distribution")
    plt.show()

    # Top 10 common side effects
    plt.figure(figsize=(10,6))
    top_side_effects = data_original['Yan_Etki'].value_counts().head(10)
    sns.barplot(y=top_side_effects.index, x=top_side_effects.values, palette='viridis')
    plt.title("Top 10 Common Side Effects")
    plt.xlabel("Frequency")
    plt.ylabel("Side Effect")
    plt.show()

    # Height and weight relationship
    plt.figure(figsize=(6,6))
    sns.scatterplot(x='Boy', y='Kilo', data=data_encoded)
    plt.title("Height vs. Weight Relationship")
    plt.show()

# Running the pipeline
file_path = 'side_effect_data.xlsx'
data_original = load_data(file_path)  
data = load_data(file_path)  

data = handle_missing_data_with_knn(data)  # Filling missing data using KNNImputer
data = encode_categorical(data)  # Encoding categorical data
data = standardize_data(data)  # Normalizing numerical data

visualize_data_with_original(data_original, data)

processed_data_head = data.head()
print(processed_data_head)
