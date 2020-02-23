import altair as alt
import pandas as pd
import streamlit as st

color_scheme = st.sidebar.selectbox(
        "Project week:",
        ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5"],
    )

st.write("# Integration of the individual reflections")
st.write("### on the learning objectives in a team achievement of learning objectives.")
st.write("# team members score")
st.write("### can be a ranking, or 1‐3 stars) each other’s performance weekly, tips and tops")
st.write("# Progress dashboard")
st.write("### Desirability: what has been achieved, what is evidence, what are next steps?")
st.write("### Feasibility: what has been achieved, what is evidence, what are next steps?")
st.write("### Viability: what has been achieved, what is evidence, what are next steps?")
st.write("### Validation: what has been achieved, what is evidence, what are next steps?")
st.write("# agile project plan")
st.write("### tasks, persons in charge, deliverables, milestones, approach/planned activities")