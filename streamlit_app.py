import streamlit as st 
import barcode
from barcode.writer import ImageWriter
import os

OUTPUT_DIR = "output"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

st.title("Barcode Generator Web App")

option = st.selectbox(
    "Choose Barcode Type",
    ("Code128 (Text)", "EAN-13 (12 digits)")
)

data = st.text_input("Enter Data")
filename = st.text_input("Enter File Name")

if st.button("Generate Barcode"):

    if data and filename:

        try:
            if option == "Code128 (Text)":
                code = barcode.get("code128", data, writer=ImageWriter())

            elif option == "EAN-13 (12 digits)":
                if len(data) != 12 or not data.isdigit():
                    st.error("EAN-13 needs exactly 12 digits")
                else:
                    code = barcode.get("ean13", data, writer=ImageWriter())

            path = os.path.join(OUTPUT_DIR, filename)
            full_path = code.save(path)

            st.success(" Barcode Generated!")
            st.image(full_path)  
            with open(full_path, "rb") as file:
             st.download_button(
                label=" Download Barcode",
                data=file,
                file_name=filename + ".png",
                mime="image/png"
    )
        except Exception as e:
            st.error(f"Error: {e}")

    else:
        st.warning("Please enter all fields")