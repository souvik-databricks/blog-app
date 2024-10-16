import datetime
import json
import requests
import streamlit as st
from utils import databricks_instance, user_info, _get_user_credentials

st.set_page_config(page_title="Blog-Job-Runner-App", layout="wide")


def trigger_job_run_func(input_text, jobid, useremail):
    url = f"{databricks_instance}/api/2.1/jobs/run-now"
    headers = _get_user_credentials()
    payload = {
        "job_id": int(jobid),
        "notebook_params": {
            "email": useremail,
            "text": input_text
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()


try:
    st.header("Lakehouse app - Job runner demo")

    job_id = st.text_input("Enter Job id")
    user_input = st.text_input("Enter name (optional)", value=user_info["user_name"])
    user_input = user_input if user_input else user_info["user_name"]
    email = st.text_input("Enter email (optional)", value=user_info["user_email"])
    email = email if email else user_info["user_email"]

    if st.button('Show Run trigger'):
        current_run_id = trigger_job_run_func(user_input, job_id, email)["run_id"]
        st.write(f"""
                        [{datetime.datetime.now()}] 
                        Run of the job was triggered with this run id: {current_run_id}
                        Report will be sent to: {email}
                """)
except Exception as e:
    st.write(e)
    st.write("You don't have permission. Please contact your admin.")
