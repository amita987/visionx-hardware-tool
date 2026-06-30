# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st

from recommendation_engine import (
    calculate_workload,
    recommend_gpu
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
        "720p",
        "1080p",
        "2K",
        "4K",
        "8K"
    ]
)



fps = st.selectbox(
    "Frames Per Second",
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
        "OpenCV",
        "YOLOv8",
        "YOLOv10",
        "Detectron2"
    ]
)



# ==========================
# INPUT TABLE
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


st.table(input_table)



# ==========================
# CALCULATION BUTTON
# ==========================


if st.button("Recommend Hardware"):



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
    # LOOKUP HARDWARE
    # ==========================


    gpu = recommend_gpu(
        workload
    )



    # ==========================
    # OUTPUT TABLE
    # ==========================


    st.subheader(
        "Recommendation"
    )



    output_table = {


    "Component":
    [
    "Workload Score",
    "GPU",
    "VRAM",
    "Power"
    ],


    "Recommendation":
    [
    workload,
    gpu["GPU"],
    gpu["VRAM"],
    gpu["Power"]
    ]

    }


    st.table(output_table)

# ==========================
# TABLE DISPLAY BUTTON
# ==========================

if st.button("Show Hardware Table"):


    # ==========================
    # FUTURE HARDWARE TABLE
    # ==========================


    st.subheader(
        "Hardware Reference Table"
    )


    hardware_table = {


        "Column 1":
        [
            "Data will come here"
        ],


        "Column 2":
        [
            "Data will come here"
        ]

    }


    st.table(
        hardware_table
    )
