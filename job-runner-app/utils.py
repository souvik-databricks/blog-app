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