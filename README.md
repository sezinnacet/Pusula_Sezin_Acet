Name & Surname : Sezin Acet
E-mail address : sezinnacet@gmail.com

**Data Science Intern Case Study**

**Overview**

This document summarizes the data analysis and preprocessing steps taken in the project on medication side effects. Throughout the project, 
tasks such as handling missing data, encoding categorical variables, and normalizing numerical variables were carried out.

**Data Analysis and Preprocessing Steps**

a. Handling Missing Data
- Method: KNNImputer
- Missing values in the dataset were filled using the KNN algorithm, which utilizes neighboring data points. During this process, categorical variables such as gender,
  nationality, city, and blood type were converted into numerical values, and missing values in weight and height were imputed.
  
b. Encoding Categorical Variables
- Method: OneHotEncoder
- Categorical variables like gender, nationality, city, and blood type were encoded into binary (0 and 1) values to make them suitable for use in machine learning algorithms.

c. Normalizing Numerical Data
- Method: StandardScaler
- Numerical columns such as weight and height were normalized to bring the data to a standard scale.
  This ensures consistent results during modeling and helps avoid issues related to differing data ranges.

**Conclusion**

The data preprocessing steps resulted in a clean, complete, and ready-to-use dataset for modeling. Missing values were filled, categorical variables were encoded, 
and numerical data was normalized. These steps ensured the dataset was properly prepared for further analysis and modeling.

  
**Instructions to Run the Code**
1. Clone the Repository: First, clone the GitHub repository to your local machine:
   
   git clone https://github.com/sezinnacet/Pusula_Sezin_Acet
   cd Pusula_Sezin_Acet

2. Install Required Libraries: Install the required Python libraries using pip:
   
   pip install pandas matplotlib seaborn scikit-learn

3. Run the Python Script: Execute the script to load the dataset, process it, and generate the visualizations:

   python pusula.py

4. Dataset: The dataset should be placed in the same directory as the script or provide the correct path to the file_path variable in the script:

   file_path = '/.../side_effect_data.xlsx'
