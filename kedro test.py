# Databricks notebook source
import logging
logger = spark._jvm.org.apache.log4j
logging.getLogger("py4j.java_gateway").setLevel(logging.ERROR)

# COMMAND ----------

pip install -r src/requirements.txt

# COMMAND ----------

import os
os.getcwd()

# COMMAND ----------

# MAGIC %sh touch /Workspace/Repos/cara.phillips@databricks.com/iris-databricks/logs/log.txt

# COMMAND ----------

import os
from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

project_root = os.getcwd()

bootstrap_project(project_root)

with KedroSession.create(project_path=project_root) as session:
    session.run()

# COMMAND ----------

dbutils.fs.mkdirs("Workspace/Repos/cara.phillips@databricks.com/iris-databricks/data/01_raw")

# COMMAND ----------

dbutils.fs.cp('dbfs:/FileStore/iris-2.csv', "Workspace/Repos/cara.phillips@databricks.com/iris-databricks/data/01_raw")

# COMMAND ----------

dbutils.fs.cp('dbfs:/FileStore/iris-2.csv', 'iris-databricks/data/01_raw')

# COMMAND ----------

dbutils.fs.ls("dbfs:/iris-databricks/data/01_raw/")

# COMMAND ----------

dbutils.fs.rm("dbfs:/Workspace", recurse = True)

# COMMAND ----------

display(dbutils.fs.mounts())

# COMMAND ----------

dbutils.fs.mount(
  source = "wasbs://iris@demostordb.blob.core.windows.net",
  mount_point = "/mnt/iris",
  extra_configs = {"fs.azure.sas.iris.demostordb.blob.core.windows.net":"sp=r&st=2022-05-02T20:45:21Z&se=2023-05-03T04:45:21Z&spr=https&sv=2020-08-04&sr=c&sig=V6SmDPIGHQo6ACtpKFEbx54K0xX6yLm3Y70imST9chw%3D"})

# COMMAND ----------

display(spark.read.csv('/mnt/iris/iris.csv'))
