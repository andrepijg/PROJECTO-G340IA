import pandas as pd
from sklearn.preprocessing import OneHotEncoder 

data ={
    "Habitantes":[12000,8000,5000,7500,9000],
    "consumo_kwh":[3000,2000,1200,1700,2500],
    "Municipios":["Quibdó","Istmina","Tadó","Quibdó","Istmina"]
}
df= pd.DataFrame(data)
#one hot encoding
encoder = OneHotEncoder(sparse_output=False)
encoded = encoder.fit_transform(df[["Municipios"]])
#convertir
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(["Municipios"]))
df_final=pd.concat([df.drop(columns=["Municipios"]),encoded_df],axis=1)
print(df_final)

