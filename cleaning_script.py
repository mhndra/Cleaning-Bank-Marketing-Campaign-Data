import pandas as pd
import numpy as np

# Extract data from the CSV file
df = pd.read_csv("bank_marketing.csv")

# Clean and transform client data
client_columns = [
    "client_id",
    "age",
    "job",
    "marital",
    "education",
    "credit_default",
    "mortgage",
]
client = df[client_columns].copy()
client["job"] = client["job"].str.replace(".", "_", regex=False)
client["education"] = (
    client["education"].str.replace(".", "_", regex=False).replace("unknown", np.nan)
)
client["credit_default"] = client["credit_default"].map(
    {"no": False, "unknown": False, "yes": True}
)
client["mortgage"] = client["mortgage"].map(
    {"no": False, "unknown": False, "yes": True}
)

# Clean and transform campaign data
campaign_columns = [
    "client_id",
    "number_contacts",
    "contact_duration",
    "previous_campaign_contacts",
    "previous_outcome",
    "campaign_outcome",
    "month",
    "day",
]
campaign = df[campaign_columns].copy()
campaign["previous_outcome"] = campaign["previous_outcome"].replace(
    {"failure": False, "nonexistent": False, "success": True}
)
campaign["campaign_outcome"] = campaign["campaign_outcome"].map(
    {"no": False, "yes": True}
)
# Extract and clean date information
month_map = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}
campaign["month"] = campaign["month"].map(month_map)
campaign["last_contact_date"] = pd.to_datetime(
    {"year": 2022, "month": campaign["month"], "day": campaign["day"]}
)
campaign.drop(columns=["month", "day"], inplace=True)

# Clean and transform economics data
economics_columns = ["client_id", "cons_price_idx", "euribor_three_months"]
economics = df[economics_columns].copy()

# Save the cleaned data to CSV files
client.to_csv("client.csv", index=False)
campaign.to_csv("campaign.csv", index=False)
economics.to_csv("economics.csv", index=False)
