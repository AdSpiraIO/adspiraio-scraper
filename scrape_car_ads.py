# SIMPLE STARTER SCRIPT (we'll add more later)
import pandas as pd

def safe_scrape():
    print("🛠️ Building your ad engine...")
    
    # TEST DATA (we'll add real scraping next)
    test_ads = pd.DataFrame({
        "Car": ["2022 Tesla Model 3", "2021 Ford F-150"],
        "Price": ["$38,500", "$29,999"],
        "Status": ["TEST DATA", "TEST DATA"]
    })
    
    test_ads.to_csv("car_ads.csv", index=False)
    print("✅ Saved test ads to 'car_ads.csv'")
    return test_ads

if __name__ == "__main__":
    safe_scrape()
