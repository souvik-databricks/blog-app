import datetime
import streamlit as st
from utils import databricks_instance, trigger_job_run_func, user_info

st.set_page_config(page_title="Blog-Job-Runner-App", layout="wide")


# Function to validate and process input
def process_input():
    id_input = st.session_state.job_id
    user_input = st.session_state.name_input
    email = st.session_state.email_input

    if id_input.isnumeric():
        id_input = int(id_input)
        job_trigger_response = trigger_job_run_func(user_input, id_input, email)
        if "run_id" in job_trigger_response.keys():
            current_run_id = job_trigger_response["run_id"]
            st.write(f"""
                        [{datetime.datetime.now()}] 
                        Job was triggered with run id: {current_run_id}
                        Report will be sent to: {email}
                    """)
        else:
            if job_trigger_response["error_code"] in ["PERMISSION_DENIED","UNAUTHORIZED"]:
                st.error("You don't have permission to run the job.")
            else:
                st.error("Unexpected error occured.")
    else:
        st.error("Invalid job id. Job id can only be numeric.")


st.header("Lakehouse app - Job runner demo")

with st.form("inputs_form"):
    job_id = st.text_input("Enter Job id", key="job_id")
    user_input = st.text_input("Enter name (optional)",key="name_input")
    email = st.text_input("Enter email (optional)",value=user_info['user_email'] ,key="email_input")
    submit_button = st.form_submit_button("Trigger Job")

# Call function when button is clicked
if submit_button:
    process_input()


