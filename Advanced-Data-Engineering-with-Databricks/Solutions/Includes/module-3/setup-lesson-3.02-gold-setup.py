# Databricks notebook source
# MAGIC %run ../_databricks-academy-helper $lesson="3.02"

# COMMAND ----------

# MAGIC %run ../_utility-functions

# COMMAND ----------

DA.cleanup()
DA.init()

# COMMAND ----------

# Create the source datasets
create_source_database()          # Create the source database
create_producer_table_source()    # Clone the producer table
create_date_lookup_source()
create_user_lookup_source()
print()

# Create the user datasets
create_date_lookup()                # Create static copy of date_lookup
create_user_lookup()                # Create the user-lookup table
create_gym_mac_logs()               # Create the gym_mac_logs()
print()

init_source_daily()                 # Create the data factory

# DA.data_factory.load()            # Load one new day for DA.paths.source_daily
# DA.process_bronze()               # Process through the bronze table
# DA.process_heart_rate_silver()    # Process the heart_rate_silver table
# DA.process_workouts_silver()      # Process the workouts_silver table
# DA.process_completed_workouts()   # Process the completed_workouts table
# DA.process_workout_bpm()          # Process the workout_bpm table

# DA.process_users()
# DA.process_user_bins()

# COMMAND ----------

DA.conclude_setup()
