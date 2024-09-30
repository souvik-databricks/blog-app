# Databricks notebook source
import datetime

# COMMAND ----------

dbutils.widgets.removeAll()
dbutils.widgets.text("email","", "email")
dbutils.widgets.text("text","","text")
text = dbutils.widgets.get("text")
email = dbutils.widgets.get("email")

# COMMAND ----------

dbutils.notebook.exit(f"""
                      [{datetime.datetime.now()}] 
                      Following text was used for process: {text}
                      Report will be sent to: {email}""")
