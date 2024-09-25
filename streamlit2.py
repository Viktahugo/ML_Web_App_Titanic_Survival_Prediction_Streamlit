import pandas as pd
import pickle
import streamlit as st 
import numpy as np



#Lets Load the Model into a variable named Model

Model = pickle.load(open(r"titanic_model","rb"))



def main():
    st.title("Titanic Survival Predcition By Victor Hugo Bisangwa")
    st.write("Would You HAve Survived the Titanic Disaster?")

    # Lets Take a look at the Sidebar#

    st.sidebar.header("Done By Victor HUgo Bisangwa")
    st.sidebar.markdown("Phone:0789066369")
    st.sidebar.markdown("Email:viktahugo91@gmail.com")


    # THE UI STRUCTURE

    Age = st.slider("Enter Your Age:",1,75,30)
    Pclass = st.selectbox("Select Passgenger Class:",[1,2,3])
    Sex = st.selectbox("Select Gender:",["Male","Female"])
    if(Sex == "Male"):
        Sex = 0
    else:
        Sex = 1

    fare = st.slider("Select Your Fare:",15,500,40)
    family = st.selectbox("Select Number of Family Members",[0,1,2,3,4,5,6,7,8,9,10])


    #Getting the Data
    data = {"Pclass":Pclass,"Sex":Sex,"Age":Age,"Family":family,"Fare":fare}

    #Framing
    df=pd.DataFrame(data,index=[0])
    return df

data = main()


#Prediction

if st.button("Predict"):
    result = Model.predict(data)
    proba = Model.predict_proba(data)
    
    if result[0]==1:
        st.write("Congratulations You Would Have Probably Survived")
        st.image("survive.jpeg",caption="Survival Yeah!",use_column_width=True)
    
    else:
        st.write("Too Bad For You, You would Probably HAve Perished!")
        st.image("death.jpeg",caption="Death",use_column_width=True)


