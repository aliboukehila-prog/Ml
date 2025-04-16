# train_model.py
import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

# Données d'exemple : surfaces (en m²) et prix (en €)
#get the date from the DB

# transform data into np arrays

X = np.array([[20], [30], [40], [50], [60], [70], [80]])  # surface
y = np.array([40000, 60000, 80000, 100000, 120000, 140000, 160000])  # prix

print(X,y)
# Création du modèle
model = LinearRegression()
model.fit(X, y)


# Sauvegarde du modèle
joblib.dump(model, 'model.pkl')

print("Modèle sauvegardé dans model.pkl")
