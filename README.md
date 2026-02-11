# GBallerz_tournament_registration_filter
Python script to filter out all unnecessary or half-done registrations.

## Problem
Manual registration via Google Forms caused:
- Incomplete forms
- Invalid player counts
- Fake or incorrect contact details

## Solution
A Python script that:
- Ensures team size is between 6 and 10 players
- Checks WhatsApp number validity
- Automatically separates valid and invalid registrations

## Tools Used
- Python
- pandas
- CSV (Google Forms export)

## How to Run
1. Export Google Form responses as CSV
2. Place the file in the project directory
3. Run:
```bash
python filter_registrations.py
