import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

def main():
    
    census_starter_df=pd.read_csv('goDaddy/census_starter.csv')
    revealed_test_df=pd.read_csv('goDaddy/revealed_test.csv')
    ss_df=pd.read_csv('goDaddy/sample_submission.csv')
    test_df=pd.read_csv('goDaddy/test.csv')
    train_df=pd.read_csv('goDaddy/train.csv')

    st.write("""row_id - An ID code for the row.
    cfips - A unique identifier for each county using the Federal Information Processing System. The first two digits correspond to the state FIPS code, while the following 3 represent the county.
    county_name - The written name of the county.
    state_name - The name of the state.
    first_day_of_month - The date of the first day of the month.
    microbusiness_density - Microbusinesses per 100 people over the age of 18 in the given county. This is the target variable. The population figures used to calculate the density are on a two-year lag due to the pace of update provided by the U.S. Census Bureau, which provides the underlying population data annually. 2021 density figures are calculated using 2019 population figures, etc.
    active - The raw count of microbusinesses in the county. Not provided for the test set.""")


    # st.title("Censur Starter")
    # st.write(census_starter_df)
    # st.title("Revealed Test")
    # st.write(revealed_test_df)
    # st.title("Sample Submuission")
    # st.write(ss_df)
    # st.title('Test')
    # st.write(test_df)
    # st.title("Train")
    # st.write(train_df)
    revealed_eda(revealed_test_df)

def revealed_eda(revl_df):
    st.write("Main")
    cols1,cols2=st.columns(2)
    with cols1:
        st.write(revl_df)
    with cols2:
        state=st.multiselect('Select the State',revl_df.state.unique())
        county=st.multiselect("Select the County",revl_df.county.unique())

if __name__=="__main__":
    main()
    




