# ==========================
# IMPORT LIBRARIES
# ==========================

import streamlit as st
import pandas as pd



# ==========================
# DATABASE FILE
# ==========================

DATABASE_FILE = "hardware_database.csv"



# ==========================
# LOAD DATABASE
# ==========================

def load_database():

    return pd.read_csv(
        DATABASE_FILE
    )



# ==========================
# SAVE DATABASE
# ==========================

def save_database(df):

    df.to_csv(

        DATABASE_FILE,

        index=False

    )



# ==========================
# HARDWARE MANAGEMENT PAGE
# ==========================

def hardware_management():


    st.subheader(
        "Hardware Database Management"
    )


    df = load_database()



    # ==========================
    # SESSION STATE
    # ==========================

    if "edit_row" not in st.session_state:

        st.session_state.edit_row = None



    if "add_hardware" not in st.session_state:

        st.session_state.add_hardware = False



    # ==========================
    # TABLE HEADER
    # ==========================

    st.write(
        "Hardware Inventory"
    )


    header = st.columns(
        [0.4,0.6,1,1,1.2,0.6,0.8,0.8,0.8,0.8,0.8,0.8,0.8]
    )


    headings = [
    
        "Row",
        "Action",
        "Type",
        "Manufacturer",
        "Model",
        "VRAM",
        "CUDA",
        "Tensor",
        "FP16",
        "INT8",
        "Power",
        "Min",
        "Max"
    
    ]


    for col, title in zip(header, headings):

        with col:

            st.markdown(
                f"**{title}**"
            )



    st.divider()



    # ==========================
    # TABLE ROWS
    # ==========================

    for index, row in df.iterrows():


        cols = st.columns(
            [0.4,0.6,1,1,1.2,0.6,0.8,0.8,0.8,0.8,0.8,0.8,0.8]
        )


        with cols[0]:

            st.write(index + 1)



        # EDIT BUTTON

        with cols[1]:


            if st.button(

                "✏️",

                key=f"edit_{index}"

            ):

                st.session_state.edit_row = index



        with cols[2]:

            st.write(
                row["Hardware_Type"]
            )


        with cols[3]:

            st.write(
                row["Manufacturer"]
            )


        with cols[4]:

            st.write(
                row["Model_Name"]
            )


        with cols[5]:

            st.write(
                row["VRAM_GB"]
            )


        with cols[6]:

            st.write(
                row["CUDA_Cores"]
            )


        with cols[7]:

            st.write(
                row["Tensor_Cores"]
            )


        with cols[8]:

            st.write(
                row["FP16_TFLOPS"]
            )


        with cols[9]:

            st.write(
                row["INT8_TOPS"]
            )


        with cols[10]:
        
            st.write(
                row["Power_W"]
            )
        
        
        with cols[11]:
        
            st.write(
                row["Workload_Min"]
            )
        
        
        with cols[12]:
        
            st.write(
                row["Workload_Max"]
            )


        # ==========================
        # EDIT ONLY SELECTED ROW
        # ==========================


        if st.session_state.edit_row == index:


            st.markdown(

            """

            <div style="
            background-color:#E8F5E9;
            padding:15px;
            border-radius:10px;
            ">

            <h3>
            Editing Hardware
            </h3>

            </div>

            """,

            unsafe_allow_html=True

            )


            edited = {}


            edit_cols = st.columns(4)



            for i,column in enumerate(df.columns):


                with edit_cols[i % 4]:


                    edited[column] = st.text_input(

                        column,

                        value=str(row[column]),

                        key=f"edit_{index}_{column}"

                    )



            save_col, cancel_col = st.columns(2)



            with save_col:


                if st.button(

                    "✅ Update",

                    key=f"save_{index}"

                ):


                    for column in df.columns:


                        df.loc[index,column] = edited[column]



                    save_database(df)


                    st.success(
                        "Updated Successfully"
                    )


                    st.session_state.edit_row = None


                    st.rerun()



            with cancel_col:


                if st.button(

                    "❌ Cancel",

                    key=f"cancel_{index}"

                ):


                    st.session_state.edit_row = None


                    st.rerun()



        st.divider()




    # ==========================
    # ADD HARDWARE
    # ==========================


    if st.button(

        "➕ Add New Hardware"

    ):

        st.session_state.add_hardware = True




    if st.session_state.add_hardware:


        st.subheader(
            "Add New Hardware"
        )


        new_row = {}



        cols = st.columns(4)



        for i,column in enumerate(df.columns):


            with cols[i % 4]:


                new_row[column] = st.text_input(

                    column,

                    key=f"new_{column}"

                )



        add_col, cancel_col = st.columns(2)



        with add_col:


            if st.button(

                "💾 Save Hardware"

            ):


                df.loc[len(df)] = new_row


                save_database(df)


                st.session_state.add_hardware = False


                st.rerun()



        with cancel_col:


            if st.button(

                "❌ Cancel Add"

            ):


                st.session_state.add_hardware = False


                st.rerun()
