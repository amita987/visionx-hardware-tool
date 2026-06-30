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
    # FULL HARDWARE TABLE
    # ==========================


    st.write(
        "Hardware Inventory"
    )



    table_df = df.copy()



    table_df.insert(

        0,

        "Row",

        range(1, len(df)+1)

    )



    st.dataframe(

        table_df,

        use_container_width=True,

        hide_index=True

    )




   



    # ==========================
    # ADD HARDWARE
    # ==========================


    st.divider()



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



        save_col, cancel_col = st.columns(2)



        with save_col:


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
