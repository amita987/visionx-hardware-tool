# ==========================
# IMPORT REQUIRED LIBRARIES
# ==========================

import streamlit as st
import pandas as pd

from recommendation_engine import (
    calculate_workload,
    recommend_hardware
)



# ==========================
# WEBSITE TITLE
# ==========================

st.title(
    "VisionX Hardware Recommendation Tool"
)



# ==========================
# CUSTOMER INPUT SECTION
# ==========================

st.header(
    "Customer Inputs"
)



camera_count = st.number_input(

    "Number of Cameras",

    min_value=1,

    value=10

)



resolution = st.selectbox(

    "Camera Resolution",

    [

        "1080p",
        "2K",
        "4K",
        "8K"

    ]

)



fps = st.selectbox(

    "Frames Per Second (FPS)",

    [

        5,
        15,
        30,
        60

    ]

)



ai_model = st.selectbox(

    "AI Model",

    [

        "YOLOv8",
        "YOLOv10",
        "Detectron2"

    ]

)



# ==========================
# DISPLAY INPUT TABLE
# ==========================


st.subheader(
    "Input Summary"
)



input_table = {


"Parameter":

[

"Camera Count",
"Resolution",
"FPS",
"AI Model"

],



"Value":

[

camera_count,
resolution,
fps,
ai_model

]


}



st.table(
    input_table
)



# ==========================
# HARDWARE RECOMMENDATION BUTTON
# ==========================


if st.button(
    "Recommend Hardware"
):


    # ==========================
    # CALCULATE WORKLOAD
    # ==========================


    workload = calculate_workload(

        camera_count,

        fps,

        resolution,

        ai_model

    )



    # ==========================
    # FIND HARDWARE
    # ==========================


    gpu = recommend_hardware(

        workload

    )



    # ==========================
    # CHECK RESULT
    # ==========================


    if gpu is None:


        st.error(

            "No suitable hardware found"

        )


        st.stop()



    # ==========================
    # OUTPUT TABLE
    # ==========================


    st.subheader(

        "Hardware Recommendation"

    )



    output_table = {


    "Component":

    [

    "Workload Score",

    "Hardware Type",

    "Manufacturer",

    "Model Name",

    "VRAM",

    "Power"

    ],



    "Recommendation":

    [

    workload,

    gpu["Hardware_Type"],

    gpu["Manufacturer"],

    gpu["Model_Name"],

    gpu["VRAM_GB"],

    gpu["Power_W"]

    ]



    }



    st.table(

        output_table

    )





# ==========================
# HARDWARE DATABASE TABLE
# ==========================


st.divider()



st.header(

    "Hardware Reference Database"

)



if st.button(

    "Show Hardware Table"

):


    # ==========================
    # LOAD CSV DATABASE
    # ==========================


    hardware_data = pd.read_csv(

        "hardware_database.csv"

    )



    # ==========================
    # DISPLAY DATABASE
    # ==========================


    st.dataframe(

        hardware_data,

        use_container_width=True

    )
