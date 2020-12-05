import streamlit as st
import pandas as pd
import sklearn
import keras
import numpy as np
from names import get_full_name

st.title("Voorspel je punt voor een wiskunde toets op basis van een aantal gegevens")
st.write("""
*door Ricky van den Berg*

# Disclaimer
De data die gebruikt is om het model te maken is fictief.
Daarom is de voorspelling die hier wordt gedaan niet betrouwbaar.
Echter zou het model in een later stage vervangen kunnen worden door "echte" data.

# Toelichting
Deze app maakt voorspellingen op basis van een aantal persoonlijke gegevens.
Voorspellingen kunnen gebruikt worden om inzicht te krijgen in hoe goed je een wiskunde toets gaat maken.
Ook kan je met de variabelen spelen om te kijken of dit je resultaat beinvloed.


\n\n

# Prediction
""")


raw = pd.read_csv("students.csv")
raw = pd.get_dummies(
    raw, columns=['gender', 'race', 'lunch', 'education_parent', "test_prep"])
dataframe = raw.head(1).drop("math", axis=1)

st.sidebar.write("Fill in your data")
gender = st.sidebar.selectbox("gender", ["Male", "Female"])
dataframe["gender_female"] = gender == "Female"
dataframe["gender_male"] = gender == "Male"

race = st.sidebar.selectbox(
    "Race", ["Elf", "Dwarf", "Halfling", "Orc", "Human"])
dataframe["race_group A"] = race == "Female"
dataframe["race_group B"] = race == "Dwarf"
dataframe["race_group C"] = race == "Halfling"
dataframe["race_group D"] = race == "Orc"
dataframe["race_group E"] = race == "Human"

lunch = st.sidebar.selectbox("Lunch Type", ["reduced (free)", "Standard"])
dataframe["lunch_free/reduced"] = lunch == "reduced (free)"
dataframe["lunch_standard"] = lunch == "Standard"

edu_parent = st.sidebar.selectbox("Parents education", [
    "Associate's Degree", "Bachelor's Degree", "High School", "Master's Degree", "College"])
dataframe["education_parent_associate's degree"] = edu_parent == "Associate's Degree"
dataframe["education_parent_bachelor's degree"] = edu_parent == "Bachelor's Degree"
dataframe["education_parent_high school"] = edu_parent == "High School"
dataframe["education_parent_master's degree"] = edu_parent == "Master's Degree"
dataframe["education_parent_some college"] = edu_parent == "College"

test_prep = st.sidebar.checkbox("I have completed the practice")
dataframe["test_prep_completed"] = test_prep == 1
dataframe["test_prep_none"] = test_prep == 0

dataframe["reading"] = st.sidebar.slider(
    "Reading Skill", min_value=0, max_value=100, value=50, step=1)
dataframe["writing"] = st.sidebar.slider(
    "Writing Skill", min_value=0, max_value=100, value=50, step=1)

st.write("## Model Predict")
model = keras.models.load_model("student.h5")
dataframe = np.asarray(dataframe).astype(np.float32)
results = model.predict(dataframe)
st.write(results)
