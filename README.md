#### SMS- Spam Detection classifier Final output:

![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/78912b31-7762-45dd-9bbd-678ba9ab489e)

# Overview
This project involves creating an SMS spam detection system using Python for data processing and machine learning, and deploying the application using Streamlit. The system classifies SMS messages as spam or not spam based on user input.
# 1. Data Processing and Model Building
### 1.1 Data Loading
We started by loading the dataset spam.csv, which contains SMS messages labeled as spam or ham (not spam). The dataset was loaded using pandas.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/5b1a92b1-4681-4f29-8347-100d8993f486)
# 1.2 Data Cleaning
We cleaned the data by dropping unnecessary columns and renaming the remaining columns for clarity.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/1212bc63-475e-465b-8579-d27e88c431c2)
# 1.3 Data Preprocessing
- Label Encoding: We converted the target labels ('ham' and 'spam') into numerical values using LabelEncoder.
- Removing Duplicates: Duplicate entries were removed to ensure data quality.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/a2b85cd6-1ed7-4039-a0fb-84a4ca8e79d2)
# 1.4 Feature Engineering
We created new features to analyze the text data:
- Number of Characters: The length of each message.
- Number of Words: The number of words in each message.
- Number of Sentences: The number of sentences in each message.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/0abcb55b-ff76-47ae-b1bf-3b0bc06d2b8e)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/fc09e3c2-59cd-456b-9863-6b99e89809b2)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/5b7dfc56-5050-4dd5-96ab-fba7edfdf803)
# 1.5 Text Preprocessing
We processed the text data by:
- Converting text to lowercase.
- Tokenizing the text.
- Removing stop words and punctuation.
- Stemming the words to their root forms.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/4e256760-26d7-4f24-9b43-b5a1e4d4b87e)
# 1.6 Vectorization and Model Training
- TF-IDF Vectorization: We converted the text data into numerical vectors using TF-IDF.
- Model Training: We trained a Multinomial Naive Bayes model on the vectorized data.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/181c6af3-dce4-412e-9e7b-e20f4655332c)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/2aaa8e81-64fb-416b-b29f-6522fce1476d)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/aab3a235-430f-441d-a541-215d1b8869ca)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/2a539250-2f48-4320-a31c-e0a72775e193)
# Model Improvement/Evaluation:
1st Improvement (Features_restricted)
- change the max_features parameter of TfIdf
- Actaully when we tried with TfIdf vectorizer to convert textual data into numerical, by default we considered all the features but there is one hidden parameter with named as "max_features"
- It means basically when we vectorize the text data into numerical data, we do not define how many frequent words take into consideration. By using "max_feature"we can say 3000, it means only top 3000 words will be consider into analysis.
- Let's see whether it impart any changes in the output
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/226d5edd-b8e1-4098-a694-9fddc87d4139)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/39ed98e5-0668-461f-afb5-4e1aead1e049)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/a49a4629-71e0-46b7-8e70-e6d5361435af)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/1002869e-4fc0-4dcd-ae70-9e6b2fcd6196)
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/a4bd2bef-7ab0-4c42-973f-007131d3e13f)
# 1.7 Model Saving
The trained model and the TF-IDF vectorizer were saved using pickle for later use in the application.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/a0a6d2e6-acee-40dd-adcf-0a3bc27b19e4)
# 2. Application Deployment using Streamlit
### 2.1 Streamlit Setup
Streamlit was used to create a web application for the SMS spam detection system.
### 2.2 Loading the Model
The saved model and TF-IDF vectorizer were loaded in the Streamlit application.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/4d7237fa-aff3-4c82-b5a6-3a21e1707440)
### 2.3 Text Preprocessing Function
A function to preprocess the input text was created.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/60cf57fb-a427-49e3-b092-ba5c4ad6686f)
### 2.4 Word Cloud Generation
A function to generate and display a word cloud was created.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/3fa38af1-eb1d-4441-8442-8cf09428d49c)
### 2.5 Streamlit Interface
The Streamlit interface allows users to input an SMS message and get a prediction.
![image](https://github.com/sivasankarseelam/SMS-Email-Spam-Classifier/assets/133698242/d5a43389-002b-4be6-9f21-1f867f08d41c)













