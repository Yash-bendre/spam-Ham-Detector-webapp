from flask import Flask,request,render_template,redirect,session,url_for,flash
import pickle
import nltk
from nltk.corpus import stopwords       
from nltk.stem import WordNetLemmatizer 
from string import punctuation 
lemmatizer = WordNetLemmatizer()



vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

app=Flask(__name__)

def text_transform(text):
    text=text.lower()
    text=nltk.word_tokenize(text)
    y=[]
    for i in text:
        if i.isalnum():
            y.append(i)
    
    text=y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in punctuation:
            y.append(i)
    
    text=y[:]
    y.clear()
    for i in text:
        y.append(lemmatizer.lemmatize(i))
        
    return " ".join(y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/prediction',methods=['POST'])
 
def predict():
    if request.method == 'POST':
        message = request.form.get('message')
        processed = text_transform(message)
        vectorized = vectorizer.transform([processed])
        proba = model.predict_proba(vectorized)[0]
        prob_ham, prob_spam = proba[0], proba[1]
        if prob_spam > prob_ham:
            result = "Spam"
            confidence = prob_spam * 100
        else:
            result = "Ham"
            confidence = prob_ham * 100

        return render_template(
            "index.html",
            message=message,
            result=result,
            confidence=f"{confidence:.2f}%",
            prob_ham=f"{prob_ham*100:.2f}%",
            prob_spam=f"{prob_spam*100:.2f}%"
        )

if __name__=='__main__':
    app.run(debug=True)
    