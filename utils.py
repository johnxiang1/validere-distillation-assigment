import requests
import pandas as pd

from bs4 import BeautifulSoup

def crudes_dictionary():
    crudes_dict = {
        "MSW_Feeder":["FD", "MSY", "MPR", "P", "MSE"],
        "Light_Sweet":["MSW", "RA"],
        "Light_Sour":["BCL", "BDY", "CAL", "MJT", "PLS"],
        "Medium_Sour":["MBL", "MGS", "MSM", "SPR"],
        "Pooled_Crudes_ex_Superior":["CHV", "HSC", "LSB", "MSB", "MSW(S)", "PCH", "PSY", "SYB", "SYN"],
        "Sweet_Synthetic":["CNS", "HSB", "PSC", "PAS", "SSX", "OSA", "SSP"],
        "Heavy_Sour_Conventional":["BRN", "BRS", "F", "LLB", "LLK", "SH", "SC", "WH", "WCB"],
        "Heavy_Sour_Unconventional":["AWB", "BHB", "CNX", "CDB","CL","FRB", "KDB", "LCB", "SHD","WDB","WCS"],
        "Heavy_Sour_Synbit":["PSH", "PXB", "SCS", "SHB", "SMA"],
        "Heavy_Sour_Partially_Upgraded":["AHS"],
        "Heavy_Low_Resid":["OSH"],
    }
    return crudes_dict

def all_dict_values(dict1):
    all_list= []
    for i in dict1.values():
        all_list = i + all_list
    return all_list

def strip_data(soup_list):
    data_list = []
    for element in soup_list:
        data_list.append(element.text.strip())
    return data_list

def get_three_lists_from_data(data_list):
    temperature_list = []
    average_list = []
    stdev_list = []
    for i in range(len(data_list)):
        if i%3==0:
            temperature_list.append(data_list[i])
            average_list.append(data_list[i+1])
            stdev_list.append(data_list[i+2])
    return temperature_list, average_list, stdev_list

def covert_cols_to_numerica(df, num_cols):
    for col in num_cols:
        df[col] = pd.to_numeric(df[col], errors = "coerce")
    return df

def get_distillation_as_df(acronym):
    url = f"https://www.crudemonitor.ca/crudes/dist.php?acr={acronym}&time=recent"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    col_name = strip_data(soup.find_all("tbody")[0].find_all("th"))
    data_list = strip_data(soup.find_all("tbody")[0].find_all("td", class_="celsius"))

    temperature_list, average_list, stdev_list = get_three_lists_from_data(data_list)
    df = pd.DataFrame(list(zip(col_name, temperature_list, average_list, stdev_list)),
                      columns=["Mass_%_Recovered", "Temperature", "Average", "Standard_Deviation"])
    df = covert_cols_to_numerica(df, ["Temperature", "Average", "Standard_Deviation"])
    df["Acronym"] = acronym

    return df

def distillation_model(v1=2, v2=2, oil1="BCL", oil2="OSH", dictionary=True):
    final_df = pd.DataFrame(columns=["Mass_%_Recovered", "Temperature", "Average", "Standard_Deviation"])
    for acronym in [oil1, oil2]:
        df = get_distillation_as_df(acronym)
        final_df = pd.concat([final_df, df])

    temperature1 = final_df[final_df["Acronym"] == oil1]["Temperature"]
    temperature2 = final_df[final_df["Acronym"] == oil2]["Temperature"]

    average_temp = (temperature1 * v1 + temperature2 * v2) / (v1 + v2)

    result_df = pd.concat([final_df[final_df["Acronym"] == oil1]["Mass_%_Recovered"] + "%", average_temp], axis=1)

    if dictionary:
        return result_df.set_index("Mass_%_Recovered").to_dict()["Temperature"]
    else:
        return result_df