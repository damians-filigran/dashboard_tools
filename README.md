# OpenCTI Dashboard Replicator

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A script for making multiple copies of a dashboard template repurposed for each of a number of different sectors, countries or other entities.

# Introduction

OpenCTI users may sometimes find the need to make multiple versions of a dashboard with a single parameter changed in multiple widgets. For example:
- Take a Strategic Threat Intelligence Landscape dashboard created for the Energy sector, and make a similar copy for the Finance, Health, Government and Logistics sectors
- Take a dashboard containing a wide range of widgets tracking the technical content and status of a specific connector, and replicate it for every other connector in the platform.
- Take a dashboard created to track a specific threat actor, and create several copies to track several other threat actors, using the same tools.

Without this script, a user would make a duplicate of the dashboard in question, and then manually edit each widget in turn, searching for the entity to add, and then removing the original entity. This can take several minutes per dashboard if there are many widgets to edit, and there could be several or more dashboards that are required. This is tedious work.


## What this script does

This script takes an exported dashboard JSON file, and then makes multiple copies, replacing the entity the dashboard focuses on with one of a number of alternatives. Hence, a user can start with a template based on the energy sector, and replicate it multiple times for each of the Finance, Entertainment, Telecommunications, Government, and other sector, with a single script execution.


## How this script works

This script takes two arguments
- An OpenCTI dashboard JSON file, acting as a template
- A CSV file containing the original template entity name and type, and then a new entity name and type on each following row

For each line on the CSV file, it:
- Decodes the Dashboard file to make it editable
- Performs a search/replace for the original UUID of the main entity of focus
- Replaces that UUID with the new UUID from the CSV file (eg. UUID for Energy sector, with UUID for Finance sector)
- Replaces any mention of the entity name in the dashboard titles, with the new entity's name (eg. "Energy" for "Finance")
- Re-encodes the JSON file
- Saves the file to disk using the filename specified in the CSV
- Loops to the next line in the CSV

## Understanding the Dashboard JSON

Dashboards can be easily [exported to JSON](https://docs.opencti.io/latest/usage/dashboards/?h=dash#export) in a single click, and [imported](https://docs.opencti.io/latest/usage/dashboards/?h=dash#import) just as easily. 

The Dashboard structure is marginally little harder to edit, as the full manifest is BASE64 encoded. This can be decoded in a text editing tool, or, as part of this script.

However, the question is *what* to edit. Typically, a dashboard will focus on a specific entity - for example, the Energy Sector, the country USA, or the Alienvault Connector. Each such entity has a UUID, which in fact is [defined in the STIX standard](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_64yvzeku5a5c). Examples of how such an ID might be used in a STIX document in OpenCTI is [here](https://docs.opencti.io/latest/usage/nested/?h=).



# Use

## How to use this script

- First, create or find the dashboard you wish to use as a template
- Find the UUID for the focal entity (specific sector, actor, malware, connector, whatever), as in this [documentation screenshot](https://docs.opencti.io/latest/usage/overview/#presentation-of-a-typical-page-in-opencti) in the bottom right.
- Then, export it to disk
- Take one of the CSV templates, and enter your source entity's name and ID in the first row
- Add the new entity ID, name and filename in the second row
- Repeat for any additional files
- Run the script with those arguments



## How to find your entities' STIX Identifiers

To find the UUID to be search/replace'd by the script, find the entity that you're changing the dashboard from and to, and find the *STIX ID* field as in this [documentation screenshot](https://docs.opencti.io/latest/usage/overview/#presentation-of-a-typical-page-in-opencti) in the bottom right.




## Installation

### Prerequisites
- Python 3.8 or higher

### Install from source
```bash
# Clone the repository
git clone https://github.com/yourusername/dashboard-tools.git
cd dashboard-tools

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

## Usage

### Dashboard Replication

The main functionality is provided by the `dashboard_replicator` module:

```python
from dashboard_tools import dashboard_replicator


# Replicate a dashboard from a template
dashboard_tools.dashboard_replicator(
    template_file="data/input/[Sector] Energy.json",
    mapping_file="data/mappings/mapping_csv_sectors_from_energy_template.csv"
)
```


## Data Files

The repository includes example data files to help you get started:

- `data/input/`: Contains JSON templates for dashboards
  - `sector_energy_template.json`: Template for energy sector dashboard
  - `strategic_finance_template.json`: Template for finance sector dashboard

- `data/mappings/`: Contains CSV mapping files for customizing dashboards
  - `sector_from_energy_template.csv`: Mapping for creating new sector dashboards from the energy template
  - `strategic_sector_from_finance_template.csv`: Mapping for creating strategic sector dashboards from the finance template

## Contributing

Contributions are welcome! Here's how you can contribute to the project:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Run tests to ensure your changes don't break existing functionality
5. Commit your changes (`git commit -m 'Add some amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request


## License

This project is licensed under the MIT License - see the LICENSE file for details.
