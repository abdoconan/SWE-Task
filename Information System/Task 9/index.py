import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Function to preprocess the text
def preprocess_text(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize each sentence into words and remove stopwords
    stop_words = set(stopwords.words('english'))
    preprocessed_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        words = [word.lower() for word in words if word.isalnum()]
        words = [word for word in words if word not in stop_words]
        preprocessed_sentences.append(' '.join(words))
    
    return preprocessed_sentences

# Function to extract features and compute sentence scores
def extract_features(text):
    preprocessed_sentences = preprocess_text(text)
    
    # Vectorize the preprocessed sentences
    vectorizer = TfidfVectorizer()
    sentence_vectors = vectorizer.fit_transform(preprocessed_sentences)
    
    # Compute the similarity matrix
    similarity_matrix = cosine_similarity(sentence_vectors, sentence_vectors)
    
    # Calculate sentence scores based on the similarity matrix
    sentence_scores = similarity_matrix.sum(axis=1)
    
    return sentence_scores, preprocessed_sentences

# Function to generate the summary
def generate_summary(text, num_sentences=3):
    sentence_scores, preprocessed_sentences = extract_features(text)
    
    # Sort the sentences based on scores
    ranked_sentences = sorted(((score, index) for index, score in enumerate(sentence_scores)), reverse=True)
    
    # Select the top 'num_sentences' sentences for the summary
    selected_sentences = sorted([index for score, index in ranked_sentences[:num_sentences]])
    
    # Reconstruct the summary
    summary = ' '.join([preprocessed_sentences[index] for index in selected_sentences])
    
    return summary

# Example usage
document = '''
Text summarization is the process of distilling the most important information from a source text. It involves reducing the text to a concise and coherent summary. There are two main approaches to text summarization: extractive and abstractive. In extractive summarization, the summary is generated by selecting and combining important sentences or phrases from the source text. On the other hand, abstractive summarization involves generating new sentences that capture the essence of the source text. Extractive summarization is relatively simpler to implement compared to abstractive summarization. In this example, we will focus on the extractive approach and build a basic text summarization model using Python.
'''

summary = generate_summary(document, num_sentences=2)
print(summary)
