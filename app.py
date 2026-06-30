# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st


# ==========================
# WEBSITE TITLE
# ==========================

st.title("VisionX Hardware Recommendation Tool")


# ==========================
# CUSTOMER INPUT SECTION
# ==========================

st.header("Customer Inputs")


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
        "OpenCV",
        "YOLOv8",
        "YOLOv10",
        "Detectron2"
    ]
)



# ==========================
# INPUT TABLE
# ==========================

st.subheader("Input Summary")


input_table = {

    "Parameter":
    [
        "Camera Count",
        "Resolution",
        "FPS",
        "AI Model"
    ],


    "Customer Value":
    [
        camera_count,
        resolution,
        fps,
        ai_model
    ]

}


st.table(input_table)



# ==========================
# OUTPUT TABLE
# ==========================

st.subheader("Hardware Recommendation")


output_table = {

    "Component":
    [
        "GPU",
        "VRAM",
        "Power"
    ],


    "Recommendation":
    [
        "Waiting for calculation",
        "-",
        "-"
    ]

}


st.table(output_table)
