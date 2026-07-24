import requests
import pandas as pd

HANDLE = "Suryansh210207"  
URL = f"https://codeforces.com/api/user.status?handle={HANDLE}"

print("🔄 Fetching your full submission history...")
response = requests.get(URL).json()

if response["status"] == "OK":
    submissions = response["result"]
    
    solved_problems = []
    seen_problems = set() 
    
    for sub in submissions:
        
        if sub["verdict"] == "OK": 
            prob = sub["problem"]
            prob_id = f"{prob.get('contestId', '')}{prob.get('index', '')}"
            
            
            if prob_id in seen_problems:
                continue
                
            seen_problems.add(prob_id)
            
            
            solved_problems.append({
                "ID": prob_id,
                "Name": prob["name"],
                "Rating": prob.get("rating", 0), # 0 means unrated/gym problem
                "Tags": prob["tags"]
            })
    
    
    df = pd.DataFrame(solved_problems)
    
    print(f"\n📊 Data loaded into DataFrame successfully!")
    print(f"Total Unique Problems Solved: {len(df)}")
    print("\n👀 Here is a quick look at your data:")
    print(df.head()) # Prints the top 5 rows of your table
    print("\n🎯 TOP 5 MOST SOLVED TOPICS:")
        # This flattens the lists of tags and counts them up!
    all_tags = df.explode('Tags')
    tag_counts = all_tags['Tags'].value_counts()
    print(tag_counts.head(5))

    print("\n🚨 WEAKEST TOPICS (LEAST SOLVED):")
    print(tag_counts.tail(3))
else:
    print("❌ Failed to fetch data. Double check your handle name!")