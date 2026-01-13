import csv
from jobspy import scrape_jobs

jobs = scrape_jobs(
    site_name=[
        "indeed",
        "linkedin",
        "google",
    ],
    search_term=(
        "fresher python developer OR "
        "entry level software engineer OR "
        "junior software developer OR "
        "graduate software engineer OR "
        "data analyst fresher"
    ),
    google_search_term=(
        "fresher OR entry level OR junior "
        "python developer software engineer jobs "
        "near Karnataka posted in last 1 hour"
    ),
    location="Bengaluru, Karnataka, India",
    results_wanted=30,
    hours_old=1,   # 🔥 ONLY LAST 1 HOUR
    country_indeed="INDIA",
    linkedin_fetch_description=True,
)

print(f"Found {len(jobs)} fresher jobs")
print(jobs.head())

jobs.to_csv(
    "fresher_jobs_last_1_hour.csv",
    quoting=csv.QUOTE_NONNUMERIC,
    escapechar="\\",
    index=False
)
