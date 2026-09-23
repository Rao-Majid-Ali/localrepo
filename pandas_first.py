import pandas as pd
import numpy as np

# #Series in pandas (1D labeled array)
# s = pd.Series([1,2,3,4,5], index=["majid","manan","rana","ahmad","bilal"])
# s1 = pd.Series([23, 24, 25, 26], index = ["Adam", "Eve", "Charlie", "Bob"])

# print(s)

# print(s["ahmad"])
# print(s["rana"])
# print(type(s))
# print(s.index)

# # Vectorized operations in pandas
# s1 = pd.Series([1,2,3,4,5])
# s2 = pd.Series([6,7,8,9,10])
# print(s1+s2)

# #pandas Series are mutable but size is immutable
# s1[0] = 100
# print(s1)
# changed_s1 = s1.drop(0)  #we hve to create a new deried to add or drop element
# print(changed_s1)


# DataFrame in pandas (2D labeled array)
#create dataframe from dictionary
# info = {
#     "Name" : ["Adam","bob","Eve"],
#     "Age" : [23,24,25],
#     "GPA" : [3.5, 3.7,3.9]
# }
# df = pd.DataFrame(info)
# print(info)
# print(df)
# print(df.index)
# print(df.columns)

# #create dataframe from list of lists
# df = pd.DataFrame([["Adam",23],["Bob",24],["Eve",25]],columns=["Name","Age"])
# print(df)

#create dataframes from numpy arrays
# np_array = np.array([[1,2,3,],[6,7,8,]])
# df = pd.DataFrame(np_array,columns=['A','B','C'])
# print(df)



# work with csv files
# df = pd.read_csv("employee_data.csv")
# print(df,"\n",type(df))

# #same as these  but data load by pandas is same in dataframes
# df = pd.read_json("employee_data.csv")
# df = pd.read_excel("employee_data.csv")
# df = pd.read_sql("employee_data.csv")



#Methods in dataframes
# df = pd.read_csv("employee_data.csv")
# print(df,"\n",type(df))
# print(df.head(2)) #just gives starting 5 rows and according to parameter
# print(df.head()) #just gives starting 5 rows and according to parameter
# print(df.tail(2)) # just gives last rows acording to parameter
# print(df.sample(2))# just gives last rows acording to parameter & default is 1

# print(df.info())#gives the summary of our data
# print(df.shape) #gives us tuple which tells us shape
# print(df.describe()) # gives us summary for only numerical columns & in this with (%) is percentile
# print(df.columns)
# print(df.nunique()) # gives us total num of unique rows in a specific column


# df = pd.read_csv("globalAirQuality.csv")
# print(df.describe())
# print(df.sample(15))


 
#selecting data
#row values
# print(df["city"]) # select column
# print(df[["city","aqi"]])# select multiple colunm

#columns values
# print(df.loc[0]) ## select row through label (in this data set idx and label are same)
# print(df.loc[0:2]) # start label : end label ( end is also included)

# print(df.iloc[0]) ## select row through index (in this data set idx and label are same)
# print(df.iloc[0:2]) # start indx : end idx ( end is not included)

# #cels row,column
# print(df.loc[0,"aqi"]) #only  single
# print(df.loc[0,["city","aqi"]]) #only  single we have to give row index and col label
# print(df.loc[4:8,["city","aqi"]]) #only  single

# print(df.columns)
# print(df.iloc[0,[2,11]]) #we want to give index of columns in iloc
# print(df.iloc[0:3,1:5]) #we want to give index of columns in iloc



# Filtering Data
# print(df[df["aqi"]>130])
# print(df[(df["aqi"] > 130) & (df["temperature"] < 30)])
# print(df[(df["aqi"] > 130) & (df["temperature"] < 30) ][["city","aqi"]])
# aqi_data = df[(df["aqi"] > 130) & (df["temperature"] < 30) ][["city","aqi"]]
# print(aqi_data.iloc[0])
# print(aqi_data.loc[0]) #Error it does not work for loc bcause 0 label does not exist in filter
# print(aqi_data.loc[3])  # label first has 3 val




# Filtering Data through Query Method
# print(df.query("aqi > 150"))
# print(df.query("aqi > 150 & temperature > 30"))
# print(df.query("aqi > 150 & temperature > 30")[["city","aqi"]]) # include chaining

# aqi_val = 160
# print(df.query("aqi > @aqi_val & temperature > 30")) # we can also use py varivales with @



#cleaning of data

# handle mising Values
# isnull()/ina() , isnull().sum() , dropna() , fillna(value) , ffill() , bfill()

df = pd.read_csv("raw_data.csv")  
# print(df.isnull()) # gives true where null/NaN  (not a number)
# print(df.isnull().sum()) # coun num of null in column
# print(df.dropna()) # drop the rows where null val exists
# print(df.dropna(axis=1)) # drop the columns where null val exists

# print(df.fillna(0)) # fill the mising val iwth parameter val
# print(df.fillna(100)) # fill the all mising val iwth parameter val

# age_mean = df["age"].mean()
# cleaned_data = df.copy()
# age_mean = cleaned_data["age"].mean()
# cleaned_data["age"] = cleaned_data["age"].fillna(age_mean)
# print(cleaned_data)

# print(df.ffill()) # forward fill  go from up to down in col and fill the missing with val that i can readed lastly (as from upper in col raeded)
# print(df.bfill()) # backward fill  go from down to up in col and fill the missing with val that i can readed lastly (as from downward in col raeded)
# print(d.ffill())


# cleaning data from duplicate values
# print(df.duplicated()) # used to find where duplicate val exists
# print(df["country"].duplicated())
# print(df[["country", "g/ender"]].duplicated())

# print(df.drop_duplicates())  # it remves the duplicate row but not in originl data
# df2 = df.copy()
# # df.drop_duplicates(inplace=True) # this effect our orginal data
# # print(df)
# df = df2
# print(df)


# Handle Data Types & date-time
# print(df.dtypes) # tells the data type

# df2 = df.copy()
# df2 = df2.fillna(0)
# df2["age"] = df2["age"].astype("int64")
# print(df2 .dtypes)

# to_datetime()  # this function is useful for date and time


#clening data  
#handle strings

# print(df["gender"].str.lower())
# print(df["gender"].str.upper())
# print(df["gender"].str.capitalize())
# print(df["gender"].str.strip()) # renoves the exra spaces

print(df["name"].str.split(" ")) # separaete the data accrding to parameter

print(df["country"].str.contains("USA")) # case senstive
print(df["country"].str.contains("india",case = False)) # not case sestive
