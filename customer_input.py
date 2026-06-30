# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st



# ==========================
# CUSTOMER INPUT FUNCTION
# ==========================


def get_customer_inputs():


    st.header(

        "Customer Configuration"

    )



    # ==========================
    # NUMBER OF CAMERAS
    # ==========================


    camera_count = st.number_input(

        "Number of Cameras",

        min_value=1,

        value=10

    )



    # ==========================
    # CAMERA RESOLUTION
    # ==========================


    resolution = st.selectbox(

        "Camera Resolution",

        [

            "1080p",

            "2K",

            "4K",

            "8K"

        ]

    )



    # ==========================
    # AI MODEL
    # ==========================


    ai_model = st.selectbox(

        "AI Model",

        [

            "YOLOv8",

            "YOLOv10",

            "Detectron"

        ]

    )



    # ==========================
    # FPS REQUIREMENT
    # ==========================


    fps = st.selectbox(

        "FPS Requirement",

        [

            15,

            30,

            60

        ]

    )



    # ==========================
    # LATENCY REQUIREMENT
    # ==========================


    latency = st.selectbox(

        "Latency Requirement",

        [

            "Real-time",

            "Normal"

        ]

    )



    # ==========================
    # RETURN CUSTOMER INPUTS
    # ==========================


    return {


        "camera_count": camera_count,


        "resolution": resolution,


        "ai_model": ai_model,


        "fps": fps,


        "latency": latency

    }
