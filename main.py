import streamlit as st

# Define the conversion factors for length, area, mass, and volume
length_conversion_factors = {
    "inch": 2.54,
    "cm": 1,
    "mm": 0.1,
    "foot": 30.48,
    "yard": 91.44,
    "meter": 100,
    "mile": 160934,
    "km": 100000,
}

area_conversion_factors = {
    "sq. inch": 6.4516,
    "sq. cm": 1,
    "sq. foot": 0.0929,
    "sq. meter": 1,
    "sq. yard": 0.83613,
    "sq. mile": 2589990,
    "sq. km": 1000000,
    "hectare": 10000,
    "acre": 4046.86,
}

mass_conversion_factors = {
    "grain": 0.06479891,
    "scruple": 1.2959782,
    "dram": 3.8879346,
    "ounce": 28.349523,
    "gram": 1,
    "pound": 453.59237,
    "kilogram": 1000,
    "short ton": 907184.74,
    "metric ton": 1000000,
    "long ton": 1016046.91,
}

volume_conversion_factors = {
    "teaspoon": 5,
    "milliliter": 1,
    "tablespoon": 15,
    "liter": 1000,
    "fluid ounce": 29.5735,
    "quart": 946.353,
    "gallon": 3785.41,
    "cup": 236.588,
    "pint": 473.176,
    "cubic meter": 1000000,
    "cubic foot": 28316.846,
    "cubic yard": 764554.858,
}

# Set page title and center everything
st.set_page_config(page_title="Unit Converter", layout="centered")

# Display the conversion options and allow the user to select a conversion type
conversion_type = st.sidebar.selectbox("Select a conversion type", ["length", "area", "mass", "volume"])

if conversion_type == "length":
    conversion_factors = length_conversion_factors
elif conversion_type == "area":
    conversion_factors = area_conversion_factors
elif conversion_type == "mass":
    conversion_factors = mass_conversion_factors
elif conversion_type == "volume":
    conversion_factors = volume_conversion_factors

# Allow the user to enter a value to convert
input_value = st.sidebar.number_input("Enter a value to convert", value=0.0, step=0.1)

# Complete the code for the conversion calculation and output
if input_value:
    input_unit = st.sidebar.selectbox("Select the input unit", list(conversion_factors.keys()))
    output_unit = st.sidebar.selectbox("Select the output unit", list(conversion_factors.keys()))

    # Perform the conversion
    output_value = input_value * (conversion_factors[input_unit] / conversion_factors[output_unit])

    # Display the result in a box
    st.write("**Result:**")
    st.success(str(round(output_value, 4)) + " " + output_unit)
