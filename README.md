# BD4Predict API Usage Documentation

This document provides an overview of how to use the BD4Predict API for predictive modeling. The API accepts JSON workloads as input and identifies missing data with a value of `-1`.

## Endpoint

### `/predict`

This endpoint is used to generate predictions based on the input data.

- **Method**: `POST`
- **Content-Type**: `application/json`

#### Request Body

The request body should be a JSON object containing the following fields:

- `hn1_dv_age_cons`: Age of the patient (integer)
- `hn1_na8_cb_sex`: Sex of the patient (0 for male, 1 for female)
- `hn1_icd_group_conf`: ICD group configuration (string, e.g., "1 - oral cavity")
- `hn1_tnm_stage_best`: TNM stage (integer)
- `hn1_a7a_ay_education_level`: Education level (integer)
- `hn1_a5_ay_marital_status`: Marital status (string, e.g., "4 - married")
- `hn1_imd10quint`: IMD Deprivation index (integer)
- `hn1_dv_a21_ay_hhold_income`: Household income level (integer)
- `hn1_nb4_cb_comorb_index`: Comorbidity index (integer)
- `hn1_nb9a_cb_hpv_status`: HPV status (string, e.g., "not obtained")
- `hn2_surgery`: Surgery status (1 for yes, 0 for no)
- `hn2_chemotherapy`: Chemotherapy status (1 for yes, 0 for no)
- `hn2_radiotherapy`: Radiotherapy status (1 for yes, 0 for no)
- `hn1_a8_ay_tobacco`: Tobacco use (string, e.g., "3 - never")
- `hn1_dv_bmi`: Body Mass Index (integer)
- `hn1_dv_total_wk`: Alcohol consumption in units/week (integer)
- Additional fields for various health and functional status indicators, which can be set to `-1` if data is missing.

#### Example with Bash
```bash
curl -X 'POST' 
'https://bd4predict.azurewebsites.net/predict/' 
-H 'accept: application/json' 
-H 'Content-Type: application/json' 
-d '{
"hn1_dv_age_cons": 42,
"hn1_na8_cb_sex": 1,
"hn1_icd_group_conf": "1 - oral cavity",
"hn1_tnm_stage_best": 1,
"hn1_a7a_ay_education_level": 3,
"hn1_a5_ay_marital_status": "4 - married",
"hn1_imd10quint": 0,
"hn1_dv_a21_ay_hhold_income": 5,
"hn1_nb4_cb_comorb_index": 1,
"hn1_nb9a_cb_hpv_status": "not obtained",
"hn2_surgery": 1,
"hn2_chemotherapy": 0,
"hn2_radiotherapy": 1,
"hn1_a8_ay_tobacco": "3 - never",
"hn1_dv_bmi": 25,
"hn1_dv_total_wk": 0,
"hn3_dv_c30_role_func": -1,
"hn3_dv_c30_phys_func": -1,
"hn3_dv_c30_emot_func": -1,
"hn3_dv_c30_cog_func": -1,
"hn3_dv_c30_soc_func": -1,
"hn3_dv_c30_fatigue": -1,
"hn3_dv_c30_nausea": -1,
"hn3_dv_c30_pain": -1,
"hn3_dv_c30_dyspnoea": -1,
"hn3_dv_c30_insomnia": -1,
"hn3_dv_c30_appetite": -1,
"hn3_dv_c30_constipation": -1,
"hn3_dv_c30_diarrhoea": -1,
"hn3_dv_c30_ghs": -1,
"hn3_dv_hn35_pain": -1,
"hn3_dv_hn35_speech": -1,
"hn3_dv_hn35_sex": -1,
"hn3_dv_hn35_drymouth": -1,
"hn3_dv_hn35_ill": -1,
"hn3_dv_hn35_swallow": -1,
"hn3_dv_hn35_soceat": -1,
"hn3_dv_hn35_teeth": -1,
"hn3_dv_hn35_saliva": -1,
"hn3_dv_hn35_senses": -1,
"hn3_dv_hn35_soccon": -1,
"hn3_dv_hn35_openmouth": -1,
"hn3_dv_hn35_cough": -1
}'```

### Example with Python

