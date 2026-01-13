project:
  name: Fresher Job Scraper
  title: Fresher Job Scraper – Real-Time Entry-Level Job Monitoring System
  description: >
    A Python-based job scraping tool that collects real-time fresher and
    entry-level job postings from multiple job platforms. The application
    automates job searches using predefined keywords and location filters,
    fetches jobs posted within the last one hour, and exports the results
    to a CSV file for easy tracking.

features:
  - Scrapes fresher and entry-level job postings
  - Supports multiple job platforms (Indeed, LinkedIn, Google Jobs, Glassdoor)
  - Filters jobs posted within the last 1 hour
  - Location-based search (Bengaluru, Karnataka – configurable)
  - Exports results to CSV
  - Useful for daily job monitoring and analysis

tech_stack:
  language:
    name: Python
    version_required: ">=3.8"
  libraries:
    - jobspy
    - csv
  output_format: CSV

project_structure:
  fresher-job-scraper:
    - job_scraper.py
    - fresher_jobs_last_1_hour.csv
    - README.yaml

setup:
  steps:
    - step: Clone repository
      command:
        - git clone https://github.com/your-username/fresher-job-scraper.git
        - cd fresher-job-scraper

    - step: Check Python version
      command:
        - python --version
      note: Python 3.8 or higher is required

    - step: Create virtual environment
      command:
        - python -m venv venv

    - step: Activate virtual environment
      windows:
        - venv\\Scripts\\activate
      linux_mac:
        - source venv/bin/activate

    - step: Install dependencies
      command:
        - pip install jobspy

    - step: Run the script
      command:
        - python job_scraper.py

output:
  file_generated: fresher_jobs_last_1_hour.csv
  description: Contains the latest fresher and entry-level job postings

use_case:
  - Helps fresh graduates track newly posted jobs automatically
  - Eliminates the need to manually check multiple job portals

notes:
  - Intended for learning and automation practice
  - Job availability depends on platform updates and search limits
  - Virtual environment should be activated before running the script
