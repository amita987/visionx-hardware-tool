# ==========================
# IMPORT LIBRARIES
# ==========================

import pandas as pd



# ==========================
# LOAD HARDWARE DATABASE
# ==========================

def load_hardware_database():

    hardware = pd.read_csv(
        "hardware_database.csv"
    )

    return hardware



# ==========================
# RESOLUTION FACTOR
# ==========================

def resolution_factor(resolution):

    factors = {

        "1080p": 1,
        "2K": 2,
        "4K": 3,
        "8K": 5

    }


    return factors.get(
        resolution,
        1
    )



# ==========================
# AI MODEL FACTOR
# ==========================

def model_factor(model):

    factors = {

        "YOLOv8": 2,
        "YOLOv10": 3,
        "Detectron2": 4

    }


    return factors.get(
        model,
        1
    )



# ==========================
# WORKLOAD CALCULATION
# ==========================

def calculate_workload(
    cameras,
    fps,
    resolution,
    model
):


    workload = (

        cameras
        *
        fps
        *
        resolution_factor(resolution)
        *
        model_factor(model)

    )


    return workload



# ==========================
# HARDWARE RECOMMENDATION
# ==========================

def recommend_hardware(workload):


    hardware = load_hardware_database()



    for index,row in hardware.iterrows():


        if (

            workload >= row["Workload_Min"]

            and

            workload <= row["Workload_Max"]

        ):


            return row



    return None
