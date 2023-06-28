import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from PIL import Image


st.set_page_config(layout="wide")

def main():
    image=Image.open('banner.jpg')
    banner_image=image.resize((1300,500))
    st.image(banner_image)
    st.markdown('''# **GoDaddy Micro Density**
    A simple App for visual representation of goDaddy Micro Density.
    ''')

    census_starter_df=pd.read_csv('goDaddy/census_starter.csv')
    revealed_test_df=pd.read_csv('goDaddy/revealed_test.csv')
    ss_df=pd.read_csv('goDaddy/sample_submission.csv')
    test_df=pd.read_csv('goDaddy/test.csv')
    train_df=pd.read_csv('goDaddy/train.csv')

    # st.write("""row_id - An ID code for the row.
    # cfips - A unique identifier for each county using the Federal Information Processing System. The first two digits correspond to the state FIPS code, while the following 3 represent the county.
    # county_name - The written name of the county.
    # state_name - The name of the state.
    # first_day_of_month - The date of the first day of the month.
    # microbusiness_density - Microbusinesses per 100 people over the age of 18 in the given county. This is the target variable. The population figures used to calculate the density are on a two-year lag due to the pace of update provided by the U.S. Census Bureau, which provides the underlying population data annually. 2021 density figures are calculated using 2019 population figures, etc.
    # active - The raw count of microbusinesses in the county. Not provided for the test set.""")


    st.title("Demographic Analysis")
    st.write(census_starter_df)
    census(census_starter_df)
    # st.title("Revealed Test")
    # st.write(revealed_test_df)
    # st.title("Sample Submuission")
    # st.write(ss_df)
    # st.title('Test')
    # st.write(test_df)
    # st.title("Train")
    # st.write(train_df)
    revealed_eda(revealed_test_df)

def census(census_df):
    btns_pressed=['pct_bb','pct_college','pct_foreign','pct_it']
    selected_year=st.multiselect('Select the year',['2017','2018','2019','2020','2021'])
    selected_demo=st.multiselect('Select the Demographic',btns_pressed)
    cols_name=census_df.columns
    cols1,cols2=st.columns(2)
    with cols1:
        if len(selected_year)!=0:
            selected_cols_name=[]
            for year_select in selected_year:
                for col_name in cols_name:
                    if year_select in col_name:
                        selected_cols_name.append(col_name)                    
        selected_year_df=census_df[selected_cols_name]
        st.write(selected_year_df)
    with cols2:    
        if len(selected_demo)!=0:
            selected_cols_demo=[]
            for demo in selected_demo:
                for selec_year in selected_cols_name:
                    if demo in selec_year:
                        selected_cols_demo.append(selec_year)
            
            selected_df=census_df[selected_cols_demo]
            st.write(selected_df)    
    try:
        fig=px.line(selected_df)
        fig.update_layout(width=1100,height=500)
        st.plotly_chart(fig)
        st.write('Median HouseHold Income')
        median_col=[]
        for col in selected_cols_name:
            if "median_hh" in col:
                median_col.append(col)
                
        median_Df=census_df[median_col]
        fig1=px.line(median_Df)
        fig1.update_layout(width=1100,height=500)
        st.plotly_chart(fig1)
        
    except:
        st.write("Demographic Chart")
        
            
    
#Function to perfomr EDA for revealed dataset
def revealed_eda(revl_df):
    cols1,cols2=st.columns(2)
    with cols1:
        st.write(revl_df)
    with cols2:
        #Button to show grouped or segregated value for graphs
        grp=st.button('Grouped')
        seg=st.button('Segregated')
        #Selecting the state value
        state_VAl=st.multiselect('Select the State',revl_df.state.unique())
        if len(state_VAl)!=0:
            #specific state df
            state_df=revl_df[revl_df.state.isin(state_VAl)]
            #selected county value
            county_val=st.multiselect("Select the County",state_df.county.unique())
            if len(county_val)!=0:
                #specific county df 
                county_Df=state_df[state_df.county.isin(county_val)]
                st.write(county_Df)
            else:
                st.write("Select County")
        else:
            st.write('Select State')
            
    if grp:
        county_Df=county_Df.groupby('county')['microbusiness_density','active'].mean()
        county_Df.reset_index(inplace=True)
        county_Df.microbusiness_density=county_Df.microbusiness_density*100
        st.write(county_Df)
        fig = px.line(x=county_Df.county, y=county_Df.microbusiness_density, )
        fig.add_bar(x=county_Df.county, y=county_Df.active)
        fig.update_layout(width=1100,height=500)
        st.plotly_chart(fig)
    if seg:
        county_Df.microbusiness_density=county_Df.microbusiness_density*100
        st.write(county_Df)    
        fig = px.line(x=county_Df.row_id, y=county_Df.microbusiness_density, )
        fig.add_bar(x=county_Df.row_id, y=county_Df.active)
        fig.update_layout(width=1100,height=500)
        st.plotly_chart(fig)
        
if __name__=="__main__":
    main()
    




