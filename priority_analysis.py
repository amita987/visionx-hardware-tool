import pandas as pd


# =================================================
# DEFAULT WEIGHTS
# =================================================

DEFAULT_WEIGHTS = {

    "vram": 10,
    "cuda": 9,
    "tensor": 9,
    "fp16": 8,
    "int8": 7,
    "price": 5

}


# =================================================
# SCORING ENGINE
# =================================================

def compute_score(row, req, weights):


    score = 0


    # VRAM
    score += weights["vram"] * min(row["VRAM_GB"] / req["VRAM Required (GB)"], 1)


    # CUDA
    score += weights["cuda"] * min(row["CUDA_Cores"] / req["CUDA Required"], 1)


    # TENSOR
    score += weights["tensor"] * min(row["Tensor_Cores"] / req["Tensor Required"], 1)


    # FP16
    score += weights["fp16"] * min(row["FP16_TFLOPS"] / req["FP16 Required"], 1)


    # INT8
    score += weights["int8"] * min(row["INT8_TOPS"] / req["INT8 Required"], 1)


    # PRICE (lower better)
    score += weights["price"] * (1 / row["Price"])


    return score



# =================================================
# MAIN FUNCTION (USED BY APP.PY)
# =================================================

def get_priority_recommendation(customer_output, csv_path="hardware_database.csv"):


    df = pd.read_csv(csv_path)


    weights = DEFAULT_WEIGHTS


    df["Priority_Score"] = df.apply(


        lambda row: compute_score(row, customer_output, weights),


        axis=1


    )



    df = df.sort_values("Priority_Score", ascending=False)



    return df.head(10)
