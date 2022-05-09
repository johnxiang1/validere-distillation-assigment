# validere-distillation-assigment

Scripts for collecting distillation profile recent data from [Crude Monitor](https://www.crudemonitor.ca/home.php) and generating distillation profile of the mixture of two oils with specified volumne

#Installation
1. Clone this repository
2. Install the Python requirements
3. Run Extract_Recent_Crude_Distillation_Data
4. Run Blend_Two_Crude_Oils

```
git clone https://github.com/johnxiang1/validere-distillation-assigment.git
cd validere-distillation-assigment
pip install -r requirements.txt
python Extract_Recent_Crude_Distillation_Data.py
python Blend_Two_Crude_Oils.py
```

- **Blend_Two_Crude_Oils.py** is a script that needs to input first type of Crude Oil and Volume and the second type of Crude Oil and volumn, and it will then return the distillation profile of the mixture of two oils
- **Extract_Recent_Crude_Distillation_Data.py** is a script that extracts the all 59 distillation profiles from [Crude Monitor](https://www.crudemonitor.ca/home.php), and it saves the data to local as a csv file - all_recent_distillation_profiles.csv
