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
    # SHOW CURRENT DATABASE
    # ==========================


    st.dataframe(

        df,

        use_container_width=True

    )



    st.divider()



    # ==========================
    # ADD NEW HARDWARE BUTTON
    # ==========================


    if st.button(

        "Add New Hardware"

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

            "Enter New Hardware Details"

        )



        new_data = {}



        for column in df.columns:


            new_data[column] = st.text_input(

                column

            )



        if st.button(

            "Update Hardware Database"

        ):



            df.loc[len(df)] = new_data



            save_database(df)



            st.success(

                "Hardware Added Successfully"

            )



            st.session_state.add_hardware = False



            st.rerun()
