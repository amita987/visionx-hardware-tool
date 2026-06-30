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
    # HARDWARE TABLE TOP
    # ==========================


    st.write(
        "Current Hardware Database"
    )



    for index,row in df.iterrows():


        col_action, col_table = st.columns(

            [1,10]

        )



        with col_action:


            if st.button(

                "✏️",

                key=f"edit_{index}"

            ):

                st.session_state.edit_row = index



        with col_table:


            st.dataframe(

                df.iloc[[index]],

                use_container_width=True

            )



        # ==========================
        # EDIT AREA
        # ==========================


        if st.session_state.get(

            "edit_row"

        ) == index:



            st.info(

                f"Editing {row['Model_Name']}"

            )



            edit_values = {}



            columns = st.columns(4)



            for i,column in enumerate(df.columns):


                with columns[i % 4]:


                    edit_values[column] = st.text_input(

                        column,

                        value=str(row[column]),

                        key=f"edit_{column}_{index}"

                    )



            update_col,cancel_col = st.columns(2)



            with update_col:


                if st.button(

                    "💾",

                    key=f"save_{index}"

                ):



                    for column in df.columns:


                        df.loc[index,column] = edit_values[column]



                    save_database(df)



                    st.success(

                        "Updated"

                    )


                    st.session_state.edit_row = None


                    st.rerun()



            with cancel_col:


                if st.button(

                    "❌",

                    key=f"cancel_{index}"

                ):


                    st.session_state.edit_row = None


                    st.rerun()



    st.divider()



    # ==========================
    # ADD NEW HARDWARE BUTTON
    # ==========================


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

            "Add Hardware Details"

        )



        new_row = {}



        columns = st.columns(4)



        for i,column in enumerate(df.columns):


            with columns[i % 4]:


                new_row[column] = st.text_input(

                    column,

                    key=f"new_{column}"

                )



        save_col,cancel_col = st.columns(2)



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
