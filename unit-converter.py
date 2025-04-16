import streamlit as st

st.title("🌍 Unit Converter App")
st.markdown("### Converts Length, Weight, And Time Instantly")
st.write("Welcome! Select a category, enter a value and get the converted result in real-time")

# Select category
category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Define unit conversion options based on category
if category == "Length":
    unit = st.selectbox("📏 Select Conversion", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weight":
    unit = st.selectbox("⚖️ Select Conversion", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("⏱️ Select Conversion", ["Hours to Minutes", "Minutes to Hours", "Hours to Days", "Days to Hours"])

# Input value
value = st.number_input("Enter the value to convert", step=0.01)

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462

    elif category == "Time":
        if unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Days":
            return value / 24
        elif unit == "Days to Hours":
            return value * 24

    return "Invalid conversion"

# Display result
if st.button("Convert"):
    result = convert_units(category, value, unit)
    st.success(f"The result is: {result:.2f}")
