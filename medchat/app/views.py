from django.shortcuts import render
from django.http import JsonResponse
import joblib
import spacy
import json

# Load the trained SVM classifier and TF-IDF vectorizer
svm_classifier = joblib.load("C:/Users/sharavana Kumar/Desktop/model.pkl")
tfidf_vectorizer = joblib.load("C:/Users/sharavana Kumar/Desktop/vector.pkl")

# Load the spaCy English language model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def predict_disease(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            symptoms = data.get('symptoms', '') 
            if symptoms:
                preprocessed_symptoms = preprocess_text(symptoms)
                symptoms_vectorized = tfidf_vectorizer.transform([preprocessed_symptoms])
                predicted_disease = svm_classifier.predict(symptoms_vectorized)[0]
                return JsonResponse({'predicted_disease': predicted_disease})
            else:
                return JsonResponse({'error': 'Symptoms data not provided'}, status=400) 
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def home(request):
    return render(request, 'home.html')
