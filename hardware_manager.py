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

    st.success("NEW HARDWARE MANAGER LOADED")

    st.subheader(
        "Hardware Database Management"
    )


    df = load_database()

    if "edit_row" not in st.session_state:

        st.session_state.edit_row = None
    



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



    # ==========================
    # CREATE ACTION COLUMN
    # ==========================
    
    table_df.insert(
    
        0,
    
        "Action",
    
        range(len(df))
    
    )
    
    
    # ==========================
    # ADD ROW NUMBER COLUMN
    # ==========================
    
    table_df.insert(
    
        1,
    
        "Row",
    
        range(1, len(df)+1)
    
    )



    # ==========================
    # DISPLAY TABLE WITH EDIT BUTTONS
    # ==========================
    
    for index, row in df.iterrows():
    
    
        cols = st.columns(len(table_df.columns))
    
    
        # ==========================
        # ACTION BUTTON
        # ==========================
    
        with cols[0]:
    
    
            if st.button(
    
                "✏️",
    
                key=f"edit_{index}"
    
            ):
    
                st.session_state.edit_row = index
    
    
    
        # ==========================
        # DISPLAY DATA
        # ==========================
    
        for i,column in enumerate(df.columns):
    
    
            with cols[i+1]:
    
                st.write(
                    row[column]
                )
    
    
    
        # ==========================
        # EDIT MODE
        # ==========================
    
        if st.session_state.get("edit_row") == index:
    
    
            st.info(
                f"Editing {row['Model_Name']}"
            )
    
    
            edited_values = {}
    
    
            edit_cols = st.columns(4)
    
    
    
            for i,column in enumerate(df.columns):
    
    
                with edit_cols[i % 4]:
    
    
                    edited_values[column] = st.text_input(
    
                        column,
    
                        value=str(row[column]),
    
                        key=f"{index}_{column}"
    
                    )
    
    
    
            update_col, cancel_col = st.columns(2)
    
    
    
            # ==========================
            # UPDATE BUTTON
            # ==========================
    
            with update_col:
    
    
                if st.button(
    
                    "✅ Update",
    
                    key=f"update_{index}"
    
                ):
    
    
                    for column in df.columns:
    
    
                        df.loc[index,column] = edited_values[column]
    
    
    
                    save_database(df)
    
    
                    st.session_state.edit_row = None
    
    
                    st.success(
    
                        "Updated Successfully"
    
                    )
    
    
                    st.rerun()
    
    
    
            # ==========================
            # CANCEL BUTTON
            # ==========================
    
            with cancel_col:
    
    
                if st.button(
    
                    "❌ Cancel",
    
                    key=f"cancel_{index}"
    
                ):
    
    
                    st.session_state.edit_row = None
    
    
                    st.rerun()




   



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
