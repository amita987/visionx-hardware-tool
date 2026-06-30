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



# COMPLETELY NEW BLOCK



# ==========================
# EDIT INDIVIDUAL ROW
# ==========================


# create edit memory

if "edit_selected_row" not in st.session_state:

    st.session_state.edit_selected_row = None



# ==========================
# ROW NUMBER INPUT
# ==========================


edit_row_number = st.number_input(

    "Enter Row Number to Edit",

    min_value=1,

    max_value=len(df),

    value=1,

    step=1

)



# ==========================
# EDIT BUTTON
# ==========================


if st.button(

    "✏️ Edit Selected Row"

):


    # convert display row number to dataframe index

    st.session_state.edit_selected_row = edit_row_number - 1




# ==========================
# EDIT MODE
# ==========================


if st.session_state.edit_selected_row is not None:


    row_index = st.session_state.edit_selected_row


    row_data = df.loc[row_index]



    st.markdown(

    """

    <div style="

    background-color:#E8F5E9;

    padding:15px;

    border-radius:10px;

    ">

    <h3>

    Editing Selected Hardware Row

    </h3>

    </div>

    """,

    unsafe_allow_html=True

    )



    # temporary storage

    edited_data = {}



    # horizontal fields

    edit_columns = st.columns(4)



    for i,column in enumerate(df.columns):


        with edit_columns[i % 4]:


            edited_data[column] = st.text_input(

                column,

                value=str(row_data[column]),

                key=f"edit_row_{row_index}_{column}"

            )




    st.write("")



    # ==========================
    # UPDATE / CANCEL BUTTONS
    # ==========================


    update_button, cancel_button = st.columns(2)




    # ==========================
    # UPDATE
    # ==========================


    with update_button:


        if st.button(

            "✅ Update Row"

        ):


            for column in df.columns:


                df.loc[row_index,column] = edited_data[column]



            save_database(df)



            st.success(

                "Row Updated Successfully"

            )



            st.session_state.edit_selected_row = None



            st.rerun()




    # ==========================
    # CANCEL
    # ==========================


    with cancel_button:


        if st.button(

            "❌ Cancel Edit"

        ):


            st.session_state.edit_selected_row = None


            st.rerun()
