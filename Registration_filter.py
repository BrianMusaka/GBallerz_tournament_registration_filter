import pandas as pd
import re

# Load tournament registrations
df = pd.read_csv("tournament_registrations.csv")

def is_valid_whatsapp(number):
    number = str(number).strip()
    return bool(re.fullmatch(r"\d{10,13}", number))

def validate_row(row):
    if pd.isna(row["Captain Name"]) or row["Captain Name"].strip() == "":
        return False
    if pd.isna(row["Team Name"]) or row["Team Name"].strip() == "":
        return False
    if pd.isna(row["Team Colour"]) or row["Team Colour"].strip() == "":
        return False
    if not (6 <= row["Number of Players"] <= 10):
        return False
    if not is_valid_whatsapp(row["WhatsApp Number"]):
        return False
    return True

# Apply validation
df["Valid Entry"] = df.apply(validate_row, axis=1)

# Separate valid and invalid teams
valid_teams = df[df["Valid Entry"] == True]
invalid_teams = df[df["Valid Entry"] == False]

# Export results

#Time to get this money boi!
valid_teams.to_csv("approved_teams.csv", index=False)
invalid_teams.to_csv("rejected_teams.csv", index=False)

print("Validation complete.")
print(f"Approved teams: {len(valid_teams)}")
print(f"Rejected entries: {len(invalid_teams)}")
