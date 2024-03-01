import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from flask import render_template_string
import streamlit as st
from content import *
import random
import pandas as pd

st.set_page_config(layout="centered",
                   page_icon="🎓",
                   page_title="Diploma Generator")
st.title("Performance Review Conversation Starters")

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.md")

form = st.form("template_form")
first_name = form.text_input("First name")
last_name = form.text_input("Last name")

performance_designation = form.selectbox(
  "Performance designation",
  [
    "1 / Does not meet expections", "2 / Partially meets expectations",
    "3 / Meets expectations", "4 / Exceeds Expectations",
    "5 / Greatly Exceeds Expectations"
  ],
  index=0,
)

promo = form.selectbox("Did you put them up for promo?", ["Yes", "No"],
                       index=0)

got_promo = form.selectbox(
  "Did they get the promo?",
  ["N/A", "Yes", "No"],
  index=0,
)

salary_bump = form.selectbox(
  "Getting a salary increase?",
  ["Yes", "No"],
  index=0,
)

bonus = form.selectbox(
  "Getting a bonus?",
  ["Yes", "No"],
  index=0,
)

performance_equity = form.selectbox(
  "Getting a performance equity?",
  ["Yes", "No"],
  index=0,
)

rows = []

if performance_designation in [
    "1 / Does not meet expections", "2 / Partially meets expectations"
]:
  rows.append([
    "The individual gets does not / partially meets expectations",
    random.choice(BAD_PERF)
  ])

if promo == "Yes" and got_promo == "No":
  rows.append(
    ["If the individual didn't get their promo",
     random.choice(NO_PROMO)])

rows.append([
  "The individual is disappointed with their designation (expected higher)",
  random.choice(NOT_HIGHER_DESIGNATION)
])

rows.append([
  "An individual is disappointed that they didn’t get a salary increase",
  random.choice(NO_SALARY_INCREASE),
])

rows.append([
  "A well-performing individual is disappointed that they didn’t get better salary increase",
  random.choice(SALARY_INCREASE_NOT_ENOUGH),
])

rows.append(["If the individual does not get bonus", random.choice(NO_BONUS)])

rows.append([
  "If the individual got bonus last year, but didn't get one this year",
  random.choice(NO_REPEAT_BONUS)
])

rows.append([
  "A well-performing individual does not receive additional equity",
  random.choice(NO_EQUITY)
])

df = pd.DataFrame(rows, columns=("Context", "Conversation Starter"))

submit = form.form_submit_button("Generate")

if submit:
  st.dataframe(df, use_container_width=True, hide_index=True)
  #html = template.render(rows=rows)
  #pdf = pdfkit.from_string(html, False)
  #st.balloons()

  #ight.success("🎉 Your diploma was generated!")
  #html
  #st.write("")
#   right.download_button(
#     "⬇️ Download PDF",
#     data=pdf,
#     file_name="diploma.pdf",
#     mime="application/octet-stream",
#   )