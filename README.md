# 🩺 MedChat AI – Disease Prediction Chat App

This project is a Medical Chat App built using **Django** and trained using **SVM (Support Vector Machine)** to predict diseases based on user input symptoms. The model leverages **natural language processing** and **fuzzy matching** to validate symptoms and provide real-time predictions.

---

## 🚀 Features

- 💬 Chat-based interface for predicting diseases
- 🧠 Trained ML model (SVM) with TF-IDF + spaCy lemmatization
- 🔍 Fuzzy symptom validation using `fuzzywuzzy`
- 📈 Accuracy display on test data
- ✅ Real-time predictions via user input
- 🛠️ Trained and deployed using `joblib` for model persistence

---

## 🛠️ Tech Stack

| Layer          | Tools/Libs                          |
|----------------|-------------------------------------|
| Frontend       | HTML, CSS, Bootstrap (Django templating) |
| Backend        | Django, Python                      |
| ML / NLP       | `scikit-learn`, `spaCy`, `fuzzywuzzy`, `joblib` |
| Dataset        | Custom `DiseaseAndSymptoms.csv`     |
| Model Type     | `SVC(kernel='linear')`              |

---

## 📁 Directory Structure

```
medchat-app/
├── disease_model/
│   ├── model.pkl               # Trained SVM model
│   ├── vector.pkl              # TF-IDF vectorizer
│   └── DiseaseAndSymptoms.csv  # Dataset
├── medchat/                    # Django project files
│   ├── views.py                # Chat logic and prediction
│   ├── urls.py
│   └── templates/
│       └── index.html          # Chat UI
├── static/                     # CSS/JS assets
├── manage.py
└── README.md
```

---

## 🧠 ML Model Details

- **Dataset**: `DiseaseAndSymptoms.csv`
- **Text Preprocessing**: Lemmatization using `spaCy`, stopword and non-alpha token removal
- **Vectorization**: TF-IDF with `TfidfVectorizer`
- **Model**: `SVC(kernel="linear")`
- **Symptom Validation**: Using `fuzzywuzzy.process.extractOne` with threshold matching

### 📈 Accuracy

Test accuracy achieved using unseen test set:
```
Accuracy: ~90%+
```

---

## 🧪 Sample Workflow

1. User inputs:  
   `fever headache vomiting`
2. System checks if symptoms exist (fuzzy validation)
3. If valid → text is preprocessed → vectorized → model predicts
4. Output:  
   `Predicted Disease: Typhoid`

---

## 💡 How to Run the Project

### 1️⃣ Clone & Install Requirements
```bash
git clone https://github.com/Sharavanakumar-Ramalingam/medchat-ai.git
cd medchat-ai
pip install -r requirements.txt
```

### 2️⃣ Download spaCy Model
```bash
python -m spacy download en_core_web_sm
```

### 3️⃣ Run Django Server
```bash
python manage.py runserver
```

### 4️⃣ Access in Browser
Navigate to:  
[http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📦 Model Training Pipeline (Used Internally)

```python
# Read and combine symptoms
data = pd.read_csv("DiseaseAndSymptoms.csv")
data['text'] = data.apply(lambda row: ' '.join(row.dropna().values.tolist()[1:]), axis=1)

# Preprocess using spaCy
def preprocess_text(text):
    doc = nlp(text)
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

# TF-IDF + SVM
tfidf = TfidfVectorizer()
X = tfidf.fit_transform(data['preprocessed_text'])
y = data['Disease']

model = SVC(kernel='linear')
model.fit(X, y)

# Save models
joblib.dump(model, 'model.pkl')
joblib.dump(tfidf, 'vector.pkl')
```

---

## 🧾 Requirements

Install all dependencies with:
```bash
pip install -r requirements.txt
```


> "Predicting diseases with language, one symptom at a time."
