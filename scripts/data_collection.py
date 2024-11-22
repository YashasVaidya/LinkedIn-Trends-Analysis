import pandas as pd

def collect_data():
    # Placeholder for data collection logic
    # This could be manual data entry or API calls
    data = {
        'Post Title': [],
        'Post Date': [],
        'Reactions': [],
        'Comments': [],
        'Follower Count': []
    }
    
    # Example: Append collected data to the DataFrame
    df = pd.DataFrame(data)
    return df

if __name__ == "__main__":
    collected_data = collect_data()
    print(collected_data)
