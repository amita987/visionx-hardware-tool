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
# HARDWARE TABLE FUNCTION
# ==========================

def show_hardware_table():


    df = load_database()



    st.subheader(
        "Hardware Reference Database"
    )



    # ==========================
    # ADD NEW HARDWARE BUTTON
    # ==========================


    if st.button(
        "Add New Hardware"
    ):


        st.session_state.add_hardware = True



    if "add_hardware" in st.session_state and st.session_state.add_hardware:


        st.write(
            "Enter Hardware Details"
        )


        new_row = {}


        for column in df.columns:


            new_row[column] = st.text_input(
                column,
                key=column
            )



        if st.button(
            "Update Hardware Database"
        ):


            df.loc[len(df)] = new_row


            save_database(df)


            st.success(
                "New Hardware Added"
            )


            st.session_state.add_hardware = False


            st.rerun()



    # ==========================
    # DISPLAY DATABASE
    # ==========================


    st.dataframe(
        df,
        use_container_width=True
    )
