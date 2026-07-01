# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st
import pandas as pd



# ==========================
# RECOMMENDATION LOGIC PAGE
# ==========================


def show_recommendation_logic():


    st.header(

        "Hardware Recommendation Logic"

    )



    # =================================================
    # HARDWARE DATABASE LOGIC TABLE
    # =================================================


    logic_table = [


        [

            "Hardware Type",

            "Workload type (AI Vision / Gaming / Server etc.)",

            "Decide component category needed",

            "AI Vision workload → GPU required",

            "Select GPU hardware"

        ],


        [

            "Manufacturer",

            "Optional preference",

            "Filter database by vendor",

            "NVIDIA only",

            "Keep matching vendor"

        ],


        [

            "Model Name",

            "None",

            "Final output from lookup table",

            "RTX 4060",

            "Return selected model"

        ],


        [

            "VRAM (GB)",

            "Camera count, resolution, AI model",

            "Calculate memory requirement",

            "Model Memory + Camera Buffer + Safety Margin",

            "VRAM ≥ Required VRAM"

        ],


        [

            "CUDA Cores",

            "Camera count, FPS, resolution",

            "Estimate processing workload",

            "Camera × FPS × Resolution Factor",

            "CUDA ≥ Required CUDA"

        ],


        [

            "Tensor Cores",

            "AI Model",

            "AI acceleration requirement",

            "YOLOv10 needs more Tensor capacity",

            "Tensor ≥ Required Tensor"

        ],


        [

            "FP16 Performance",

            "FPS requirement, AI model",

            "Estimate inference speed",

            "Higher FPS → Higher TFLOPS",

            "FP16 ≥ Required TFLOPS"

        ],


        [

            "INT8 Performance",

            "AI model, camera count, FPS",

            "Optimized inference need",

            "Large cameras increase INT8 need",

            "INT8 ≥ Required TOPS"

        ],


        [

            "Power Consumption",

            "None",

            "System planning",

            "GPU Power + CPU + Margin",

            "Select PSU"

        ],


        [

            "Minimum Workload Score",

            "Camera count, FPS, resolution",

            "Database lower limit",

            "RTX4060 starts at 500",

            "Workload ≥ Minimum"

        ],


        [

            "Maximum Workload Score",

            "Camera count, FPS, resolution",

            "Database upper limit",

            "RTX4060 supports 1500",

            "Workload ≤ Maximum"

        ]


    ]



    logic_df = pd.DataFrame(

        logic_table,

        columns=[

            "Hardware Database Column",

            "Customer Input Required",

            "Backend Calculation / Logic",

            "Example Calculation",

            "Selection Rule"

        ]

    )



    st.dataframe(

        logic_df,

        use_container_width=True,

        hide_index=True

    )





    # =================================================
    # CALCULATION LOGIC TABLE
    # =================================================


    st.subheader(

        "Backend Calculation Logic"

    )



    calculation_table = [


        [

            "Workload Score",

            "Camera Count × FPS × Resolution Factor × AI Model Factor"

        ],


        [

            "VRAM Required",

            "Model Memory + Camera Memory + Safety Margin"

        ],


        [

            "CUDA Requirement",

            "Workload Score × Processing Factor"

        ],


        [

            "Tensor Requirement",

            "AI Model Complexity Factor"

        ],


        [

            "FP16 Requirement",

            "FPS × Camera Count × Model Factor"

        ],


        [

            "INT8 Requirement",

            "Workload Score × Optimization Factor"

        ]

    ]



    calculation_df = pd.DataFrame(

        calculation_table,

        columns=[

            "Calculation",

            "Formula"

        ]

    )



    st.dataframe(

        calculation_df,

        use_container_width=True,

        hide_index=True

    )





    # =================================================
    # HARDWARE SELECTION PROCESS
    # =================================================


    st.subheader(

        "Hardware Selection Process"

    )



    selection_table = [


        ["1","Remove unavailable hardware"],

        ["2","Remove over-budget hardware"],

        ["3","Check workload range"],

        ["4","Check VRAM"],

        ["5","Check CUDA"],

        ["6","Check Tensor cores"],

        ["7","Check FP16"],

        ["8","Check INT8"],

        ["9","Rank remaining hardware"],

        ["10","Recommend best match"]

    ]



    selection_df = pd.DataFrame(

        selection_table,

        columns=[

            "Step",

            "Check"

        ]

    )



    st.dataframe(

        selection_df,

        use_container_width=True,

        hide_index=True

    )
