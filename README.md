# 🚧 Road Accident Analysis & Hotspot Visualizer

This project combines **machine learning-based accident severity classification** and a **clickable interactive heatmap** to visualize accident hotspots across the UK. Built with Python, Folium, and Streamlit, it allows users to explore accident data and analyze high-risk zones in a user-friendly way.

---

## 🔍 Features

- ✅ **Accident Severity Classification**  
  Jupyter notebook (`road_accident.ipynb`) with data preprocessing, feature engineering, and training a Random Forest classifier to predict accident severity (Slight, Serious, Fatal).

- 📍 **Hotspot Visualization Web App**  
  Streamlit-based interactive map (`app.py`) where users can click on any UK region and view a heatmap of accident density around that area using weighted severity.

- 📊 **Dataset**  
  `accident_dataset_UK.csv`:The dataset is derived from UK-road accident dataset 2008-2017 with attributes like weather, road conditions, speed limits, and GPS coordinates.

---

## 🧪 Getting Started


### Install requirements

```bash
pip install streamlit pandas folium scikit-learn
```

### To run the web app

```bash
streamlit run app.py
```



