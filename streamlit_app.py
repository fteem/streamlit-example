import streamlit as st
from content import *
from framework_content import *
import random
from jinja2 import Environment, FileSystemLoader

st.set_page_config(layout="centered",
                   page_icon="💼",
                   page_title="Performance Review Conversation Starters")
st.title("Performance Review Conversation Starters")

environment = Environment(loader=FileSystemLoader("."))
scenarios_template = environment.get_template("scenarios.html")
framework_template = environment.get_template("framework.html")

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

scenarios = []
framework = []

framework.append([
  "Set up the conversation and the tone of the meeting",
  """
  Open the meeting thanking them for taking the time and give high level overview:

  * "%s"
  
  Explain that it's not only about looking back, but also forward:
  * "%s"
  * "%s"
  
  Reinforce the idea that it's a 2-way conversation:
  * "%s"

  Prepare them for the next section:  
  * "%s"

  Check in before diving in:  
  * "How does that sound?"
  """ % (random.choice(OPENING), random.choice(ATMOSPHERE), random.choice(GOALS), random.choice(TWO_WAY), random.choice(NEXT_SECTION_PREP))
])

framework.append([
  "Summarize performance results, feedback and outcomes",
  """
  Start by acknowledging their contributions and efforts.

  * "%s"
  * "%s"

  Emphasize their strengths.
  * "%s"

  Link their performance to specific recognitions and potential for growth.
  * "Based on the significant impact of your contributions in areas X, Y, and Z, you've been awarded a XX performance designation, and identified as a Future Leader. Your exceptional talent is crucial to our success, and I'm enthusiastic about what lies ahead for you."
  * "Your consistent performance at an advanced level has been indispensable, leading to your promotion. Congratulations! I'm keen to discuss the broader influence you can wield at this new tier..."

  Clarify decisions around non-promotion.
  * "If you were anticipating a promotion and it didn't happen, I understand your disappointment. Let's discuss the reasons behind this decision, whether they stem from performance or organizational needs, and how we can target your career aspirations moving forward."

  View developmental feedback as a stepping stone for advancement.
  * "Let's examine areas where there's room for improvement. Here are the observations from myself and your peers... Which areas do you believe should be prioritized? How can I assist you in this journey?"

  Gauge their reaction to the feedback.
  * "How does this feedback sit with you? Does it align with your own observations?"
  """ % (random.choice(GRATITUDE), random.choice(REFLECTION), random.choice(SHOWCASE))
])

framework.append([
  "Talk about their future in the company and the team, and how they want to develop their career ",
  """
  Ask about what are their growth aspirations:

  * "I'd like to explore specific opportunities that align with your personal and professional growth. Are there particular projects that excite you? Are there any leaders within the organization you're eager to learn from or collaborate with? What competencies are you looking to enhance?"

  Link back to previous discussions about career advancement:
  * "Reflecting on our past discussions about your career path, let's review the progress you've made, any new directions you're considering, and how I can assist you in achieving your goals."
  """
])

framework.append([
  "Talk about compensation",
  """
  Start on the same page:

  * Reiterate your company's total compensation package setup. Usually companies the following compensation structure: base salary,  equity, bonus, and additional performance-based equity.

  Start with a summary:
  * "Given your contributions this year, including leading the [specific project] to success, you'll receive a [specific perctengate] salary increase, [specific amount] bonus, and [specific amount] equity refresh. This reflects our appreciation for your hard work and the value you bring to our team."
  
  When discussing salary bumps, spell out the math for them:
  * "You get a 5% raise to your base. Starting next month, instead of your old salary of 100K, your new annual base salary will be 105K." 
  
  When you go into the bonus, explain the bonus structure:
  * "Per your contract, your bonus is 15%. Based on your performance designation, you're rewarded with 150% of your bonus. In other words, your bonus is your base salary * 0.15 * 1.5 = 22.5K"
  
  When discussing equity, continue diving into the numbers.
  * "This year you are awarded a [specific amount] of equity. It will be vesting quarterly over 1 year. Vesting will commence on April 1, this year."
 
  Make sure the math checks out:
  * The last thing you want to happen is to miscalculate or incorrectly explain any compensation outcomes. Take your time; don't rush it. If the math doesn't work, either try to debug on the spot with the individual or say that you'll ping HR to get help, and you will follow up with the individual ASAP.
  """  
])

framework.append([
  "Close off",
  """
  Celebrate their achievements:

  * "Well done on an outstanding year and achieving your [specific performance designation] designation. It's truly a pleasure having you as part of our team, and I'm looking forward to supporting your continued development."

  Follow up on the action items from the discussion:

  * "Based on our conversation, I take the following actions [specify actions related to completing the action items]."
  """  
])

if performance_designation in [
    "1 / Does not meet expections", "2 / Partially meets expectations"
]:
  scenarios.append([
    "The individual gets does not / partially meets expectations",
    random.choice(BAD_PERF)
  ])

if promo == "Yes" and got_promo == "No":
  scenarios.append(
    ["If the individual didn't get their promo",
     random.choice(NO_PROMO)])

if performance_designation in ["3 / Meets expectations", "4 / Exceeds expectations"]:
  scenarios.append([
    "The individual is disappointed with their designation (expected higher)",
    random.choice(NOT_HIGHER_DESIGNATION)
  ])

if salary_bump == "No":
  scenarios.append([
    "An individual is disappointed that they didn’t get a salary increase",
    random.choice(NO_SALARY_INCREASE),
  ])

if salary_bump == "Yes":
  scenarios.append([
    "A well-performing individual is disappointed that they didn’t get better salary increase",
    random.choice(SALARY_INCREASE_NOT_ENOUGH),
  ])

if bonus == "No":
  scenarios.append(["If the individual does not get bonus", random.choice(NO_BONUS)])

  scenarios.append([
    "If the individual got bonus last year, but didn't get one this year",
    random.choice(NO_REPEAT_BONUS)
  ])

if performance_equity == "No":
  scenarios.append([
    "A well-performing individual does not receive additional equity",
    random.choice(NO_EQUITY)
  ])


submit = form.form_submit_button("Generate")

if submit:
  st.write("<h3>Main conversation<h3/>", unsafe_allow_html=True)
  conversations_content = framework_template.render(rows=framework)
  st.write(conversations_content, unsafe_allow_html=True)
  st.write("<br/><br/><br/>", unsafe_allow_html=True)

  scenarios_content = scenarios_template.render(rows=scenarios)
  st.write("<h3>Conversation scenarios<h3/>", unsafe_allow_html=True)
  st.write(scenarios_content, unsafe_allow_html=True)