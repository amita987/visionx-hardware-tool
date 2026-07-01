import pandas as pd


# ==========================
# PRIORITY SCORING ENGINE
# ==========================

def compute_priority_score(row, requirements, weights):


    score = 0


    # ==========================
    # VRAM SCORE
    # ==========================

    if row["VRAM_GB"] >= requirements["vram_required"]:

        score += weights["vram"] * 1

    else:

        score += weights["vram"] * (row["VRAM_GB"] / requirements["vram_required"])



    # ==========================
    # CUDA SCORE
    # ==========================

    if row["CUDA_Cores"] >= requirements["cuda_required"]:

        score += weights["cuda"] * 1

    else:

        score += weights["cuda"] * (row["CUDA_Cores"] / requirements["cuda_required"])



    # ==========================
    # TENSOR SCORE
    # ==========================

    if row["Tensor_Cores"] >= requirements["tensor_required"]:

        score += weights["tensor"] * 1

    else:

        score += weights["tensor"] * 0.5



    # ==========================
    # FP16 SCORE
    # ==========================

    if row["FP16_TFLOPS"] >= requirements["fp16_required"]:

        score += weights["fp16"] * 1

    else:

        score += weights["fp16"] * (row["FP16_TFLOPS"] / requirements["fp16_required"])



    # ==========================
    # INT8 SCORE
    # ==========================

    if row["INT8_TOPS"] >= requirements["int8_required"]:

        score += weights["int8"] * 1

    else:

        score += weights["int8"] * (row["INT8_TOPS"] / requirements["int8_required"])



    # ==========================
    # PRICE PENALTY (LOWER IS BETTER)
    # ==========================

    score += weights["price"] * (1 / row["Price"])



    return score



# ==========================
# MAIN FUNCTION
# ==========================

def get_priority_recommendation(hardware_df, requirements, weights):


    hardware_df["Priority_Score"] = hardware_df.apply(


        lambda row: compute_priority_score(row, requirements, weights),


        axis=1


    )



    sorted_df = hardware_df.sort_values(


        by="Priority_Score",


        ascending=False


    )



    return sorted_df.head(10)
