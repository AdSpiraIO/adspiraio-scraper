# SUPER SIMPLE STARTER (we'll tweak later)
import pandas as pd

def scrape_ads():
    print("🔥 Fake data for now—replace with nxtscape later!")
    fake_ads = pd.DataFrame({
        "Car": ["2021 Tesla", "2020 Ford F-150"],
        "Price": ["$45,000", "$28,500"]
    })
    fake_ads.to_csv("scraped_ads.csv")
    return fake_ads

if __name__ == "__main__":
    scrape_ads()
