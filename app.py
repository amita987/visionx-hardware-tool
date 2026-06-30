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

customer_tab, database_tab, logic_tab = st.tabs(

[

"Customer Recommendation",

"Hardware Database Management",

"Recommendation Logic"

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
# =================================================
# RECOMMENDATION LOGIC TAB
# =================================================


with logic_tab:


    st.header(

        "Hardware Recommendation Logic"

    )


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

            "YOLOv10 needs more Tensor capacity than YOLOv8",

            "Tensor ≥ Required Tensor"

        ],

        [

            "FP16 Performance",

            "FPS requirement, AI model",

            "Estimate inference speed need",

            "Higher FPS → Higher TFLOPS required",

            "FP16 ≥ Required TFLOPS"

        ],

        [

            "INT8 Performance",

            "AI model, camera count, FPS",

            "Estimate optimized inference need",

            "Large camera count increases INT8 need",

            "INT8 ≥ Required TOPS"

        ],

        [

            "Power Consumption (W)",

            "None",

            "Used for system design",

            "GPU 115W + CPU + margin",

            "Select PSU/cooling"

        ],

        [

            "Minimum Workload Score",

            "Camera count, FPS, resolution",

            "Lower boundary stored in database",

            "RTX4060 starts at workload 500",

            "Workload ≥ Minimum"

        ],

        [

            "Maximum Workload Score",

            "Camera count, FPS, resolution",

            "Upper boundary stored in database",

            "RTX4060 supports up to workload 1500",

            "Workload ≤ Maximum"

        ],

        [

            "Recommended Camera Count",

            "Camera count",

            "Customer-friendly conversion",

            "RTX4060 → 20 cameras",

            "Display to customer"

        ],

        [

            "Max Resolution Support",

            "Camera resolution",

            "Convert resolution requirement",

            "4K = higher requirement than 1080p",

            "Required Resolution ≤ Supported Resolution"

        ],

        [

            "Max FPS Support",

            "FPS input",

            "Compare real-time requirement",

            "Customer needs 60 FPS",

            "Required FPS ≤ Hardware FPS"

        ],

        [

            "AI Model Compatibility",

            "AI model selection",

            "Match supported models",

            "YOLOv8 supported",

            "AI model must exist in list"

        ],

        [

            "Price",

            "Customer budget",

            "Budget filtering",

            "Budget $500",

            "Price ≤ Budget"

        ],

        [

            "Availability",

            "None / admin data",

            "Inventory check",

            "Available",

            "Remove unavailable products"

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
    # CUSTOMER INPUT REFERENCE TABLE
    # =================================================
    
    
    st.subheader(
    
        "Customer Input Requirements"
    
    )
    
    
    
    input_table = [
    
    
        [
    
            "Number of Cameras",
    
            "20",
    
            "VRAM, CUDA, workload"
    
        ],
    
    
        [
    
            "Camera Resolution",
    
            "4K",
    
            "VRAM, workload"
    
        ],
    
    
        [
    
            "FPS Requirement",
    
            "30 FPS",
    
            "CUDA, FP16, workload"
    
        ],
    
    
        [
    
            "AI Model",
    
            "YOLOv8",
    
            "Tensor, compatibility"
    
        ],
    
    
        [
    
            "Budget",
    
            "$500",
    
            "Price filtering"
    
        ],
    
    
        [
    
            "Vendor Preference",
    
            "NVIDIA",
    
            "Manufacturer filtering"
    
        ],
    
    
        [
    
            "Latency Requirement",
    
            "Real-time",
    
            "FP16/INT8 requirement"
    
        ]
    
    ]
    
    
    
    input_df = pd.DataFrame(
    
        input_table,
    
        columns=[
    
            "Input Field",
    
            "Example",
    
            "Used For"
    
        ]
    
    )
    
    
    
    st.dataframe(
    
        input_df,
    
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
    # HARDWARE SELECTION PROCESS TABLE
    # =================================================
    
    
    st.subheader(
    
        "Hardware Selection Process"
    
    )
    
    
    
    selection_table = [
    
    
        [
    
            "1",
    
            "Remove unavailable hardware"
    
        ],
    
    
        [
    
            "2",
    
            "Remove over-budget hardware"
    
        ],
    
    
        [
    
            "3",
    
            "Check workload range"
    
        ],
    
    
        [
    
            "4",
    
            "Check VRAM"
    
        ],
    
    
        [
    
            "5",
    
            "Check CUDA"
    
        ],
    
    
        [
    
            "6",
    
            "Check Tensor cores"
    
        ],
    
    
        [
    
            "7",
    
            "Check FP16"
    
        ],
    
    
        [
    
            "8",
    
            "Check INT8"
    
        ],
    
    
        [
    
            "9",
    
            "Rank remaining hardware"
    
        ],
    
    
        [
    
            "10",
    
            "Recommend best match"
    
        ]
    
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
    # =================================================
    # HARDWARE DATABASE COLUMN REFERENCE TABLE
    # =================================================
    
    
    st.subheader(
    
        "Hardware Database Column Reference"
    
    )
    
    
    
    hardware_column_table = [
    
    
        [
    
            "Hardware Type",
    
            "GPU",
    
            "To identify the hardware category"
    
        ],
    
    
        [
    
            "Manufacturer",
    
            "NVIDIA",
    
            "To identify vendor"
    
        ],
    
    
        [
    
            "Model Name",
    
            "RTX 4060",
    
            "Final recommended hardware name"
    
        ],
    
    
        [
    
            "VRAM (GB)",
    
            "8",
    
            "Determines how many AI models/streams can fit"
    
        ],
    
    
        [
    
            "CUDA Cores",
    
            "3072",
    
            "Measures parallel processing capability"
    
        ],
    
    
        [
    
            "Tensor Cores",
    
            "96",
    
            "AI acceleration capability"
    
        ],
    
    
        [
    
            "FP16 Performance",
    
            "15 TFLOPS",
    
            "Deep learning inference speed"
    
        ],
    
    
        [
    
            "INT8 Performance",
    
            "242 TOPS",
    
            "Optimized AI inference performance"
    
        ],
    
    
        [
    
            "Power Consumption (W)",
    
            "115W",
    
            "Power supply and thermal planning"
    
        ],
    
    
        [
    
            "Minimum Workload Score",
    
            "500",
    
            "Lowest workload this hardware should handle"
    
        ],
    
    
        [
    
            "Maximum Workload Score",
    
            "1500",
    
            "Highest recommended workload"
    
        ],
    
    
        [
    
            "Recommended Camera Count",
    
            "20",
    
            "Easy customer-facing estimate"
    
        ],
    
    
        [
    
            "Max Resolution Support",
    
            "4K",
    
            "Highest camera resolution supported"
    
        ],
    
    
        [
    
            "Max FPS Support",
    
            "30",
    
            "Maximum real-time frame rate"
    
        ],
    
    
        [
    
            "AI Model Compatibility",
    
            "YOLOv8, YOLOv10",
    
            "Checks AI model suitability"
    
        ],
    
    
        [
    
            "Price",
    
            "$299",
    
            "Budget calculation"
    
        ],
    
    
        [
    
            "Availability",
    
            "Available",
    
            "Product availability tracking"
    
        ]
    
    ]
    
    
    
    hardware_column_df = pd.DataFrame(
    
    
        hardware_column_table,
    
    
        columns=[
    
    
            "Column Name",
    
            "Example",
    
            "Why We Need It"
    
    
        ]
    
    
    )
    
    
    
    st.dataframe(
    
        hardware_column_df,
    
        use_container_width=True,
    
        hide_index=True
    
    )
