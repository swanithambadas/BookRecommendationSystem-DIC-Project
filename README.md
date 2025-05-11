# BookRecommendationSystem-DIC-Project

> A Flask-based web application that delivers personalized book recommendations  
> using collaborative filtering (SVD) and Top-50 popularity models.

---

## 📋 Table of Contents

- [Description](#description)  
- [Features](#features)  
- [Overview](#overview)  
- [Goals](#goals)  
- [Architecture](#architecture)  
- [Technical Requirements](#technical-requirements)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Data](#data)  
- [Contributors](#contributors)  
- [License](#license)  

---

## 🔍 Description

`BookRecommendationSystem-DIC-Project` is a lightweight, modular Flask app that lets users upload a book ratings CSV and receive two types of recommendations:

1. **Top-50 Popular Books** – based on average ratings of titles with ≥ 100 reviews.  
2. **Personalized Recommendations** – using collaborative filtering via truncated SVD.

An interactive web UI guides you through uploading your data and viewing results.

---

## ⚙️ Features

- **Collaborative Filtering** (SVD): Predict user-specific book ratings.  
- **Top-N Popularity**: Quickly surface the 50 highest-rated books.  
- **Interactive Web UI**: Two pages—Home (Top 50) and Recommend (User-based).  
- **Visualization**: Error histogram of actual vs. predicted ratings (PNG).  
- **Data Caching**: Pre-computed pickle (`popular_df_final_100.pkl`) for fast startup.  

---

## 🗒️ Overview

This project addresses the need for both **global** and **personalized** suggestions in a simple package:

- **Global Trends**: Identify universally popular books.  
- **User Tastes**: Leverage rating patterns to tailor suggestions.  
- **Seamless Experience**: Drag-and-drop CSV upload; instant recommendations.  

---

## 🎯 Goals

1. **Accuracy** – Leverage SVD to minimize prediction error.  
2. **Performance** – Pre-compute heavy data transformations; serve results in under 1 sec.  
3. **Usability** – Clean, intuitive UI with clear instructions and error handling.  
4. **Extensibility** – Modular codebase—add new algorithms or swap data sources easily.

---

## 🏗️ Architecture

