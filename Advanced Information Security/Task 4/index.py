import pandas as pd 


data = pd.read_csv("data.csv")
data["ARO"] = data["FrequencyOfOccurrencesPerYear"]
data["ALE"] = data["ARO"] * data["CostPerIncident"]

print(data.head())
print("max threat: ", data.loc[data['ALE'].idxmax()]["ThreatCategory"])