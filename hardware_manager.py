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

    if "add_hardware" not in st.session_state:

        st.session_state.add_hardware = False



    # ==========================
    # FULL HARDWARE TABLE
    # ==========================



    # ==========================
    # HARDWARE INVENTORY HEADER
    # ==========================
    
    
    header_col, row_col, button_col = st.columns([4,2,1])
    
    
    with header_col:
    
        st.subheader(
            "Hardware Inventory"
        )
    
    
    
    with row_col:
    
        edit_row_number = st.number_input(
    
            "Edit Row",
    
            min_value=1,
    
            max_value=len(df),
    
            value=1,
    
            step=1
    
        )
    
    
    
    with button_col:
    
        st.write("")
    
        if st.button(
    
            "✏️ Edit"
    
        ):
    
            st.session_state.edit_row = edit_row_number - 1



    table_df = df.copy()



    # Add row number only
    
    table_df.insert(
    
        0,
    
        "Row",
    
        range(1, len(df)+1)
    
    )



    # Display table


    st.dataframe(

        table_df,

        use_container_width=True,

        hide_index=True

    )

    # COMPLETELY NEW BLOCK XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx
        
        
     # =================================================
    # EDIT INDIVIDUAL ROW BLOCK (SEPARATE)
    # =================================================
    
    
    # --------------------------
    # CREATE MEMORY
    # --------------------------
    
    if "selected_edit_row" not in st.session_state:
    
        st.session_state.selected_edit_row = None
    
    
    
    # --------------------------
    # CONNECT EXISTING EDIT BUTTON
    # --------------------------
    
    if "edit_row" in st.session_state:
    
        if st.session_state.edit_row is not None:
    
            st.session_state.selected_edit_row = st.session_state.edit_row
    
    
    
    
    # --------------------------
    # SHOW EDIT AREA
    # --------------------------
    
    if st.session_state.selected_edit_row is not None:
    
    
        selected_row = st.session_state.selected_edit_row
    
    
        row_data = df.loc[selected_row]
    
    
    
        st.markdown(
    
        """
    
        <div style="
    
        background-color:#E8F5E9;
    
        padding:15px;
    
        border-radius:10px;
    
        ">
    
        <h3>
    
        Editing Selected Hardware
    
        </h3>
    
        </div>
    
        """,
    
        unsafe_allow_html=True
    
        )
    
    
    
        edited_row = {}
    
    
    
        # --------------------------
        # HORIZONTAL FIELDS
        # --------------------------
    
        edit_columns = st.columns(4)
    
    
    
        for i, column in enumerate(df.columns):
    
    
            with edit_columns[i % 4]:
    
    
                edited_row[column] = st.text_input(
    
                    column,
    
                    value=str(row_data[column]),
    
                    key=f"edit_box_{selected_row}_{column}"
    
                )
    
    
    
        st.write("")
    
    
    
        # --------------------------
        # UPDATE / CANCEL BUTTONS
        # --------------------------
    
        update_button, cancel_button = st.columns(2)
    
    
    
    
        # UPDATE
    
        with update_button:
    
    
            if st.button(
    
                "✅ Update",
    
                key="update_selected_row"
    
            ):
    
    
                for column in df.columns:
    
    
                    df.loc[selected_row,column] = edited_row[column]
    
    
    
                save_database(df)
    
    
    
                st.success(
    
                    "Row Updated Successfully"
    
                )
    
    
                st.session_state.selected_edit_row = None
    
    
                st.session_state.edit_row = None
    
    
                st.rerun()
    
    
    
    
        # CANCEL
    
        with cancel_button:
    
    
            if st.button(
    
                "❌ Cancel",
    
                key="cancel_selected_row"
    
            ):
    
    
                st.session_state.selected_edit_row = None
    
    
                st.session_state.edit_row = None
    
    
                st.rerun()
    # COMPLETELY NEW BLOCK XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXx

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



