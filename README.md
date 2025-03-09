# Movie-Recommender-System

## 📌 Overview
This is a **Movie Recommender System** built using **Python, Sklearn, and Streamlit**. It suggests movies based on content similarity using NLP techniques like **Bag-of-Words** and **Cosine Similarity**.

## 🚀 Features
- Select a movie from the dropdown.
- Get **5 similar movie recommendations** based on the selected movie.
- Interactive **Streamlit UI** with a customized theme.

## 🛠️ Technologies Used
- **Python** (Backend Logic)
- **Pandas & NumPy** (Data Processing)
- **Scikit-learn** (Feature Extraction & Cosine Similarity)
- **Pickle** (Model Serialization)
- **Streamlit** (Web UI)

## 📂 Project Structure
```
Movie-Recommender-System/
│── app.py                # Main Streamlit App
│── movies_dict.pkl       # Serialized Movie Data
│── similarity.pkl        # Precomputed Similarity Matrix
│── README.md             # Project Documentation
```

## ⚙️ Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
```

### 2️⃣ Create and Activate a Virtual Environment
```sh
python -m venv env
# Windows
env\Scripts\activate
# Mac/Linux
source env/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install streamlit pandas numpy
```

## ▶️ Usage
### 1️⃣ Run the Streamlit App
```sh
streamlit run app.py
```
### 2️⃣ Open the Web App
- The app will launch in your browser at:  
  **http://localhost:8501/**

## 🏗️ How It Works
1. **Load Data**: Preprocessed movie dataset is loaded using **Pickle**.
2. **TF-IDF Vectorization**: Converts movie descriptions into numerical vectors.
3. **Cosine Similarity**: Computes the similarity between movies based on textual content.
4. **Recommend Movies**: Returns the top 5 most similar movies.

## 🔧 Customization
- Modify `movies_dict.pkl` and `similarity.pkl` to use a different dataset.
- Customize `app.py` for **UI enhancements**.


