# 📱 Spam-Ham Detector Web App

A lightweight Flask-based web application that classifies SMS messages as **Spam** or **Ham** using a trained machine learning model. Built with a focus on precision, recall, and real-world usability.

## 🚀 Features

- 🔍 Accurate spam detection using ensemble ML techniques
- 📊 Model trained with TF-IDF vectorization and evaluated using ROC curves, confusion matrices
- 🧠 Handles class imbalance with SMOTE and class weights
- 🖥️ Clean, responsive UI styled with custom CSS
- 📁 Easy-to-deploy Flask backend

## 🧠 Model Details

- **Vectorizer**: TF-IDF
- **Classifier**: Voting Ensemble (Naive Bayes, Random Forest)
- **Evaluation**: Precision, Recall, ROC-AUC, Confusion Matrix
- **Artifacts**: `model.pkl`, `vectorizer.pkl`

## 📂 Project Structure
├── app.py                      # Flask app entry point ├── SMS_Spam&Ham_Detection.ipynb # Model training and evaluation notebook ├── model.pkl                   # Trained ML model ├── vectorizer.pkl              # TF-IDF vectorizer ├── static/ │   └── css/                    # Custom styles └── templates/ └── index.html              # Web interface


## 🛠️ Setup Instructions

1. Clone the repo  
   `git clone https://github.com/Yash-bendre/spam-Ham-Detector-webapp.git`

2. Install dependencies  
   `pip install -r requirements.txt` 

3. Run the app  
   `python app.py`

4. Open your browser at  
   `http://localhost:5000`

## 📌 Future Enhancements

- Add support for smishing detection
- Include feedback loop for user corrections
- Deploy on cloud (Heroku, Render, etc.)

## 👨‍💻 Author

**Yash Bendre**  
Persistent | Analytical | Passionate about real-world ML deployment

---
