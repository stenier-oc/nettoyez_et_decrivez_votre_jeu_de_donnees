#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd # On importe la librairie Pandas, que l'on surnomme 'pd'

def lower_case(value): 
    print('Voici la valeur que je traite:', value)
    return value.lower()

data = pd.DataFrame([['A',1],
                     ['B',2],
                     ['C',3]], columns = ['lettre','position'])

nouvelle_colonne = data['lettre'].apply(lower_case)
nouvelle_colonne = nouvelle_colonne.values
print(nouvelle_colonne)
data['lettre'] = nouvelle_colonne
print(data)


# In[2]:


# import des librairies dont nous aurons besoin
import pandas as pd
import numpy as np
import re

# chargement et affichage des données
data = pd.read_csv('personnes.csv')
print(data)


# In[3]:


VALID_COUNTRIES = ['France', "Côte d'ivoire", 'Madagascar', 'Bénin', 'Allemagne', 'USA']

def check_country(country):
    if country not in VALID_COUNTRIES:
        print(' - "{}" n\'est pas un pays valide, nous le supprimons.'.format(country))
        return np.NaN
    return country


# In[4]:


def first(string):
    parts = string.split(',')
    first_part = parts[0]
    if len(parts) >= 2:
        print(' - Il y a plusieurs parties dans "{}", ne gardons que {}.'            .format(parts,first_part))  
    return first_part


# In[5]:


def convert_height(height):
    found = re.search('\d\.\d{2}m', height)
    if found is None:
        print('{} n\'est pas au bon format. Il sera ignoré.'.format(height))
        return np.NaN
    else:
        value = height[:-1] # on enlève le dernier caractère, qui est 'm'
        return float(value)

def fill_height(height, replacement):
    if pd.isnull(height):
        print('Imputation par la moyenne : {}'.format(replacement))
        return replacement
    return height


# In[6]:


data['email'] = data['email'].apply(first)
data['pays'] = data['pays'].apply(check_country)
data['taille'] = [convert_height(t) for t in data['taille']]
data['taille'] = [t if t<3 else np.NaN for t in data['taille']]

mean_height = data['taille'].mean()
data['taille'] = [fill_height(t, mean_height) for t in data['taille']]
data['date_naissance'] = pd.to_datetime(data['date_naissance'],format='%d/%m/%Y', 
                                        errors='coerce')

print(data)


# In[7]:


data

