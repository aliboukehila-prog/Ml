import os
import django
import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

# Étape 1 : Configuration Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crud.settings")  # Remplacez 'votre_projet'
django.setup()

# Étape 2 : Import du modèle
from produit.models import Produit  # Remplacez 'votre_app' et 'House'

# Étape 3 : Récupération des données
houses = Produit.objects.all().values_list('surface', 'prix')

# Étape 4 : Transformation en np.array
data = np.array(list(houses))
X = data[:, 0].reshape(-1, 1)  # surface
Y = data[:, 1]  # prix

print (X,Y)
# Étape 5 : Entraînement du modèle
model = LinearRegression()
model.fit(X, Y)

# Étape 6 : Sauvegarde
joblib.dump(model, 'model_DB.pkl')
print("Modèle sauvegardé dans model.pkl")
