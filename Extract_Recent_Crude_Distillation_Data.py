import pandas as pd
from utils import all_dict_values, crudes_dictionary, get_distillation_as_df

final_df = pd.DataFrame(columns = ["Mass_%_Recovered", "Temperature", "Average", "Standard_Deviation"])
print("Start loading Distinllation Profile from https://www.crudemonitor.ca/")
for acronym in all_dict_values(crudes_dictionary()):
    df = get_distillation_as_df(acronym)
    final_df = pd.concat([final_df, df])
    print(f"{acronym} distinllation profile has been extracted")
print(final_df)

final_df.to_csv('all_recent_distillation_profiles.csv')
print(f"all {len(all_dict_values(crudes_dictionary()))} "
      f"Crude Oils have been saved as all_recent_distillation_profiles.csv")
