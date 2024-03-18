from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
import joblib


model = joblib.load('trained_model.pkl')

vectorizer = joblib.load('vectorizer.pkl')

def preprocess_text(text):
    return text.lower()

def predict_disease(symptoms):
 
    preprocessed_symptoms = preprocess_text(symptoms)

    
    features = vectorizer.transform([preprocessed_symptoms])

    
    predicted_disease = model.predict(features)

    return predicted_disease[0] 

# Example usage
user_input = "Symptoms entered by the user"
predicted_disease = predict_disease(user_input)
print("Predicted Disease:", predicted_disease)
