# Fake_News_Detection
# 📰 Fake News Detection System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-black)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Passive%20Aggressive%20Classifier-green)
![Render](https://img.shields.io/badge/Deployed%20on-Render-purple)

---

## 📖 About the Project

This is a Fake News Detection web application made using **Python**, **Flask**, and **Machine Learning**.

The purpose of this project is to check whether a news article is **Real** or **Fake**. The user enters the news text and the model predicts the result.

I made this project to improve my knowledge of Machine Learning, Flask, GitHub, and Render deployment.

---

## 🌐 Live Demo

**Website:**  
https://fake-news-detection-1-ewp3.onrender.com/

**GitHub Repository:**  
https://github.com/vinitkushwaha548-beep/Fake_News_Detection

---

## ✨ Features

- Predicts whether news is Real or Fake
- Simple and easy-to-use interface
- Fast prediction
- Machine Learning based project
- Responsive web design
- Deployed on Render

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- Tailwind CSS
- Scikit-learn
- Pandas
- NumPy
- Pickle
- Git
- GitHub
- Render

---

## 🤖 Machine Learning Model

This project uses:

- TF-IDF Vectorizer
- Passive Aggressive Classifier

The model is trained on a fake news dataset and saved using Pickle.

---

## 📂 Project Structure

```text
Fake_News_Detection
│
├── app.py
├── finalized_model.pkl
├── vectorizer.pkl
├── requirements.txt
├── Procfile
├── README.md
│
├── images
│   ├── input.jpg
│   └── output.jpg
│
├── templates
│   ├── index.html
│   ├── prediction.html
│   ├── about.html
│   └── contact.html
│
└── static
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/vinitkushwaha548-beep/Fake_News_Detection.git
```

### Open the project

```bash
cd Fake_News_Detection
```

### Install required packages

```bash
pip install -r requirements.txt
```

### Run the project

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

## Input

![Input Screenshot](images/input.png.jpg)

---

## Output

![Output Screenshot](images/output.png.jpg)

---

## 📝 How It Works

1. User enters a news headline or article.
2. The text is cleaned.
3. TF-IDF converts the text into numbers.
4. The trained Passive Aggressive Classifier predicts the result.
5. The website displays whether the news is Real or Fake.

---

## 📈 Future Improvements

- Improve model accuracy
- Add more training data
- Show prediction confidence
- Store previous predictions
- Improve the website design

---

## 👨‍💻 Author

**Vinit Kushwaha**

B.Tech – Artificial Intelligence and Machine Learning (AIML)

2nd Year | 3rd Semester

United College of Engineering and Research

GitHub:  
https://github.com/vinitkushwaha548-beep

---

## 🙏 Thank You

Thank you for visiting my project.

If you like this project, please give it a ⭐ on GitHub.
