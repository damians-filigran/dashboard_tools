#!/usr/bin/env python3
import argparse
import base64
import csv
import json
import os
import sys

def main():
    parser = argparse.ArgumentParser(
        description=("""** OpenCTI Dashboard entity find/replace tool**.     This tool enables the user to take an exported OpenCTI custom dashboard
                     that focuses on one subject, such as a specific sector, country, or creator, and make multiple copies for each of a
                     range of alternative sectors, countries, etc. It decodes an OpenCTI dashboard JSON file, and replaces all occurrances
                     of the UUID of the entity with the UUID of a replacement.
                     It will also replace all occurrences of the entity's name (eg. sector, country) in widgets and the title, with a new name.
                     The CSV file should have three fields of: UUID, Name string, Output filename, and the first row should contain the current value to
                     """)
    )
    parser.add_argument("json_file", help="Path to the JSON configuration file.")
    parser.add_argument("csv_file", help="Path to the CSV file with mapping.")
    args = parser.parse_args()


    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)


    # Load JSON configuration
    with open(args.json_file, "r") as jf:
        data = json.load(jf)

    try:
        encoded_manifest = data["configuration"]["manifest"]
    except KeyError:
        print("Error: 'manifest' key not found under 'configuration' in JSON.")
        return

    # Decode the Base64 manifest
    try:
        decoded_manifest = base64.b64decode(encoded_manifest).decode("utf-8")
    except Exception as e:
        print(f"Error decoding manifest: {e}")
        return

    # Read CSV mapping file
    with open(args.csv_file, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    if len(rows) < 2:
        print("CSV must contain at least two rows: one for search criteria and at least one for a replacement.")
        return

    # First CSV row: original UUID and original name (search criteria), order: UUID, Field name
    orig_uuid = rows[0][0].strip()
    orig_name = rows[0][1].strip()
    print(f"Original values to replace: UUID='{orig_uuid}', name='{orig_name}'")

    # Process each subsequent CSV row; each row must have three columns: new UUID, new name, and output filename.
    for row in rows[1:]:
        if len(row) < 3:
            print("Skipping invalid row (expected at least three fields):", row)
            continue

        new_uuid = row[0].strip()
        new_name = row[1].strip()
        output_file = row[2].strip()
        if not output_file.lower().endswith(".json"):
            output_file += ".json"

        # Replace the original UUID with the new UUID in the decoded manifest
        updated_manifest = decoded_manifest.replace(orig_uuid, new_uuid)
        # Replace occurrences of the original name with the new name in the decoded manifest
        updated_manifest = updated_manifest.replace(orig_name, new_name)

        # Base64 re-encode the updated manifest
        updated_encoded_manifest = base64.b64encode(updated_manifest.encode("utf-8")).decode("utf-8")

        # Create an updated JSON configuration by copying the original and updating the manifest
        updated_data = data.copy()
        updated_data["configuration"] = updated_data["configuration"].copy()

        # A final replacement of the Name string in the title, if it's present
        updated_data["configuration"]["name"] = updated_data["configuration"]["name"].replace(orig_name,new_name)

        updated_data["configuration"]["manifest"] = updated_encoded_manifest

        # Write the updated JSON to the specified output file
        with open(output_file, "w") as outf:
            json.dump(updated_data, outf, indent=4)
        print(f"Created file: {output_file}")

if __name__ == "__main__":
    main()