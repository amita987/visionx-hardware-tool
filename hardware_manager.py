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
    return pd.read_csv(DATABASE_FILE)



# ==========================
# SAVE DATABASE
# ==========================

def save_database(df):
    df.to_csv(DATABASE_FILE, index=False)



# ==========================
# HARDWARE MANAGEMENT PAGE
# ==========================

def hardware_management():


    st.subheader("Hardware Database Management")

    df = load_database()



    # ==========================
    # TABLE DISPLAY
    # ==========================

    st.write("Hardware Inventory")

    st.dataframe(df, use_container_width=True, hide_index=True)



    # ==========================
    # SELECT ROW TO EDIT
    # ==========================

    if "edit_row" not in st.session_state:
        st.session_state.edit_row = None


    st.divider()

    edit_index = st.selectbox(
        "Select Hardware to Edit",
        options=range(len(df)),
        format_func=lambda x: df.loc[x, "Model_Name"]
    )

    if st.button("✏️ Edit"):
        st.session_state.edit_row = edit_index



    # ==========================
    # EDIT PANEL
    # ==========================

    if st.session_state.edit_row is not None:

        index = st.session_state.edit_row
        row = df.loc[index]

        st.markdown(
            """
            <div style="
                background-color:#E8F5E9;
                padding:15px;
                border-radius:10px;
            ">
            <h3>Editing Hardware Record</h3>
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
                    key=f"edit_{column}_{index}"
                )

        update_col, cancel_col = st.columns(2)

        with update_col:
            if st.button("✅ Update"):
                for column in df.columns:
                    df.loc[index, column] = updated_values[column]

                save_database(df)

                st.success("Hardware Updated Successfully")

                st.session_state.edit_row = None

                st.rerun()

        with cancel_col:
            if st.button("❌ Cancel"):
                st.session_state.edit_row = None
                st.rerun()



    # ==========================
    # ADD HARDWARE
    # ==========================

    st.divider()

    if "add_hardware" not in st.session_state:
        st.session_state.add_hardware = False


    if st.button("➕ Add New Hardware"):
        st.session_state.add_hardware = True


    if st.session_state.add_hardware:

        st.subheader("Add New Hardware")

        new_row = {}

        cols = st.columns(4)

        for i, column in enumerate(df.columns):
            with cols[i % 4]:
                new_row[column] = st.text_input(
                    column,
                    key=f"new_{column}"
                )

        save_col, cancel_col = st.columns(2)

        with save_col:
            if st.button("💾 Save Hardware"):
                df.loc[len(df)] = new_row
                save_database(df)

                st.success("Hardware Added")

                st.session_state.add_hardware = False

                st.rerun()

        with cancel_col:
            if st.button("❌ Cancel Add"):
                st.session_state.add_hardware = False
                st.rerun()
