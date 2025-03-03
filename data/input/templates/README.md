# Templates Directory

This directory contains template JSON files used by the dashboard replication tools to create and configure OpenCTI dashboards.

## Purpose

The templates in this directory serve as standardized structures for creating different types of dashboards in OpenCTI. These templates define the layout, components, and configuration settings needed for specific dashboard types.

## Contents

This directory contains the following template files:

- `sector_energy_template.json`: Template for creating Energy sector dashboards with predefined widgets and configurations.
- `strategic_finance_template.json`: Template for creating Strategic Finance sector dashboards with specialized views and analytics components.

## Usage

These templates are used by the dashboard replication tool to:

1. Create new dashboards based on standardized layouts
2. Ensure consistent visualization across similar dashboard types
3. Provide a starting point for customization based on specific requirements

When using the dashboard replication tool, you can specify which template to use as a base for your new dashboard.

## Template Structure

Each template is a JSON file that follows the OpenCTI dashboard configuration format, containing:

- Dashboard metadata (name, description, etc.)
- Layout information
- Widget configurations
- Data source mappings

Refer to the mapping files in the `data/mappings/` directory for information on how these templates map to specific data sources.