```python
import requests
import json

# Define the URL for the API endpoint
url = 'https://bd4predict.azurewebsites.net/predict/'

# Define the headers
headers = {
  'accept': 'application/json',
  'Content-Type': 'application/json'
}



# Define the payload
payload = {
  "hn1_dv_age_cons": 42,
  "hn1_na8_cb_sex": 1,
  "hn1_icd_group_conf": "1 - oral cavity",
  "hn1_tnm_stage_best": 1,
  "hn1_a7a_ay_education_level": 3,
  "hn1_a5_ay_marital_status": "4 - married",
  "hn1_imd10quint": 0,
  "hn1_dv_a21_ay_hhold_income": 5,
  "hn1_nb4_cb_comorb_index": 1,
  "hn1_nb9a_cb_hpv_status": "not obtained",
  "hn2_surgery": 1,
  "hn2_chemotherapy": 0,
  "hn2_radiotherapy": 1,
  "hn1_a8_ay_tobacco": "3 - never",
  "hn1_dv_bmi": 25,
  "hn1_dv_total_wk": 0,
  "hn3_dv_c30_role_func": -1,
  "hn3_dv_c30_phys_func": -1,
  "hn3_dv_c30_emot_func": -1,
  "hn3_dv_c30_cog_func": -1,
  "hn3_dv_c30_soc_func": -1,
  "hn3_dv_c30_fatigue": -1,
  "hn3_dv_c30_nausea": -1,
  "hn3_dv_c30_pain": -1,
  "hn3_dv_c30_dyspnoea": -1,
  "hn3_dv_c30_insomnia": -1,
  "hn3_dv_c30_appetite": -1,
  "hn3_dv_c30_constipation": -1,
  "hn3_dv_c30_diarrhoea": -1,
  "hn3_dv_c30_ghs": -1,
  "hn3_dv_hn35_pain": -1,
  "hn3_dv_hn35_speech": -1,
  "hn3_dv_hn35_sex": -1,
  "hn3_dv_hn35_drymouth": -1,
  "hn3_dv_hn35_ill": -1,
  "hn3_dv_hn35_swallow": -1,
  "hn3_dv_hn35_soceat": -1,
  "hn3_dv_hn35_teeth": -1,
  "hn3_dv_hn35_saliva": -1,
  "hn3_dv_hn35_senses": -1,
  "hn3_dv_hn35_soccon": -1,
  "hn3_dv_hn35_openmouth": -1,
  "hn3_dv_hn35_cough": -1
}

# Make the POST request
response = requests.post(url, headers=headers, data=json.dumps(payload))

# Check if the request was successful
if response.status_code == 200:
  # Parse the JSON response
  result = response.json()
  print("Predicted Value:", result['predicted_value'])
  print("Confidence Interval:", result['ci'])
  print("Decline Probability:", result['decline_probability'])
  print("Death Probability:", result['death_probability'])
  print("Death Decline Probability:", result['death_decline_probability'])
  print("Joint Decline Probability:", result['joint_decline_probability'])
  print("Conformal Predictive Distribution:", result['conformal_predictive_distribution'])
  print("Imputation:", result['imputation'])
else:
  print("Request failed with status code:", response.status_code)
```

#### Response

The response is a JSON object containing the following fields:

- `predicted_value`: The predicted value (integer)
- `ci`: Confidence interval (array of two integers)
- `decline_probability`: Probability of decline (float)
- `death_probability`: Probability of death (float)
- `death_decline_probability`: Joint probability of death and decline (float)
- `joint_decline_probability`: Joint probability of decline (float)
- `conformal_predictive_distribution`: Distribution of conformal predictions (array of floats)
- `imputation`: Object containing original input and imputed values where necessary

#### Example Response

```json
{
"predicted_value": 73,
"ci": [60, 83],
"decline_probability": 0.7,
"death_probability": 0.3,
"death_decline_probability": 0.79,
"joint_decline_probability": 0.49,
"conformal_predictive_distribution": [ 0, 0, 3, 4.5],
"imputation": {
// Original input and imputed values
}
}
```


## Server Wakening time

When using the BD4Predict API for the first time, or after a period of inactivity, you may experience a slight delay in receiving predictions. This is because the API is hosted on an Azure server that enters a sleep state when not in use for an extended period. The initial request triggers the server to wake up, which can take a little time. Subsequent requests should be processed more quickly once the server is fully active.

This behavior is important for several reasons, particularly in the context of resource management, energy consumption, and environmental impact. By allowing the server to enter a sleep state during periods of inactivity, the system conserves computational resources and reduces energy usage. This not only helps in lowering operational costs but also minimizes the carbon footprint associated with running cloud-based services. Efficient resource management is crucial in promoting sustainable technology practices, as it contributes to reducing the overall environmental impact of data centers, which are significant consumers of energy. By optimizing server usage, the BD4Predict API aligns with broader efforts to create more environmentally friendly and sustainable digital infrastructures.

## Imputation and uncertainty

The accuracy and reliability of predictions generated by the BD4Predict API can be affected when a significant number of quality of life variables are missing and require imputation. Imputation is a statistical technique used to estimate missing data, but it introduces a degree of uncertainty into the predictions. When many variables are imputed, the model's ability to accurately reflect the true conditions and outcomes diminishes, leading to less precise predictions. Therefore, for the most reliable results, it is important to provide as complete and accurate data as possible, minimizing the need for imputation and enhancing the model's predictive power. We use KNN imputer which does not take into account imputation uncertainty as a single imputation method. 


## About the BD4QoL project

  The BD4QoL (Big Data for Quality of Life) project is an innovative initiative aimed at enhancing the quality of life for cancer patients through the use of big data and advanced analytics. By integrating data from various sources, including clinical records, patient-reported outcomes, and lifestyle information, the project seeks to develop personalized care strategies that address the unique needs of each patient. The goal is to improve long-term health outcomes and well-being by providing healthcare professionals with actionable insights and tools to tailor interventions more effectively. Through collaboration among researchers, clinicians, and technology experts, BD4QoL aims to transform cancer care and support systems, ultimately leading to better patient experiences and outcomes.

## Usage terms

The developers of the BD4Predict tool provide this software as-is, without any express or implied warranties. While efforts have been made to ensure the accuracy and reliability of the tool, the developers assume no responsibility for errors, omissions, or any outcomes resulting from the use of this tool. Users are advised to employ the tool at their own risk and discretion. It is important to consult with qualified healthcare professionals when making decisions based on the tool's predictions. By using the BD4QoLPredict tool, you acknowledge and agree that the developers shall not be held liable for any direct, indirect, incidental, or consequential damages arising from its use.
        
