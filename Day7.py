import json
file_name = "store_data.json"
def load_data(file_name):
    with open(file_name,"r") as f:
            data = json.load(f)
    return data
   
data2 = load_data(file_name)

# Cleaning and structuring data
def clean_data(data1):
    cleaned_data = []
    unique_user = set()
    text_to_num = {"one":1,"two":2,"three":3,"four":4,"five":5}
    for user in data1:
        #clean rating 
        raw_rating = str(user["rating"]).strip().lower()
        if (raw_rating in text_to_num):
            raw_rating = text_to_num[raw_rating]
        user["rating"] = raw_rating

        #handing missing values
        raw_age = user.get("age")
        if(raw_age == None):
            user["age"] = None
         
        #Depulication
        if (user["name"].strip() in unique_user):
            continue
        unique_user.add(user["name"])
        cleaned_data.append(user)
    return cleaned_data
                
print(clean_data(data2))
data3 = clean_data(data2)

# Get the meaningful insughts from data
def get_insights(data3):

    #avg rating
    tol_rating = 0
    count = 0
    for user in data3:
        tol_rating += float(user["rating"])
        
    print("avg rating =  ",tol_rating/len(data2))

get_insights(data3)

# percentage of user wih poor raing
poor_ratings = 0
for user in data3:
    if (float(user["rating"]) < 3):
        poor_ratings += 1
print(f"% of the poor rating users =  {poor_ratings/len(data3)*100}%")


# Recommendation feature
def get_recommendation(data3):
    recommendation = []    
    for user in data3:
        cur_recom = {}
        cur_recom["name"] = user["name"]
        if (float(user["rating"]) >= 4):
            cur_recom["brand"] = "Apple"
        else:
            cur_recom["brand"] = "Samsung"
        recommendation.append(cur_recom)
    return recommendation
print(get_recommendation(data3))
