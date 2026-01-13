# Fresher Job Scraper – Real-Time Entry-Level Job Monitoring System

A Python-based job scraping tool that collects real-time fresher and entry-level job postings from multiple job platforms. The application automates job searches using predefined keywords and location filters, fetching only the latest jobs posted within the last one hour and exporting them to a CSV file for easy tracking.

---

## Features
- Scrapes fresher and entry-level job postings
- Supports multiple job platforms (Indeed, LinkedIn, Google Jobs, Glassdoor)
- Filters jobs posted within the last 1 hour
- Location-based search (Bengaluru, Karnataka — configurable as required)
- Exports results to a CSV file
- Useful for daily job monitoring and analysis

---

## Tech Stack
- Language: Python (version 3.8 or higher)
- Libraries: jobspy, csv
- Output Format: CSV

---

## Project Structure

fresher-job-scraper/
├── job_scraper.py
└── fresher_jobs_last_1_hour.csv



---

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/fresher-job-scraper.git


### 2. Check Python Version

python --version

Python 3.8 or above is required.

### 3. Install Dependencies

pip install jobspy


### 4. Run the Script
python job_scraper.py


---

## Output
The script generates a CSV file containing the latest fresher job postings:

fresher_jobs_last_1_hour.csv


---

## Use Case
This project helps fresh graduates and entry-level candidates stay updated with newly posted job opportunities without manually checking multiple job portals.

---

## Notes
- This project is intended for learning and automation practice
- Job availability depends on platform updates and search limits

---

