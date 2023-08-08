import pandas as pd
import pickle
import streamlit as st
import numpy as np

model = pickle.load(open(r"titanic_victor.pkl",'rb'))


## Main Function

def main():
    st.title("Titanic Survival Prediction")
    ##st.image("r.jpg",caption="Sinking of the Titanic RMS : 15th April 1912 in North Atlantic Ocean",use_column_width=True)
    st.write(""" Would you have Survived The Titanic Disaster ?""")


    ## Sidebar Configurations
    st.sidebar.header("By Victor Hugo Bisangwa")
    st.sidebar.markdown("Phone: 0789066369")
    st.sidebar.markdown("Email: Vikathugo91@gmail.com")
    st.write("##### Check What could have happend to you if you were on the RMS Titanic")

    #UI Structure
    Age = st.slider("Enter Your Age:",1,75,30)

    Pclass = st.selectbox("Select Passenger-Class:",[1,2,3])

    Sex = st.selectbox("Select Gender:",["Male","Female"])
    if(Sex == "Male"):
        Sex=0
    else:
        Sex=1
    
    fare = st.slider("Fare (Ticket Price):",15,500,40)

    Family = st.selectbox("Select Total Family Mmebers:",[0,1,2,3,4,5,6,7,10])

    #Getting Data and Framing
    data={"Pclass":Pclass,"Sex":Sex,"Age":Age,"Family":Family,"Fare":fare}

    df=pd.DataFrame(data,index=[0])
    return df

data = main()

##Prediction:

if st.button("Predict"):
    result = model.predict(data)
    proba = model.predict_proba(data)

    if result[0] ==1:
        st.write("Congartulations You Probably Would have Survived")
        st.image("titanic_rescueing.jpg",caption='Surviving the RMS Titanic',use_column_width=True)
    
    else:
        st.write("Better Luck Next Time, You Probabaly Would have Died!")
        st.image("titanic_sinking.jpg",caption='Death',use_column_width=True)
    
    

