# 🧱 BrickWorth
**AI-powered Lego Resale Value Predictor & Set Recommender**

BrickWorth is a data science project that predicts the resale value of Lego sets and recommends similar builds based on theme, piece count, and release year.  
Built with Python, Machine Learning, and public Lego datasets, this project demonstrates skills in **data engineering, exploratory data analysis, regression modeling, and recommendation systems**.

---

## 📌 Features
- **Lego Price Prediction**  
  Estimate the current market value of a Lego set using machine learning models.
- **Set Recommendation Engine**  
  Discover similar Lego sets based on themes, piece count, and release year.
- **Interactive Dashboard** *(Coming Soon)*  
  A Streamlit app for searching sets, predicting prices, and exploring recommendations.
- **End-to-End Data Pipeline**  
  From API ingestion to cloud-ready ML deployment.

---

## 🛠 Tech Stack
- **Languages:** Python 3, SQL  
- **Libraries:** pandas, scikit-learn, XGBoost, LightGBM, matplotlib, seaborn  
- **Data Sources:**  
  - [Rebrickable API](https://rebrickable.com/api/) – Lego set metadata  
  - BrickLink Marketplace Data – Historical pricing  
  - Kaggle Lego Datasets – Sales history & set details
- **Tools:** Jupyter, Streamlit, AWS S3 (future deployment), GitLab/GitHub

---

## 📂 Project Structure
```bash
brickworth-lego-price-predictor/
│
├── data/
│   ├── raw/                # Raw API/scraped data
│   ├── processed/          # Cleaned data ready for ML
│
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_model_training.ipynb
│   ├── 04_recommender.ipynb
│
├── src/
│   ├── config.py
│   ├── data_ingestion.py
│   ├── preprocessing.py
│   ├── train_model.py
│   ├── recommender.py
│
├── models/
│   ├── price_model.pkl
│
├── dashboard/
│   ├── app.py              # Streamlit app
│
├── requirements.txt
├── README.md
├── Makefile
