import pandas as pd
import tools.utilitaires as tools

# Ouverture du fichier CSV
df = pd.read_csv("movies_etl/dataset/dataset_movies_25k.csv")

tools.separation_lignes()
## Pré-néttoyage des données

# Inspection du dataset
print("\nAffichage des 5 premières lignes du dataset")
print(df.head(5))

print("\nAffichage des informations du dataset")
print(df.info())

tools.separation_lignes()

# Colonnes inutiles ? Suppression de ceux-ci 
columns_to_drop = [
    'status', 'backdrop_path', 'homepage', 'imdb_id', 'original_title',
    'overview', 'poster_path', 'tagline', 'production_companies',
    'production_countries', 'spoken_languages', 'keywords']

df_movies = df.drop(columns_to_drop, axis=1)

print(df_movies.info())

# Gestion des valeurs manquantes
print("\nValeurs manquantes par colonne avant nettoyage :")
print(df_movies.isna().sum())

# Vue la faible quantité de valeurs manquantes dans le dataset, on supprime supprime ces lignes directement

# Suppression des lignes contenant des valeurs manquantes
df_movies = df_movies.dropna()

# Validation après suppression
print("\nNombre de lignes après suppression des valeurs manquantes :")
print(df_movies.shape[0])
print("\nValeurs manquantes par colonne après nettoyage :")
print(df_movies.isna().sum())