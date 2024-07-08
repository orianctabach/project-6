import streamlit as st
import pandas as pd
import plotly_express as px


df = pd.read_csv("vehicles_us.csv")

st.header('Raw Data')

st.dataframe(df)

#-------------------
st.header('How many days pass until the deal is made')
st.text ('First and foremost, I wanted to see how many days it takes for a deal to be made.')
st.write(px.histogram(df, x='days_listed'))
st.text ('It is easy to see that most deals are made a few days after posting the listing. ')

#-------------------
st.header('Does mentioning the car\'s color in the listing affect the number of days the car is listed? ')
st.text('Initial exploration of the dataset revealed a significant number of missing values for car color. This implies that the color of the car was not recorded for a substantial portion of the records. This raises the question of whether the absence of car color information has any impact on the speed at which the car is sold.')

color_index=[]
for c in df.paint_color:
    if pd.isna(c):
        color_index.append('no color is listed')
    else:
        color_index.append('a color is listed')
df["color_index"]=color_index

st.write(px.histogram(df, x="days_listed", color="color_index", barmode="overlay", histnorm='probability'))

st.text('Analysis Reveals No Significant Impact of Car Color on Sales Velocity')

#-------------------
st.header('Does the car\' condition affect the number of days the car is listed?' )
# explanation about what is going to happen
st.write(px.histogram(df, x="days_listed", color="condition", barmode="overlay", histnorm='probability'))
# explanation about the noise

cond_index=[]
for c in df.condition:
    if c in ["excellent", "good", "like new"]:
        cond_index.append(True)
    else:
        cond_index.append(False)
df2=df[cond_index]

st.write(px.histogram(df2, x="days_listed", color="condition", barmode="overlay", histnorm='probability'))

# results

#-------------------
st.header('Exploring the Impact of listing date on the number of days a deal is made')

# explantaion
trim_date=[]
for d in df.date_posted:
    trim_date.append(d[:-3])
df["trim_date"]=trim_date
st.dataframe(df.trim_date.value_counts())



#-------------------