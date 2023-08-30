code_content = '''
# Social Science Project: Analysis of Advertisements

## Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from textblob import TextBlob
import numpy as np
import re
from sklearn.feature_extraction.text import CountVectorizer

## Data Collection
# Simulated dataset for demonstration
data = {
    'Advertisement': ['Panasonic: Your Inner Man', 'Apple: Think Different', 'Nike: Just Do It', 'Coca-Cola: Open Happiness'],
    'Text': [
        'Unleash the man in you. Our products redefine masculinity.',
        'Dare to be different. Our technology sets you apart.',
        'Just Do It. No excuses.',
        'Open a bottle, open happiness. Life tastes better with Coca-Cola.'
    ]
}
ads_df = pd.DataFrame(data)

## Data Preprocessing
# Function to clean and tokenize text
def clean_and_tokenize(text):
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()
    return text

# Cleaning and tokenization
ads_df['Cleaned_Text'] = ads_df['Text'].apply(clean_and_tokenize)

## Exploratory Data Analysis (EDA)
# Generate a Word Cloud
all_text = ' '.join(ads_df['Cleaned_Text'])
wordcloud = WordCloud(background_color='white').generate(all_text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud of Advertisement Text")
plt.show()

## Text Analysis
# Sentiment Analysis using TextBlob
ads_df['Polarity'] = ads_df['Cleaned_Text'].apply(lambda x: TextBlob(x).sentiment.polarity)
ads_df['Subjectivity'] = ads_df['Cleaned_Text'].apply(lambda x: TextBlob(x).sentiment.subjectivity)

# Calculate average polarity and subjectivity
avg_polarity = np.mean(ads_df['Polarity'])
avg_subjectivity = np.mean(ads_df['Subjectivity'])

# Display results
print("Average Polarity:", avg_polarity)
print("Average Subjectivity:", avg_subjectivity)
'''

# Save the code as a Python script (.py) file
code_file_path = '/mnt/data/Analysis_of_Advertisements_Code.py'
with open(code_file_path, 'w') as f:
    f.write(code_content)

code_file_path
