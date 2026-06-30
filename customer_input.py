# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st



# ==========================
# CUSTOMER INPUT FUNCTION
# ==========================


def get_customer_inputs():


    st.subheader(

        "Customer System Configuration"

    )



    # ==========================
    # ROW 1
    # ==========================


    col1, col2 = st.columns(2)



    with col1:


        camera_count = st.number_input(

            "📷 Number of Cameras",

            min_value=1,

            value=10

        )



    with col2:


        resolution = st.selectbox(

            "🎥 Camera Resolution",

            [

                "1080p",

                "2K",

                "4K",

                "8K"

            ]

        )



    st.divider()



    # ==========================
    # ROW 2
    # ==========================


    col3, col4 = st.columns(2)



    with col3:


        ai_model = st.selectbox(

            "🤖 AI Model",

            [

                "YOLOv8",

                "YOLOv10",

                "Detectron"

            ]

        )



    with col4:


        fps = st.selectbox(

            "⚡ FPS Requirement",

            [

                15,

                30,

                60

            ]

        )



    st.divider()



    # ==========================
    # ROW 3
    # ==========================


    col5, col6 = st.columns(2)



    with col5:


        latency = st.selectbox(

            "⏱ Latency Requirement",

            [

                "Real-time",

                "Normal"

            ]

        )



    with col6:


        st.info(

            """

            System will calculate:

            • Workload Score

            • VRAM Requirement

            • CUDA Requirement

            • AI Processing Need

            """

        )



    st.divider()



    # ==========================
    # RETURN VALUES
    # ==========================


    return {


        "camera_count": camera_count,


        "resolution": resolution,


        "ai_model": ai_model,


        "fps": fps,


        "latency": latency

    }
