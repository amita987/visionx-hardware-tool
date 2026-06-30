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
# HARDWARE TABLE + INLINE EDIT
# ==========================

def hardware_management():

    st.subheader("Hardware Database Management")

    df = load_database()

    # ==========================
    # INIT SESSION STATE
    # ==========================

    if "edit_row" not in st.session_state:
        st.session_state.edit_row = None


    
    # ==========================
    # HARDWARE TABLE WITH HEADERS
    # ==========================
    
    st.write("Hardware Inventory")
    
    
    # ==========================
    # TABLE HEADER
    # ==========================
    
    header = st.columns(
        [0.5,1,2,2,2,1,1,1,1]
    )
    
    
    headers = [
    
        "Row",
        "Action",
        "Hardware Type",
        "Manufacturer",
        "Model Name",
        "VRAM",
        "CUDA Cores",
        "Tensor Cores",
        "FP16"
    
    ]
    
    
    for col, text in zip(header, headers):
    
        with col:
            st.markdown(
                f"**{text}**"
            )
    
    
    
    st.divider()
    
    
    
    # ==========================
    # TABLE ROWS
    # ==========================
    
    for index, row in df.iterrows():
    
    
        cols = st.columns(
            [0.5,1,2,2,2,1,1,1,1]
        )
    
    
        with cols[0]:
            st.write(index + 1)
    
    
    
        with cols[1]:
    
            if st.button(
                "✏️",
                key=f"edit_{index}"
            ):
    
                st.session_state.edit_row = index
    
    
    
        with cols[2]:
            st.write(row["Hardware_Type"])
    
    
        with cols[3]:
            st.write(row["Manufacturer"])
    
    
        with cols[4]:
            st.write(row["Model_Name"])
    
    
        with cols[5]:
            st.write(row["VRAM_GB"])
    
    
        with cols[6]:
            st.write(row["CUDA_Cores"])
    
    
        with cols[7]:
            st.write(row["Tensor_Cores"])
    
    
        with cols[8]:
            st.write(row["FP16_TFLOPS"])
    
    
    
        st.divider()


    # ==========================
    # EDIT PANEL
    # ==========================


    if st.session_state.get(

        "edit_row",

        None

    ) is not None:



        index = st.session_state.edit_row


        row = df.loc[index]



        # ==========================
        # GREEN EDIT AREA
        # ==========================


        st.markdown(

        """

        <div style="
            background-color:#E8F5E9;
            padding:15px;
            border-radius:10px;
            margin-top:10px;
        ">
            <h3 style="margin:0;">
                Editing Hardware Record
            </h3>
        </div>
        """,

        unsafe_allow_html=True

        )



        updated_values = {}



        # ==========================
        # HORIZONTAL INPUT FIELDS
        # ==========================


        cols = st.columns(4)



        for i,column in enumerate(df.columns):


            with cols[i % 4]:


                updated_values[column] = st.text_input(

                    column,

                    value=str(row[column]),

                    key=f"edit_{column}_{index}"

                )



        st.write("")



        # ==========================
        # UPDATE / CANCEL BUTTONS
        # ==========================


        update_col, cancel_col = st.columns(

            [1,1]

        )



        with update_col:


            if st.button(

                "✅ Update",

                key=f"update_{index}"

            ):



                for column in df.columns:


                    df.loc[index,column] = updated_values[column]



                save_database(df)



                st.success(

                    "Hardware Updated Successfully"

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



    # ==========================
    # ADD HARDWARE BUTTON
    # ==========================


    st.divider()



    if st.button(

        "➕ Add New Hardware"

    ):


        st.session_state.add_hardware = True




    # ==========================
    # ADD HARDWARE FORM
    # ==========================


    if st.session_state.get(

        "add_hardware",

        False

    ):


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



        st.write("")



        save_col, cancel_col = st.columns(

            [1,1]

        )



        with save_col:


            if st.button(

                "💾 Update Hardware Database"

            ):



                df.loc[len(df)] = new_row



                save_database(df)



                st.success(

                    "New Hardware Added"

                )



                st.session_state.add_hardware = False


                st.rerun()



        with cancel_col:


            if st.button(

                "❌ Cancel Add"

            ):


                st.session_state.add_hardware = False


                st.rerun()
