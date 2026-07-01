# ==========================
# PRIORITY ANALYSIS ENGINE
# ==========================

import pandas as pd

# ==========================
# DEFAULT WEIGHTS
# ==========================

DEFAULT_WEIGHTS = {

    "VRAM_GB_weight": 1,
    "CUDA_Cores_weight": 1,
    "Tensor_Cores_weight": 1,
    "FP16_TFLOPS_weight": 1,
    "INT8_TOPS_weight": 1,
    "Price_weight": 1

}


# ==========================
# LOAD WEIGHTS
# ==========================

def get_weights(custom_weights=None):

    if custom_weights:
        return custom_weights

    return DEFAULT_WEIGHTS


# ==========================
# MAIN PRIORITY ENGINE
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


    results = []


    
    for _, row in df.iterrows():
    
        # ==========================
        # 0/1 SCORING
        # ==========================
    
        vram_score = 1 if row["VRAM_GB"] >= required_vram else 0
        cuda_score = 1 if row["CUDA_Cores"] >= required_cuda else 0
        tensor_score = 1 if row["Tensor_Cores"] >= required_tensor else 0
        fp16_score = 1 if row["FP16_TFLOPS"] >= required_fp16 else 0
        int8_score = 1 if row["INT8_TOPS"] >= required_int8 else 0
        price_score = 1 if row["Price"] <= max_price else 0
    
    
        # ==========================
        # WEIGHTED VALUES (THIS IS YOUR REQUEST)
        # ==========================
    
        vram = round(vram_score * w["VRAM_GB_weight"], 2)
        cuda = round(cuda_score * w["CUDA_Cores_weight"], 2)
        tensor = round(tensor_score * w["Tensor_Cores_weight"], 2)
        fp16 = round(fp16_score * w["FP16_TFLOPS_weight"], 2)
        int8 = round(int8_score * w["INT8_TOPS_weight"], 2)
        price = round(price_score * w["Price_weight"], 2)
    
    
        # ==========================
        # SUBJECTIVE (KEEP AS RAW OR 1)
        # ==========================
    
        hardware_type = 1
        manufacturer = 1
        model_name = 1
        cameras = 1
        availability = 1 if row["Availability"] == "Available" else 0
    
    
        # ==========================
        # TOTAL SCORE
        # ==========================
    
        total_score = (
            vram + cuda + tensor + fp16 + int8 + price +
            hardware_type + manufacturer + model_name + cameras + availability
        )
    
    
        results.append({
    
            "Hardware_Type": row["Hardware_Type"],
            "Manufacturer": row["Manufacturer"],
            "Model_Name": row["Model_Name"],
    
            # 👇 NOW SHOW WEIGHTED VALUES IN TABLE
            "VRAM_GB": vram,
            "CUDA_Cores": cuda,
            "Tensor_Cores": tensor,
            "FP16_TFLOPS": fp16,
            "INT8_TOPS": int8,
            "Price": price,
    
            "Recommended_Cameras": row["Recommended_Cameras"],
            "Availability": row["Availability"],
    
            "Total_Score": total_score
        })

    # ==========================
    # CREATE FINAL TABLE
    # ==========================
    
    result_df = pd.DataFrame(results)
    
    result_df = result_df.sort_values(
        "Total_Score",
        ascending=False
    ).head(10)

return result_df


# ==========================
# DEFAULT WEIGHTS EXPORT
# ==========================

def get_default_weights():

    return DEFAULT_WEIGHTS
