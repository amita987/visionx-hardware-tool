# ==========================
# IMPORT LIBRARIES
# ==========================

import pandas as pd



# ==========================
# DATABASE FILE
# ==========================

DATABASE_FILE = "hardware_database.csv"



# ==========================
# LOAD HARDWARE DATABASE
# ==========================

def load_hardware_database():


    return pd.read_csv(

        DATABASE_FILE

    )





# ==========================
# HARDWARE TYPE LOGIC
# ==========================


def check_hardware_type(df):


    return df[

        df["Hardware_Type"] == "GPU"

    ]





# ==========================
# MANUFACTURER FILTER
# ==========================


def filter_manufacturer(df, vendor=None):


    if vendor is None:


        return df



    return df[

        df["Manufacturer"] == vendor

    ]





# ==========================
# MAIN RECOMMENDATION ENGINE
# ==========================


def recommend_hardware(

        calculation_output,

        vendor=None

):



    df = load_hardware_database()



    # ==========================
    # 1. HARDWARE TYPE
    # ==========================


    df = check_hardware_type(df)




    # ==========================
    # 2. MANUFACTURER
    # ==========================


    df = filter_manufacturer(

        df,

        vendor

    )




    # ==========================
    # 3. VRAM CHECK
    # ==========================


    df = df[

        df["VRAM_GB"]

        >=

        calculation_output["VRAM Required (GB)"]

    ]




    # ==========================
    # 4. CUDA CHECK
    # ==========================


    df = df[

        df["CUDA_Cores"]

        >=

        calculation_output["CUDA Required"]

    ]




    # ==========================
    # 5. TENSOR CHECK
    # ==========================


    df = df[

        df["Tensor_Cores"]

        >=

        calculation_output["Tensor Required"]

    ]




    # ==========================
    # 6. FP16 CHECK
    # ==========================


    df = df[

        df["FP16_TFLOPS"]

        >=

        calculation_output["FP16 Required"]

    ]




    # ==========================
    # 7. INT8 CHECK
    # ==========================


    df = df[

        df["INT8_TOPS"]

        >=

        calculation_output["INT8 Required"]

    ]




    # ==========================
    # 8. WORKLOAD RANGE CHECK
    # ==========================


    df = df[

        (df["Workload_Min"]

        <=

        calculation_output["Workload Score"])

        &

        (df["Workload_Max"]

        >=

        calculation_output["Workload Score"])

    ]




    # ==========================
    # FINAL RESULT
    # ==========================


    if len(df) == 0:


        return None



    # Pick first suitable hardware


    recommendation = df.iloc[0]



    return recommendation
