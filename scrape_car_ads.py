# TURBOCHARGED AD SCRAPER (NO TYPOS, I PROMISE)
import pandas as pd
from nxtscape import scrape_ads  # Correct import

def scrape_dealer_ads():
    print("⚡ Scraping competitor car ads...")
    
    # Target: Facebook Marketplace (cars under $30K)
    ads = scrape_ads(
        url="https://www.facebook.com/marketplace/cars/under-30000",
        selectors={
            "title": "div.ad-title",
            "price": "div.ad-price", 
            "mileage": "div.ad-mileage"  # Corrected spelling
        }
    )
    
    # CarMax-style depreciation alerts
    ads["price_drop_risk"] = ads["price"].apply(
        lambda x: "⚠️" if int(x.replace("$","").replace(",","")) > 25000 else "✅"
    )
    
    ads.to_csv("hot_car_ads.csv", index=False)
    print(f"🔥 Saved {len(ads)} ads to 'hot_car_ads.csv'")
    return ads

if __name__ == "__main__":
    scrape_dealer_ads()  # Correct function name
