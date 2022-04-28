# Databricks notebook source
pip install -r src/requirements.txt

# COMMAND ----------

import os
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

project_root = os.getcwd()

bootstrap_project(project_root)

with KedroSession.create(project_path=project_root) as session:
    session.run()
