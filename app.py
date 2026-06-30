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


.card {{

background-color:{SECONDARY_COLOR};

padding:20px;

border-radius:10px;

}}


.success-card {{

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
AI Vision System Hardware Advisor
</p>

</div>

""",

unsafe_allow_html=True

)



st.write("")



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
# CUSTOMER TAB
# =================================================


with customer_tab:


    st.subheader(

        "Camera & AI Requirements"

    )


    # ==========================
    # INPUT CARD
    # ==========================


    with st.container():


        col1,col2 = st.columns(2)



        with col1:


            camera_count = st.number_input(

                "Number of Cameras",

                min_value=1,

                value=10

            )



            resolution = st.selectbox(

                "Resolution",

                [

                "1080p",
                "2K",
                "4K",
                "8K"

                ]

            )



        with col2:


            fps = st.selectbox(

                "FPS",

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
    # RECOMMEND BUTTON
    # ==========================


    if st.button(

        "Generate Recommendation"

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


           
