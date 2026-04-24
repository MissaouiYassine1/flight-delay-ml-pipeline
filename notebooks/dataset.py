import pandas as pd

dataset = pd.DataFrame({'id_vol':[i for i in range(1,5)],'ville_depart':["Sfax","Kasserine","Kef","Tunis"],'retard_minutes':[0,1,3,5]})

est_en_retard = lambda x: x>=15

ret_20 = est_en_retard(20)

ret_5 = est_en_retard(5)

prix_bruts = ["12€", "45€", "Error", "99€", "Missing"]

prix_bruts = [i for i in prix_bruts if "€" in i ]

prix_bruts = [float(i.replace("€","")) for i in prix_bruts]

print(dataset.head(0))
num_dataset = dataset.select_dtypes(include='number')

print(num_dataset.describe())

print(dataset.loc[:, 'ville_depart'])

print(dataset.iloc[1,-1] )

vols_problematiques = dataset[dataset['retard_minutes'] > 1]

dataset['statut']= dataset["retard_minutes"].apply(lambda x: "A l'heure" if x == 0 else "En retard")

print(dataset)

