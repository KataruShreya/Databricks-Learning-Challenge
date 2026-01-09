data = [("Shreya", 25), ("Alex", 30), ("Ravi", 28)]
columns = ["Name", "Age"]

#dataframe creation and display
df = spark.createDataFrame(data, columns)
df.show()

#printing the schema
print("SCHEMA:")
df.printSchema()

#displaying one column
print("Display of a column")
df.select("Name").show()

#filtering
print("Filtering")
df.filter(df.Age > 26).show()

#renaming a column
print("Renaming a column")
df_renamed = df.withColumnRenamed("Age", "User_Age")
df_renamed.show()