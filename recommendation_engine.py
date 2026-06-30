# ==========================
# IMPORT LIBRARIES
# ==========================

import pandas as pd



# ==========================
# LOAD HARDWARE DATABASE
# ==========================

def load_hardware_database():

    database = pd.read_csv(
        "hardware_database.csv"
    )

    return database



# ==========================
# RESOLUTION CALCULATION
# ==========================

def get_resolution_factor(resolution):


    if resolution == "720p":
        return 1


    elif resolution == "1080p":
        return 2


    elif resolution == "2K":
        return 3


    elif resolution == "4K":
        return 5


    elif resolution == "8K":
        return 8



# ==========================
# AI MODEL CALCULATION
# ==========================

def get_model_factor(ai_model):


    if ai_model == "OpenCV":
        return 1


    elif ai_model == "YOLOv8":
        return 3


    elif ai_model == "YOLOv10":
        return 4


    elif ai_model == "Detectron2":
        return 5



# ==========================
# WORKLOAD CALCULATION
# ==========================

def calculate_workload(
        camera_count,
        fps,
        resolution,
        ai_model
):


    resolution_factor = get_resolution_factor(
        resolution
    )


    model_factor = get_model_factor(
        ai_model
    )


    workload = (

        camera_count
        *
        fps
        *
        resolution_factor
        *
        model_factor

    )


    return workload



# ==========================
# HARDWARE LOOKUP
# ==========================

def recommend_gpu(workload):


    database = load_hardware_database()


    for index,row in database.iterrows():


        if (

            workload >= row["Workload_Min"]

            and

            workload <= row["Workload_Max"]

        ):

            return row



    return None
