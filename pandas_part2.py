## Transforming Data / Feature Engineering
# for improving the perfomance of our model

import pandas as pd
df = pd.read_csv("raw_data.csv")
df2 = df.copy()
#aplly() is  higher order function which takes another function as a parameter
# df2["tax"] = df["income"].apply(lambda x : "20%" if x >= 60000 else "10%") # we crete a new column

# gender_map = { "Male" : 'M' , "Female" : "F" , "Unkhown" : "U"}
# df2["gender"] = df2["gender"].map(gender_map) # for maping the values in columns

# df2 = df2.assign(new_income = df2["income"]*1.1) # for adding new column

# df2["country"] = df["country"].replace("USA","United states") # for replace old values in col with new values
# print(df2)


# other methods for data transformation
# df2.columns = ["Id","Name","Age","Country","Gender","Income"] # renaming the label of all the columns
# df2 = df2.rename(columns={"Income":"Salary"}) #Renaming te label of the columns
# df2 = df2.rename(index={1:"First"}) #Renaming the label of row

# df2 = df2.sort_values("income") # sort in ascending all the rows by income
# df2 = df2.sort_values("income" , ascending = False) # sort in decending all the rows by income
sorted_df2 = df2.sort_values(["income","age"]) # sor in ascending  all the rows by income but if income is same then it wil see the age
# sorted_df2 = sorted_df2.sort_index() # sort jumbled data in  by index in orginal order
# reset
# sorted_df2 = sorted_df2.reset_index() # create the new label in reset order and preverse the original index
# sorted_df2 = sorted_df2.reset_index(drop = True) # drop the old labels and preserve he new one
# print(sorted_df2)

#ranking
# sorted_df2["Ranking"] = sorted_df2["income"].rank() # giving ranking if income is same then it gives average to both
# sorted_df2["Ranking"] = sorted_df2["income"].rank(ascending = False) # giving 1 to he highest order val
# sorted_df2["Ranking"] = sorted_df2["income"].rank(ascending = False , method = "dense") # it can resolve the ties giving  whole va instead of avg/decimal val
# sorted_df2["Ranking"] = sorted_df2["income"].rank(ascending = False , method = "min" , ) # it can resolve the ties giving  min val if avg is 3.5 it givs 3
# print(sorted_df2)
# sorted_df2["Ranking"] = sorted_df2["income"].rank(ascending = False , method = "max") # it can resolve the ties giving max val like if avg is 3.5 it gives 4
# print(sorted_df2)

#Reordering column
# df2.columns = ["Id","Name","Country","Gender","Income","Age"] # age to the last column
# new_col_order = [col for col in df2.columns if col != "id" ] + ["id"]
# df2 = df2[new_col_order]
# print(df2)



# writing data in csv file
# df2 =  df.copy()
# df2 = df.drop_duplicates()
# df2 = df2.fillna(0)
# df2 = df2.sort_values("income")
# df2 = df2.reset_index(drop = True)
# df2.to_csv("sorted_data.csv") # created a file if no exists and write the data in the file



# Grouping and Aggregation of Data
# print(df.groupby("country")["income"].mean()) # make groupuing on basis of country and give their mean
# print(df.groupby("country")["income"].min())
# print(df.groupby("country")["income"].max())
# print(df.groupby("gender")["income"].min())
# print(df.groupby("gender")["income"].mean())

# print(df.groupby("country")["income"].agg(["mean","min","max"]))  # for multiple aggregate functions
# print(df.groupby("gender")["income"].agg(["mean","min","max"]))

# print(df.groupby("country")["income"].agg(avg_salary="mean",min_salary="min",max_salary="max")) # to include new label names


print(df.groupby("country").agg({ # to apply  different agg function to diff columns
    "income" : "mean",
    "age" : "mean"
}))

print(df.groupby("country").agg({
    "income" : "max",
    "age" : "mean"
}))

print(df.groupby("country").agg(
    max_salary = ("income" , "max"),
    avg_age = ("age" , "mean")
))
