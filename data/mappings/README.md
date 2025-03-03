# Mapping Files

## Purpose

This directory contains mapping configuration files that define how data should be transformed between different OpenCTI dashboard templates. These mapping files serve as translation layers that enable the dashboard replication tool to convert dashboards from one template format to another.

## Mapping File Structure

The mapping files are stored in CSV format and follow this naming convention:
```
mapping_csv_[target]_from_[source]_template.csv
```

Where:
- `[target]` - The target dashboard type (e.g., sectors, strategic_sectors)
- `[source]` - The source template name (e.g., energy, finance)

### CSV Structure

Each mapping file contains columns that define how elements from the source template should be mapped to elements in the target dashboard. Typical columns include:

- **Source Field**: The field name in the source template
- **Target Field**: The corresponding field name in the target
- **Transformation**: Optional transformation rules to apply during conversion
- **Data Type**: The expected data type for the field
- **Required**: Whether the field is required (true/false)

## Relationship to Templates

The mapping files work directly with the templates found in the `data/input/templates` directory. For example:

- `mapping_csv_sectors_from_energy_template.csv` defines how to transform data from the `sector_energy_template.json` to a sectors dashboard
- `mapping_csv_strategic_sectors_from_finance_template.csv` defines how to transform data from the `strategic_finance_template.json` to a strategic sectors dashboard

## Usage

The mapping files are used by the dashboard replication tool to:

1. Read the source dashboard data
2. Apply the transformations defined in the mapping file
3. Generate a new dashboard according to the target format

## Example

A simple mapping file might look like:

```csv
source_field,target_field,transformation,data_type,required
title,name,,string,true
description,description,,string,false
energy_value,sector_value,multiply_by_100,number,true
timeframe,period,,string,true
```

This would instruct the replication tool on how to map fields from the source to the target, including any necessary transformations.

## Adding New Mappings

To create a new mapping between templates:

1. Identify the source and target template formats
2. Create a new CSV file following the naming convention
3. Define the field mappings and transformations
4. Place the file in this directory

