# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st
import pandas as pd


from customer_input import get_customer_inputs


from output import generate_output


from recommendation_engine import (
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


customer_tab, output_tab, database_tab, logic_tab = st.tabs(

[

"Customer Recommendation",

"Recommendation Output",

"Hardware Database Management",

"Recommendation Logic"

]

)



# =================================================
# CUSTOMER RECOMMENDATION TAB
# =================================================


with customer_tab:


    customer_data = get_customer_inputs()




    if st.button(
    
        "Generate Recommendation"
    
    ):
    
    

    
        st.session_state.customer_output = generate_output(
        
            customer_data
        
        )
        
        
        hardware_result = recommend_hardware(
        
            st.session_state.customer_output
        
        )
        
        
        st.session_state.hardware_result = hardware_result
   
        st.success(
    
            "Recommendation Generated Successfully"
    
        )
    
    
        # ==========================
        # SHOW RESULT IMMEDIATELY
        # ==========================
    
    
        customer_output = st.session_state.customer_output
    
    
    
        st.markdown(
    
        """
    
        <div class="result-card">
    
        <h3>
        System Requirement Analysis
        </h3>
    
        </div>
    
        """,
    
        unsafe_allow_html=True
    
        )
    
    
    
        output_table = {
    
    
        "Parameter":
    
        list(customer_output.keys()),
    
    
        "Value":
    
        list(customer_output.values())
    
    
    
        }
    
    
    
        st.table(
    
            output_table
    
        )



# =================================================
# RECOMMENDATION OUTPUT TAB
# =================================================


with output_tab:


    st.header(

        "Hardware Recommendation Output"

    )



    if "customer_output" in st.session_state:



        customer_output = st.session_state.customer_output



        st.markdown(

        """

        <div class="result-card">

        <h3>
        System Requirement Analysis
        </h3>

        </div>

        """,

        unsafe_allow_html=True

        )



        output_table = {


        "Parameter":

        [


        "Resolution Factor (Multiplier)",


        "AI Model Factor (Multiplier)",


        "Model Memory (GB)",


        "Camera Memory (GB)",


        "Safety Margin (GB)",


        "Workload Score (Score)",


        "VRAM Required (GB)",


        "CUDA Required (Cores)",


        "Tensor Required (Cores)",


        "FP16 Required (TFLOPS)",


        "INT8 Required (TOPS)",


        "Model Factor - FP16 (Multiplier)",


        "Processing Factor - CUDA (Multiplier)",


        "AI Model Complexity Factor - Tensor (Cores)",


        "Optimization Factor - INT8 (Multiplier)"


        ],



        "Value":

        [


        customer_output["Resolution Factor"],


        customer_output["Model Factor (FP16)"],


        customer_output["Model Memory (GB)"],


        customer_output["Camera Memory (GB)"],


        customer_output["Safety Margin (GB)"],


        customer_output["Workload Score"],


        customer_output["VRAM Required (GB)"],


        customer_output["CUDA Required"],


        customer_output["Tensor Required"],


        customer_output["FP16 Required"],


        customer_output["INT8 Required"],


        customer_output["Model Factor (FP16)"],


        customer_output["Processing Factor (CUDA)"],


        customer_output["AI Model Complexity Factor (Tensor)"],


        customer_output["Optimization Factor (INT8)"]


        ],



        "Type":

        [


        "Assumed / Lookup value",


        "Assumed / Lookup value",


        "Assumed value",


        "Calculated",


        "Assumed value",


        "Calculated",


        "Calculated",


        "Calculated",


        "Assumed / Lookup value",


        "Calculated",


        "Calculated",


        "Assumed / Lookup value",


        "Assumed value",


        "Assumed / Lookup value",


        "Assumed / Lookup value"


        ]


        }



        st.table(

            output_table

        )



    else:


        st.info(

            "Generate recommendation first from Customer Recommendation tab"

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


    show_recommendation_logic()
