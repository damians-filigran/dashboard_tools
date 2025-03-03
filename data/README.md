# Data Directory

This directory contains input data and mapping files used by the dashboard tools to generate and replicate OpenCTI dashboards.

## Directory Structure

```
data/
├── input/            # JSON template files for different sectors
│   ├── [Sector] Energy.json
│   └── [Strategic Sector] Finance.json
├── mappings/         # CSV mapping files for translating template data
│   ├── mapping_csv_sectors_from_energy_template.csv
│   └── mapping_csv_strategic_sectors_from_finance_template.csv
└── README.md         # This file
```

## Subdirectories

### input/

This directory contains JSON template files that serve as the basis for dashboard replication. Each file represents a sector-specific dashboard template with predefined visualizations, widgets, and layouts.

- **[Sector] Energy.json**: Template for energy sector dashboards
- **[Strategic Sector] Finance.json**: Template for finance sector dashboards

### mappings/

This directory contains CSV mapping files that define how data from template files should be transformed for different use cases. These mappings enable the dashboard replicator to customize dashboards while maintaining the core structure.

- **mapping_csv_sectors_from_energy_template.csv**: Maps energy template elements to generic sector dashboards
- **mapping_csv_strategic_sectors_from_finance_template.csv**: Maps finance template elements to strategic sector dashboards

## Usage

The files in this directory are used by the dashboard replication tools to:

1. Load template dashboard configurations from the `input/` directory
2. Apply transformations defined in mapping files from the `mappings/` directory
3. Generate new dashboard configurations for different sectors or purposes

## Adding New Files

When adding new files to this directory:

- JSON template files should be placed in the `input/` directory with a clear naming convention
- Mapping files should be placed in the `mappings/` directory and follow the naming pattern `mapping_csv_[purpose]_from_[template]_template.csv`
- Avoid using special characters or spaces in filenames when possible

