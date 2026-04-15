import pandas as pd
import numpy as np # Numpy nous permet de générer des vrais 'trous' (NaN)

dataset_v2 = pd.DataFrame({
    'id_vol': [101, 102, 103, 104, 105, 106],
    'compagnie': ['Nouvelair', 'Tunisair', 'Nouvelair', 'Tunisair', 'Nouvelair', 'Transavia'],
    'ville_depart': ['Djerba', 'Tunis', 'Djerba', 'Tunis', 'Monastir', 'Tunis'],
    'retard_minutes': [10, np.nan, 0, 45, np.nan, 5] 
    # np.nan simule un capteur qui n'a pas enregistré le retard
})

print(dataset_v2.isna().sum())

dataset_v2['retard_minutes']=dataset_v2['retard_minutes'].fillna(0)

print(dataset_v2.isna().sum())

group = dataset_v2.groupby('compagnie')['retard_minutes'].sum()

print(group)