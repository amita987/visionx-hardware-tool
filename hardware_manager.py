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
    # SESSION SETTINGS
    # ==========================

    if "edit_row" not in st.session_state:

        st.session_state.edit_row = None



    if "add_hardware" not in st.session_state:

        st.session_state.add_hardware = False



    # ==========================
    # HARDWARE TABLE DISPLAY
    # ==========================


    st.write(
        "Current Hardware Database"
    )



    st.dataframe(

        df,

        use_container_width=True,

        hide_index=True

    )



    # ==========================
    # SELECT HARDWARE TO EDIT
    # ==========================


    st.divider()



    st.subheader(
        "Edit Hardware"
    )



    edit_index = st.selectbox(

        "Select Hardware",

        options=range(len(df)),

        format_func=lambda x:
        df.loc[x,"Model_Name"]

    )



    if st.button(

        "✏️ Edit"

    ):


        st.session_state.edit_row = edit_index





    # ==========================
    # EDIT SECTION
    # ==========================


    if st.session_state.edit_row is not None:


        index = st.session_state.edit_row


        row = df.loc[index]



        # ==========================
        # GREEN BACKGROUND
        # ==========================


        st.markdown(

        """

        <div style="

        background-color:#E8F5E9;

        padding:20px;

        border-radius:10px;

        ">

        <h3>
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


        update_col, cancel_col = st.columns(2)



        with update_col:


            if st.button(

                "✅ Update",

                key="update_button"

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

                key="cancel_button"

            ):


                st.session_state.edit_row = None


                st.rerun()





    # ==========================
    # ADD NEW HARDWARE BUTTON
    # ==========================


    st.divider()



    if st.button(

        "➕ Add New Hardware"

    ):


        st.session_state.add_hardware = True





    # ==========================
    # ADD HARDWARE FORM
    # ==========================


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



        st.write("")



        save_col, cancel_col = st.columns(2)



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
