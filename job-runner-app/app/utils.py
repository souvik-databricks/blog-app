import requests
import json
import streamlit as st
from databricks.sdk.core import Config


cfg = Config()

def _get_user_credentials():
    return cfg.authenticate()

def _get_user_info():
    headers = st.context.headers
    return dict(
        user_name=headers.get("X-Forwarded-Preferred-Username"),
        user_email=headers.get("X-Forwarded-Email"),
        user_id=headers.get("X-Forwarded-User")
    )

user_info = _get_user_info()

databricks_instance = cfg.host


def trigger_job_run_func(input_text, jobid, useremail):
    url = f"{databricks_instance}/api/2.1/jobs/run-now"
    headers = _get_user_credentials()
    payload = {
        "job_id": jobid,
        "notebook_params": {
            "email": useremail,
            "text": input_text
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.json()