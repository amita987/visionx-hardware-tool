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
    # HARDWARE TABLE DISPLAY
    # ==========================


    st.write(
        "Hardware Inventory"
    )


    # --------------------------
    # ACTION COLUMN
    # --------------------------

    display_df = df.copy()


    display_df.insert(

        0,

        "Action",

        "✏️"

    )


    st.dataframe(

        display_df,

        use_container_width=True,

        hide_index=True

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
    # CLEAN HARDWARE TABLE (NEW VERSION)
    # ==========================
    
    st.write("Hardware Inventory (Compact View)")
    
    if "edit_row" not in st.session_state:
        st.session_state.edit_row = None
    
    
    for index, row in df.iterrows():
    
        # ==========================
        # TABLE ROW (COMPACT VIEW)
        # ==========================
        col1, col2, col3, col4, col5, col6 = st.columns([0.5, 2, 2, 2, 1, 1])
    
        # --------------------------
        # COLUMN 1 → EDIT BUTTON
        # --------------------------
        with col1:
            if st.button("✏️", key=f"edit_{index}"):
                st.session_state.edit_row = index
    
        # --------------------------
        # COLUMN 2 → MODEL NAME
        # --------------------------
        with col2:
            st.write(row["Model_Name"])
    
        # --------------------------
        # COLUMN 3 → MANUFACTURER
        # --------------------------
        with col3:
            st.write(row["Manufacturer"])
    
        # --------------------------
        # COLUMN 4 → VRAM
        # --------------------------
        with col4:
            st.write(f"{row['VRAM_GB']} GB")
    
        # --------------------------
        # COLUMN 5 → POWER
        # --------------------------
        with col5:
            st.write(f"{row['Power_W']} W")
    
        # --------------------------
        # COLUMN 6 → WORKLOAD RANGE
        # --------------------------
        with col6:
            st.write(f"{row['Workload_Min']} - {row['Workload_Max']}")
    
        # ==========================
        # EDIT MODE (ONLY THIS ROW)
        # ==========================
        if st.session_state.edit_row == index:
    
            st.markdown(
                """
                <div style="
                    background-color:#E8F5E9;
                    padding:12px;
                    border-radius:10px;
                    margin-top:10px;
                ">
                <b>Editing This Hardware</b>
                </div>
                """,
                unsafe_allow_html=True
            )
    
            updated_values = {}
    
            cols = st.columns(4)
    
            for i, column in enumerate(df.columns):
                with cols[i % 4]:
                    updated_values[column] = st.text_input(
                    
                        column,
                    
                        value=str(row[column]),
                    
                        key=f"edit_{index}_{column}"
                    
                    )
    
            btn1, btn2 = st.columns(2)
    
            # --------------------------
            # UPDATE BUTTON
            # --------------------------
            with btn1:
                if st.button("✅ Update", key=f"update_{index}"):
    
                    for column in df.columns:
                        df.loc[index, column] = updated_values[column]
    
                    save_database(df)
    
                    st.success("Updated Successfully")
    
                    st.session_state.edit_row = None
    
                    st.rerun()
    
            # --------------------------
            # CANCEL BUTTON
            # --------------------------
            with btn2:
                if st.button("❌ Cancel", key=f"cancel_{index}"):
    
                    st.session_state.edit_row = None
    
                    st.rerun()
    
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
