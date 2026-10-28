#Program to convert from a unit to another
import streamlit as st

def km_to_miles(km):
    return km * 0.621371

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kg_to_pounds(kg):
    return kg * 2.20462


st.title("Unit Converter")

conversion = st.selectbox(
    "Select Conversion",
    ["Kilometers to Miles",
     "Celsius to Fahrenheit",
     "Kilograms to Pounds"]
)

value = st.number_input("Enter Value", value=0.0)

if st.button("Bolo iski unit badal du !"):

    if conversion == "Kilometers to Miles":
        result = km_to_miles(value)
        unit = "Miles"

    elif conversion == "Celsius to Fahrenheit":
        result = celsius_to_fahrenheit(value)
        unit = "°F"

    else:
        result = kg_to_pounds(value)
        unit = "Pounds"

    st.success(f"Result: {result:.2f} {unit}")