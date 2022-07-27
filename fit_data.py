"""
FIt data using min max scalar - this has to be run AFTER you have made a datafile
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import config
import functions_pressure as funp

 #read data, minmax fit, and save to pickle
DATA_FILENAME = config.paths_["DATA_FILENAME"]
FIT_FILENAME = config.paths_["FIT_MINMAX_FILENAME"]
print (f"using:\n{DATA_FILENAME}\nwill do a minMax fit\nsave as pickle to:\n{FIT_FILENAME}..")

df = pd.read_csv(DATA_FILENAME,skiprows=50) #skipping the first 50 rows as they are full of shit
df[df < 0] = 0 #todo make this into a general filter when aquiriing data
scaler = MinMaxScaler()
X = df.iloc[:,1:]
scaler.fit(X.values)
funp.save_pickle(filepath_=FIT_FILENAME, pickle_object=scaler)
print(f"..fit saved {FIT_FILENAME}")
X_scaled = scaler.transform(X)


