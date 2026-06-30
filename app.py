# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st
import pandas as pd

from recommendation_engine import (
    calculate_workload,
    recommend_hardware
)

from color_config import (
    PRIMARY_COLOR,
    SECONDARY_COLOR,
    SUCCESS_COLOR
)



# ==========================
# PAGE SETTINGS
# ==========================

st.set_page_config(

    page_title="VisionX Hardware Tool",

    layout="wide"

)



# ==========================
# CUSTOM STYLE SECTION
# ==========================

st.markdown(

f"""

<style>

.main-header {{

background-color:{PRIMARY_COLOR};

padding:20px;

border-radius:10px;

color:white;

}}


.result-card {{

background-color:{SUCCESS_COLOR};

padding:20px;

border-radius:10px;

}}


</style>

""",

unsafe_allow_html=True

)



# ==========================
# VISIONX HEADER
# ==========================


st.markdown(

"""

<div class="main-header">

<h1>
VisionX Hardware Recommendation Tool
</h1>

<p>
AI Vision System Hardware Advisor - Version 1.0
</p>

</div>

""",

unsafe_allow_html=True

)



# ==========================
# CREATE TABS
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
    # INPUT SECTION
    # ==========================


    col1, col2 = st.columns(2)



    with col1:


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



    with col2:


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



    st.divider()



    # ==========================
    # RECOMMENDATION BUTTON
    # ==========================


    if st.button(

        "Generate Recommendation"

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


        else:


            # ==========================
            # OUTPUT CARD
            # ==========================


            st.markdown(

            """

            <div class="result-card">

            <h3>
            Recommended Hardware
            </h3>

            </div>

            """,

            unsafe_allow_html=True

            )



            # ==========================
            # OUTPUT TABLE
            # ==========================


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


    from hardware_manager import hardware_management


    hardware_management()



    # ==========================
    # DISPLAY TABLE
    # ==========================


    st.dataframe(

        hardware_data,

        use_container_width=True

    )
