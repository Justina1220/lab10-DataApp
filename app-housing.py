
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data(1990)by Ziyu Chen')

df =pd.read_csv(r'housing.csv')


#add a slider
price_slider = st.slider('Median House Price', 0, 500001, 200000)

st.write('See more filters in the sidebar')

# add a multi select
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# add a radio button
income_filter = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Medium', 'High')
)




#filter by house value
df = df[df.median_house_value >= price_slider]

# filter by location type
df = df[df.ocean_proximity.isin(location_filter)]

# filter by income level
if income_filter == 'Low':
    df = df[df.median_income <= 2.5]
elif income_filter == 'High':
    df = df[df.median_income > 4.5]
elif income_filter == 'Medium':
    df = df[(df.median_income > 2.5) & (df.median_income <= 4.5)]
    


#show on map
st.map(df)

#show the df
st.write(df)

#show the population figure
fig,ax = plt.subplots()
price_distribution = df.median_house_value
price_distribution.plot.hist(ax=ax,bins=30)
st.pyplot(fig)