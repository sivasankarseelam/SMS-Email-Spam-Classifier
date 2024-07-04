import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Ensure that the necessary NLTK data is downloaded
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# Load your trained models
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))


# Function to preprocess the text
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


# Function to generate and display a word cloud
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110).generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis('off')
    st.pyplot(fig)  # Pass the figure object to st.pyplot()


# Streamlit application layout
st.title("Email/SMS Spam Classifier")

input_sms = st.text_input("Enter the message")

if st.button('Predict'):
    # Preprocess the input
    transformed_sms = transform_text(input_sms)
    # Vectorize the input
    vector_input = tfidf.transform([transformed_sms])
    # Predict using the model
    result = model.predict(vector_input)[0]
    # Display the prediction result
    if result == 1:
        st.header("Spam")
    else:
        st.header("Not Spam")

    # Generate and display the word cloud
    generate_wordcloud(transformed_sms)