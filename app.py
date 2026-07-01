# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st
import pandas as pd

from customer_input import get_customer_inputs

from output import generate_output

from recommendation_logic import show_recommendation_logic


from recommendation_engine import (
    recommend_hardware
)

from output import generate_output

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

customer_tab, database_tab, logic_tab, output_tab = st.tabs(

[

"Customer Recommendation",

"Hardware Database Management",

"Recommendation Logic",

"Recommendation Output"

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




        st.session_state.customer_output = generate_output(
        
            customer_data
        
        )

          
#============================================================
        # ==========================
        # DISPLAY CALCULATION OUTPUT
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
        
        [
        
        
        "Workload Score",
        
        
        "VRAM Required",
        
        
        "CUDA Required",
        
        
        "Tensor Required",
        
        
        "FP16 Required",
        
        
        "INT8 Required",
        
        
        "Processing Factor",
        
        
        "AI Model Complexity Factor",
        
        
        "Model Factor",
        
        
        "Optimization Factor"
        
        
        ],
        
        
        
        "Value":
        
        [
        
        
        customer_output["Workload Score"],
        
        
        customer_output["VRAM Required (GB)"],
        
        
        customer_output["CUDA Required"],
        
        
        customer_output["Tensor Required"],
        
        
        customer_output["FP16 Required"],
        
        
        customer_output["INT8 Required"],
        
        
        customer_output["Processing Factor (CUDA)"],
        
        
        customer_output["AI Model Complexity Factor (Tensor)"],
        
        
        customer_output["Model Factor (FP16)"],
        
        
        customer_output["Optimization Factor (INT8)"]
        
        
        ]
        
        }
        
        
        
        st.table(
        
            output_table
        
        )
#============================================================


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





# =================================================
# OUTPUT TAB
# =================================================


with output_tab:


    st.header(

        "Hardware Recommendation Output"

    )



    if "customer_output" in st.session_state:


        result = st.session_state.customer_output



        output_table = pd.DataFrame(

            {

                "Parameter":

                result.keys(),


                "Value":

                result.values()

            }

        )



        st.dataframe(

            output_table,

            use_container_width=True,

            hide_index=True

        )



    else:


        st.info(

            "In customer recommendation (tab) hit Generate recommendation (button) first after giving proper inputs"

        )
