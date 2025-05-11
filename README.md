<p align="center">
  <img src="assets/demo.gif" alt="Book Recommendation System Demo" width="80%"/>
</p>

<h1 align="center">📚 NextChapter - Book Recommendation System</h1>
<p align="center">
  <strong>Your go-to Flask app for both trending and personalized book recommendations!</strong>
</p>

<p align="center">
  <a href="#features">✨ Features</a> • 
  <a href="#goals">🎯 Goals</a> • 
  <a href="#architecture">🏗️ Architecture</a> • 
  <a href="#tech-stack">🛠️ Tech Stack</a> • 
  <a href="#contributors">👥 Contributors</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Flask-2.0%2B-green?logo=flask&logoColor=white" alt="Flask"/>
  <img src="https://img.shields.io/badge/scikit--learn-0.24%2B-orange?logo=scikitlearn&logoColor=white" alt="scikit-learn"/>
  <img src="https://img.shields.io/badge/matplotlib-3.4%2B-purple?logo=matplotlib&logoColor=white" alt="matplotlib"/>
  <img src="https://img.shields.io/badge/license-MIT-red" alt="MIT License"/>
</p>

---

## 🔍 At a Glance

> **BookRecommendationSystem-DIC-Project** is a **lightweight**, **modular** Flask application that empowers readers with:
>
> - 🚀 **Top-50 Popular Books** based on community ratings  
> - 🤝 **SVD-Powered Collaborative Filtering** for truly **personalized** suggestions  
> - 📊 **Visual Feedback** via rating error histograms  
> - ⚡ **Lightning-Fast** startup with pre-computed pickle files

---

## ✨ Features

- 🎯 **Dual Recommendation Modes**  
  - **Global**: Top 50 books with ≥100 ratings, sorted by average score  
  - **Personalized**: Predict what _you_ will love using truncated SVD  
- 🖼️ **Interactive Web UI**  
  - Drag-and-drop CSV upload  
  - Dynamic results pages (“Home” & “Recommend”)  
- 📈 **Insightful Analytics**  
  - Error histogram showing predicted vs. actual ratings  
- 🔄 **Pre-Computed Models**  
  - `popular_df_final_100.pkl` for sub-second response times  

---

## 🎯 Goals

1. **Precision**: Minimize prediction error with robust SVD tuning  
2. **Performance**: Serve recommendations in under **1 second**  
3. **UX Excellence**: Intuitive interface with clear instructions & validation  
4. **Future-Proof**: Easily swap in new algorithms or data sources  

---

## 🏗️ Architecture

```text
┌────────────────────────────┐
│        Flask App           │   ← `app.py`
│ ────────────────────────── │
│ • Routes & Templates       │
│ • CSV File Handling        │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│    Recommendation Core     │   ← `recommender.py`
│ ────────────────────────── │
│ • Collaborative Filtering  │
│ • Error Visualization      │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│     Popularity Engine      │   ← `top_50.py`
│ ────────────────────────── │
│ • Filter & Rank by Rating  │
└────────────┬───────────────┘
             │
             ▼
┌────────────────────────────┐
│       Data Assets          │
│ ────────────────────────── │
│ • `phase3_merged_URB.csv`  │
│ • `popular_df_final_100.pkl`│
└────────────────────────────┘

## 🛠️ Tech Stack
| Component            | Technology         |
| -------------------- | ------------------ |
| **Language**         | Python 3.8+        |
| **Web Framework**    | Flask              |
| **Data Processing**  | pandas, numpy      |
| **Machine Learning** | scikit-learn (SVD) |
| **Visualization**    | matplotlib         |
| **Serialization**    | pickle             |
| **Templates**        | Jinja2             |

## 🚀 Quick Start

Clone & Navigate
git clone https://github.com/swanithambadas/BookRecommendationSystem-DIC-Project.git
cd BookRecommendationSystem-DIC-Project

Set Up Virtual Env
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install Dependencies
pip install flask pandas numpy scipy scikit-learn matplotlib

Run the App
python app.py

Browse
Open 👉 http://127.0.0.1:5000/
