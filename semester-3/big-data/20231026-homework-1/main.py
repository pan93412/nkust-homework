#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import json
import mimetypes
import re

import requests

urls = [
    "https://www.nkust.edu.tw/",
    "https://ic.nkust.edu.tw/",
]

invalid_characters = re.compile(r"[^a-zA-Z0-9_]")
unexpected_underscore = re.compile(r"_+")

csv_target = open("homework1.csv", "w")
csv_writer = csv.DictWriter(
    csv_target, fieldnames=["URL", "MIME Type", "Filename", "Raw Response Filename", "Content"]
)
csv_writer.writeheader()

session = requests.Session()

for url in urls:
    filename = re.sub(r"_+", "_", invalid_characters.sub("_", url)).strip("_")

    resp = session.get(
        url,
        headers={
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
        },
    )
    resp.raise_for_status()

    content_type = resp.headers["Content-Type"] + ";"
    mime = resp.headers["Content-Type"][0 : content_type.find(";")]
    extension = mimetypes.guess_extension(mime)

    # content (.html typically)
    blob_filename = f"{filename}.{extension}"
    with open(blob_filename, "wb") as fp:
        fp.write(resp.content)

    # json
    json_filename = f"{filename}.json"
    with open(json_filename, "w", encoding="utf-8") as fp:
        json.dump(
            {
                "method": resp.request.method,
                "headers": dict(resp.headers),
                "status_code": resp.status_code,
                "encoding": resp.encoding,
                "request_url": resp.request.url,
                "final_url": resp.url,
                "content": resp.text
            },
            fp,
            ensure_ascii=False,
            indent=4,
        )

    # csv
    csv_writer.writerow(
        {
            "URL": url,
            "MIME Type": mime,
            "Filename": filename,
            "Raw Response Filename": json_filename,
            "Content": resp.text
        }
    )

csv_target.close()
