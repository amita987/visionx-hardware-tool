# ==========================
# PRIORITY ANALYSIS ENGINE
# ==========================

import pandas as pd

# ==========================
# DEFAULT WEIGHTS (editable later)
# ==========================

DEFAULT_WEIGHTS = {

    "VRAM_GB_weight": 1,
    "CUDA_Cores_weight": 1,
    "Tensor_Cores_weight": 1,
    "FP16_TFLOPS_weight": 1,
    "INT8_TOPS_weight": 1,
    "Price_weight": 1,

    # subjective (fixed weight = 1 but kept for structure clarity)
    "subjective_weight": 1

}


# ==========================
# LOAD / USE WEIGHTS
# ==========================

def get_weights(custom_weights=None):

    if custom_weights:
        return custom_weights

    return DEFAULT_WEIGHTS


# ==========================
# 0/1 CHECK FUNCTIONS
# ==========================

def check_vram(row, required_vram):

    return 1 if row["VRAM_GB"] >= required_vram else 0


def check_cuda(row, required_cuda):

    return 1 if row["CUDA_Cores"] >= required_cuda else 0


def check_tensor(row, required_tensor):

    return 1 if row["Tensor_Cores"] >= required_tensor else 0


def check_fp16(row, required_fp16):

    return 1 if row["FP16_TFLOPS"] >= required_fp16 else 0


def check_int8(row, required_int8):

    return 1 if row["INT8_TOPS"] >= required_int8 else 0


def check_price(row, max_price):

    return 1 if row["Price"] <= max_price else 0


# ==========================
# MAIN RANKING FUNCTION
# ==========================

def get_priority_recommendation(customer_output, weights=None, csv_path="hardware_database.csv"):


    df = pd.read_csv(csv_path)

    w = get_weights(weights)


    required_vram = customer_output["VRAM Required (GB)"]
    required_cuda = customer_output["CUDA Required"]
    required_tensor = customer_output["Tensor Required"]
    required_fp16 = customer_output["FP16 Required"]
    required_int8 = customer_output["INT8 Required"]
    max_price = customer_output.get("Budget", 999999)


    scores = []


    for _, row in df.iterrows():


        score = 0


        # ==========================
        # HARD CHECKS (0/1 × WEIGHT)
        # ==========================

        score += check_vram(row, required_vram) * w["VRAM_GB_weight"]
        score += check_cuda(row, required_cuda) * w["CUDA_Cores_weight"]
        score += check_tensor(row, required_tensor) * w["Tensor_Cores_weight"]
        score += check_fp16(row, required_fp16) * w["FP16_TFLOPS_weight"]
        score += check_int8(row, required_int8) * w["INT8_TOPS_weight"]
        score += check_price(row, max_price) * w["Price_weight"]


        # ==========================
        # SUBJECTIVE FIELDS (always 1)
        # ==========================

        score += 1  # Hardware_Type
        score += 1  # Manufacturer
        score += 1  # Model_Name
        score += 1  # Recommended_Cameras
        score += 1  # Availability


        scores.append(score)


    df["Priority_Score"] = scores


    # sort descending
    df = df.sort_values("Priority_Score", ascending=False)


    return df.head(10)


# ==========================
# OPTIONAL: DEFAULT WEIGHT TEMPLATE
# ==========================

def get_default_weights():

    return DEFAULT_WEIGHTS
