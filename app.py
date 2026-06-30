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
# PAGE CONFIGURATION
# ==========================

st.set_page_config(

    page_title="VisionX Hardware Tool",

    layout="wide"

)



# ==========================
# VISIONX HEADER
# ==========================

st.title(
    "VisionX Hardware Recommendation Tool"
)


st.write(
    "AI Vision System Hardware Advisor - Version 1.0"
)



# ==========================
# CREATE TOP TABS
# ==========================

customer_tab, database_tab = st.tabs(

    [

        "Customer Recommendation",

        "Hardware Database Management"

    ]

)



# =================================================
# CUSTOMER RECOMMENDATION TAB
# =================================================


with customer_tab:


    st.header(
        "Customer Configuration"
    )


    # ==========================
    # CUSTOMER INPUTS
    # ==========================


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

            "YOLOv8",
            "YOLOv10",
            "Detectron2"

        ]

    )



    # ==========================
    # RECOMMEND BUTTON
    # ==========================


    if st.button(

        "Recommend Hardware"

    ):


        workload = calculate_workload(

            camera_count,

            fps,

            resolution,

            ai_model

        )



        gpu = recommend_hardware(

            workload

        )



        if gpu is None:


            st.error(

                "No suitable hardware found"

            )


        else:


            st.subheader(

                "Recommended Hardware"

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



            "Value":

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





# =================================================
# HARDWARE DATABASE MANAGEMENT TAB
# =================================================


with database_tab:


    st.header(

        "Hardware Database Management"

    )


    st.write(

        "Manage hardware reference database"

    )



    # ==========================
    # LOAD DATABASE
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
