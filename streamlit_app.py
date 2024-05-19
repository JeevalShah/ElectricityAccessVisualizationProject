import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

# Constants
ELECTRICITY = pd.read_csv('./CSVs/Predicted_Dataset_mean_lasso_ridge_linear.csv')
ELECTRICITY = ELECTRICITY.set_index('Country Name') 
country_list = [
    "Africa Western and Central",
    "Angola",
    "Burundi",
    "Benin",
    "Burkina Faso",
    "Botswana",
    "Central African Republic",
    "Cameroon",
    "Congo, Dem. Rep.",
    "Congo, Rep.",
    "Comoros",
    "Cabo Verde",
    "Djibouti",
    "Algeria",
    "Egypt, Arab Rep.",
    "Eritrea",
    "Ethiopia",
    "Gabon",
    "Ghana",
    "Guinea",
    "Gambia, The",
    "Guinea-Bissau",
    "Equatorial Guinea",
    "Kenya",
    "Liberia",
    "Libya",
    "Lesotho",
    "Morocco",
    "Madagascar",
    "Mali",
    "Mozambique",
    "Mauritania",
    "Mauritius",
    "Malawi",
    "Namibia",
    "Niger",
    "Nigeria",
    "Rwanda",
    "Sudan",
    "Senegal",
    "Sierra Leone",
    "Somalia",
    "Sub-Saharan Africa (excluding high income)",
    "South Sudan",
    "Sub-Saharan Africa",
    "Eswatini",
    "Seychelles",
    "Chad",
    "Togo",
    "Tunisia",
    "Tanzania",
    "Uganda",
    "South Africa",
    "Zambia",
    "Zimbabwe"
]

def graph(countries, low, up):
    # Initialize an empty DataFrame to store combined data
    combined_df = pd.DataFrame()

    # Iterate over each country in the list
    for country in countries:
        # Extract electricity data for the current country and specified range
        electricity_data = ELECTRICITY.loc[country][map(str, range(low, up+1))]
        electricity_series = pd.Series(electricity_data, name=country)

        # Convert the Series to a DataFrame and combine it with existing data
        combined_df = pd.concat([combined_df, electricity_series], axis=1)

    # Reset index to make years a column
    combined_df.reset_index(inplace=True)
    # Rename the columns
    combined_df.columns = ['Year'] + countries
    # Set the 'Year' column as index
    combined_df.set_index('Year', inplace=True)

    st.title('Evolution of Electricity Access')

    # Plot the combined data
    st.line_chart(data=combined_df, use_container_width=True)

    
st.title("Predictive Modeling of Electricity Access in Africa")

countries = st.multiselect('Choose Country: ',
                      (None, *country_list))

if not None in countries:

    selected_countries_str = ', '.join(countries)

    if  selected_countries_str:
        st.success(f'You selected {selected_countries_str}')

        years = list(range(1990, 2031))

        # Create dropdowns for selecting the lower and upper bounds
        lower_bound = st.selectbox("Select Lower Bound Year", [None, *years])
        upper_bound = st.selectbox("Select Upper Bound Year", [None, *years])

        low, upp = lower_bound, upper_bound

        if low and upp:
            if low > upp:
                low, upp = upp, low

            # Display the selected range
            st.write("Selected Range:", low, "to", upp)

            graph(countries, low, upp)
            
