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
    # ADD NEW HARDWARE
    # ==========================


    if st.button(

        "Add New Hardware"

    ):


        st.session_state.add_hardware = True




    if st.session_state.get(

        "add_hardware",

        False

    ):


        st.subheader(

            "Add Hardware"

        )


        new_row = {}



        for column in df.columns:


            new_row[column] = st.text_input(

                column,

                key="add_"+column

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





    st.divider()



    # ==========================
    # EDIT EXISTING ROWS
    # ==========================


    st.subheader(

        "Existing Hardware"

    )



    for index,row in df.iterrows():



        col1,col2 = st.columns(

            [1,6]

        )



        with col1:


            if st.button(

                "Edit",

                key=f"edit_{index}"

            ):


                st.session_state.edit_row = index




        with col2:


            if st.session_state.get(

                "edit_row"

            ) == index:



                st.info(

                    f"Editing {row['Model_Name']}"

                )



                updated_row = {}



                for column in df.columns:


                    updated_row[column] = st.text_input(

                        column,

                        value=str(row[column]),

                        key=f"{column}_{index}"

                    )



                if st.button(

                    "Update Row",

                    key=f"update_{index}"

                ):



                    for column in df.columns:


                        df.loc[index,column] = updated_row[column]



                    save_database(df)



                    st.success(

                        "Row Updated Successfully"

                    )



                    st.session_state.edit_row = None


                    st.rerun()



        st.dataframe(

            df.iloc[[index]],

            use_container_width=True

        )
