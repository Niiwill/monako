#!/usr/bin/env python3
"""Fetch the last 28 days of Search Console data and save it to seo/reports/.

Reads credentials from the GSC_SERVICE_ACCOUNT_JSON environment variable
(the full service-account JSON as a string, e.g. from a GitHub Actions
secret). Run weekly by .github/workflows/gsc-weekly-fetch.yml.
"""
import datetime
import json
import os
import sys

from google.oauth2 import service_account
from googleapiclient.discovery import build

SITE_URL = "sc-domain:apartmani-igalo.com"
SCOPES = ["https://www.googleapis.com/auth/webmasters.readonly"]
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")

PULLS = [
    {"dimensions": ["query"], "rowLimit": 1000},
    {"dimensions": ["page"], "rowLimit": 250},
    {"dimensions": ["query", "page"], "rowLimit": 1000},
]


def main():
    raw_key = os.environ.get("GSC_SERVICE_ACCOUNT_JSON")
    if not raw_key:
        print("GSC_SERVICE_ACCOUNT_JSON is not set.", file=sys.stderr)
        sys.exit(1)

    creds = service_account.Credentials.from_service_account_info(
        json.loads(raw_key), scopes=SCOPES
    )
    service = build("searchconsole", "v1", credentials=creds)

    today = datetime.date.today()
    end_date = today - datetime.timedelta(days=3)  # GSC reporting lag
    start_date = end_date - datetime.timedelta(days=27)

    report = {
        "fetched_at": today.isoformat(),
        "site_url": SITE_URL,
        "start_date": start_date.isoformat(),
        "end_date": end_date.isoformat(),
        "pulls": {},
    }

    for pull in PULLS:
        key = "+".join(pull["dimensions"])
        resp = service.searchanalytics().query(
            siteUrl=SITE_URL,
            body={
                "startDate": start_date.isoformat(),
                "endDate": end_date.isoformat(),
                "dimensions": pull["dimensions"],
                "rowLimit": pull["rowLimit"],
            },
        ).execute()
        report["pulls"][key] = resp.get("rows", [])
        print(f"Fetched {key}: {len(report['pulls'][key])} rows")

    os.makedirs(REPORTS_DIR, exist_ok=True)
    out_path = os.path.join(REPORTS_DIR, f"{today.isoformat()}.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print(f"Saved {out_path}")


if __name__ == "__main__":
    main()
