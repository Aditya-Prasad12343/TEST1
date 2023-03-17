import streamlit as st

# Conversion factors for length
length_conversion_factors = {
    "inches to centimeters": 2.540,
    "millimeters to inches": 0.03937,
    "feet to centimeters": 30.4878,
    "centimeters to inches": 0.3937,
    "yards to meters": 0.9144028,
    "meters to feet": 3.281,
    "miles to kilometers": 1.6093419,
    "kilometers to miles": 0.621372
}

# Conversion factors for area
area_conversion_factors = {
    "square inches to square centimeters": 6.4516,
    "square centimeters to square inches": 0.1550,
    "square feet to square meters": 0.0929,
    "square meters to square yards": 1.195986,
    "square yards to square meters": 0.83613,
    "square kilometers to square miles": 0.386101,
    "square miles to square kilometers": 2.589999,
    "hectares to acres": 2.471044,
    "acres to hectares": 0.404687
}

# Conversion factors for mass
mass_conversion_factors = {
    "grains to ounces": 0.00208,
    "ounces to grams": 28.3495,
    "grams to ounces": 0.03527396,
    "pounds to kilograms": 0.4535924,
    "kilograms to pounds": 2.2046223,
    "short tons to metric tons": 0.892857,
    "metric tons to short tons": 1.1200,
    "long tons to metric tons": 1.01605
}

# Conversion factors for volume
volume_conversion_factors = {
    "teaspoons to milliliters": 5,
    "milliliters to fluid ounces": 0.0338147,
    "tablespoons to milliliters": 15,
    "liters to pints": 2.11342,
    "fluid ounces to milliliters": 30,
    "liters to quarts": 1.05671,
    "gallons to liters": 3.785332,
    "cups to liters": 0.23658,
    "pints to liters": 0.473167,
    "cubic meters to cubic feet": 35.3144,
    "cubic feet to cubic meters": 0.0283170,
    "cubic yards to cubic meters": 0.764559
}

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
input_value = st.sidebar.number_input("Enter a value to convert", value=0.0, step=0.1
# Perform the conversion
output_value = input_value * (conversion_factors[input_unit] / conversion_factors[output_unit])

# Display the result
st.write("Result:", round(output_value, 4), output_unit)
