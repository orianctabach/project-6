import streamlit as st
import pandas as pd
import plotly_express as px
import numpy as np 



df = pd.read_csv("vehicles_us.csv")

st.header('Viewing the Data')
st.markdown(
    "To get a sense of the data we are dealing with, "
     "it would be beneficial to view a portion of the table"
     "(after cleaning it a bit):"
     )

#filling missing values

df['paint_color']=df['paint_color'].fillna('Unknown')
df['is_4wd']=df['is_4wd'].fillna(0)
df['model_year'] = df['model_year'].fillna(df.groupby(['model'])['model_year'].transform('median'))
df['odometer'] = df['odometer'].fillna(df.groupby(['model_year'])['odometer'].transform('mean'))

mean_odometer=df['odometer'].mean()
df['odometer'] = df['odometer'].fillna(mean_odometer)

new_cylinders = df['cylinders'].fillna(df.groupby(['model'])['cylinders'].transform('mean'))
df['cylinders']=np.floor(new_cylinders)

#searching and removing duplicates

df=df.drop_duplicates()

st.dataframe(df)

#-------------------
st.header('How many days pass until the deal is made')
st.text ('First and foremost, I wanted to see how many days it takes for a deal to be made.')
st.write(px.histogram(df, x='days_listed'))
st.text ('It is easy to see that most deals are made a few days after posting the listing. ')

#-------------------
st.header('Does mentioning the car\'s color in the listing affect the number of days the car is listed? ')
st.markdown(
    "Initial exploration of the dataset revealed a "
    "significant number of missing values for car color."
     " This implies that the color of the car was not recorded "
     "for a substantial portion of the records. This raises the "
     "question of whether the absence of car color information has "
     "any impact on the speed at which the car is sold."
     )

color_index=[]
for c in df.paint_color:
    if c== 'Unknown':
        color_index.append('no color is listed')
    else:
        color_index.append('a color is listed')
df["color_index"]=color_index

st.write(px.histogram(df, x="days_listed", color="color_index", barmode="overlay", histnorm='probability'))

st.text('Analysis Reveals No Significant Impact of Car Color on Sales Velocity')

#-------------------
st.header('Does the car\'s condition affect the number of days the car is listed?' )
st.markdown(
    "Having examined whether including the car's color in the listings leads "
    "to faster sales, and finding no conclusive evidence in this regard, "
    "I now aim to investigate the influence of the car's condition "
    "on the number of days until it is sold."
    )
st.write(px.histogram(df, x="days_listed", color="condition", barmode="overlay", histnorm='probability'))

st.markdown(
    "We observe the presence of some noise in the data. Upon closer inspection, "
    "it appears that this noise stems from categories with a relatively small "
    "number of car sales compared to other categories. "
    "I choose to exclude these categories to get a clearer and more "
    "focused analysis of the data."
)

cond_index=[]
for c in df.condition:
    if c in ["excellent", "good", "like new"]:
        cond_index.append(True)
    else:
        cond_index.append(False)
df2=df[cond_index]

st.write(px.histogram(df2, x="days_listed", color="condition", barmode="overlay", histnorm='probability'))

st.markdown(
    "Even after removing the noise, we still lack a definitive conclusion."
    )

#-------------------
st.header('Exploring the Impact of listing date on the number of days a deal is made')

st.markdown(
    "Having established the lack of influence of car color listing "
    "and car condition on sale speed, I intend to investigate "
    "potential changes in the car sales market over time "
    "that might explain any broader trends or patterns."
)

trim_date=[]
for d in df.date_posted:
    trim_date.append(d[:-3])
df["trim_date"]=trim_date
st.dataframe(df.trim_date.value_counts())

st.markdown(
    "As observed in the table, the number of cars sold remains consistent "
    "across all months except for April 2019. It is possible that the "
    "data collection for that month ended prematurely. "
    "Regardless, April 2019 stands out as an anomaly compared to the other months, "
    "and therefore, I will choose to exclude it from the analysis. "
    "I will now present the probability against the days that it took to astablish a deal:"
)

date_index=[]
for d in df.trim_date:
    if c in ["2019-04"]:
        date_index.append(False)
    else:
        date_index.append(True)
df3=df[date_index]

st.write(px.histogram(df3, x="days_listed", color="trim_date", barmode="overlay", histnorm='probability'))

st.markdown(
    "Similarly, the sales patterns across the months appear consistent, "
    "suggesting that there is no significant change in sales over time."
    )

#-------------------
st.header('Impact of car price on number of days until a deal is made')
st.markdown(
    "To conclude my analysis, I aim to investigate "
    "the relationship between the car's price and its sales speed."
)


st.write(px.scatter(df, x='days_listed', y='price'))

st.markdown(
    "The presence of a small number of exceptionally expensive cars "
    "distorts the distribution of the data, making it challenging to visualize and analyze. "
    "To address this issue, I intend to exclude these extremely expensive cars "
    "from the upcoming analysis. In my case, I have chosen to remove cars priced above $150,000."
)

res_price=[]
for p in df.price:
    if p>150000:
        res_price.append(False)
    else:
        res_price.append(True)

df4=df[res_price]

st.write(px.scatter(df4, x='days_listed', y='price'))

st.markdown(
    "While this visualization is an improvement, it's still not ideal. "
    "I'll change the data points to transparent, allowing me to better identify areas "
    "with higher concentrations of points. This means that darker regions represent "
    "the most frequent price ranges. "
    "Clicking on the checkbox will adjust the viewing resolution."
)

opacity_ = st.checkbox('Render the points are transparecy?', value=False)
if opacity_:
    st.write(px.scatter(df4, x='days_listed', y='price', opacity=(0.05)))
else:
    st.write(px.scatter(df4, x='days_listed', y='price', opacity=(0.9)))

st.markdown("The visualization reveals a cluster of data points indicating a "
            "specific price range that is relatively inexpensive and "
            "associated with relatively quick car sales.")

st.markdown(
            "In conclusion, in this analysis I aimed to identify a specific "
            "factor that either its presence or absence significantly impacts "
            "car sales speed. Unfortunately, no such definitive factor was discovered. "
            "While a correlation between lower car prices and faster sales times was observed, "
            "this trend was not universal. Certain outliers, represented by "
            "exceptionally inexpensive cars, remained on the market for extended periods. "
            "Therefore, it is recommended to further investigate the characteristics of these "
            "inexpensive cars to understand why they stay on the market for a long time "
            "instead of selling quickly.")

#-------------------