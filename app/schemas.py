from pydantic import BaseModel
from typing import Dict

class PredictionRequest(BaseModel):
    hn1_dv_age_cons: int = 42
    hn1_na8_cb_sex: int = 1
    hn1_icd_group_conf: str = "1 - oral cavity"
    hn1_tnm_stage_best: int = 1
    hn1_a7a_ay_education_level: int = 3
    hn1_a5_ay_marital_status: str = "4 - married"
    hn1_imd10quint: int = 0
    hn1_dv_a21_ay_hhold_income: int = 5
    hn1_nb4_cb_comorb_index: int = 1
    hn1_nb9a_cb_hpv_status: str = "not obtained"
    hn2_surgery: int = 1
    hn2_chemotherapy: int = 0
    hn2_radiotherapy: int = 1
    hn1_a8_ay_tobacco: str = "3 - never"
    hn1_dv_bmi: float = 25
    hn1_dv_total_wk: float = 0
    hn3_dv_c30_role_func: float = -1
    hn3_dv_c30_phys_func: float = -1
    hn3_dv_c30_emot_func: float = -1
    hn3_dv_c30_cog_func: float = -1
    hn3_dv_c30_soc_func: float = -1
    hn3_dv_c30_fatigue: float = -1
    hn3_dv_c30_nausea: float = -1
    hn3_dv_c30_pain: float = -1
    hn3_dv_c30_dyspnoea: float = -1
    hn3_dv_c30_insomnia: float = -1
    hn3_dv_c30_appetite: float = -1
    hn3_dv_c30_constipation: float = -1
    hn3_dv_c30_diarrhoea: float = -1
    hn3_dv_c30_ghs: float = -1
    hn3_dv_hn35_pain: float = -1
    hn3_dv_hn35_speech: float = -1
    hn3_dv_hn35_sex: float = -1
    hn3_dv_hn35_drymouth: float = -1
    hn3_dv_hn35_ill: float = -1
    hn3_dv_hn35_swallow: float = -1
    hn3_dv_hn35_soceat: float = -1
    hn3_dv_hn35_teeth: float = -1
    hn3_dv_hn35_saliva: float = -1
    hn3_dv_hn35_senses: float = -1
    hn3_dv_hn35_soccon: float = -1
    hn3_dv_hn35_openmouth: float = -1
    hn3_dv_hn35_cough: float = -1



# Pydantic model definitions for the responses
class PredictionResponse(BaseModel):
    predicted_value: float = 73
    ci: list = [60.0, 83.0]
    decline_probability: float = 0.7
    death_probability: float = 0.3
    death_decline_probability: float = 0.79
    joint_decline_probability: float = 0.49
    conformal_predictive_distribution: list = [0.0, 0.0, 3.0, 4.5]
    imputation: Dict
