# Sprint 1 Technical Details

This document outlines the technical implementation details of Sprint 1, focusing on the core components that enable the generation of CRUD endpoints from a YAML idea sheet.

## Directory Structure

The key directories and files for Sprint 1 are:

```
aisp-poc/
├── examples/
│   └── vehicle.yml         # Sample idea sheet
├── generator/
│   └── gen.py              # Script to generate specs
├── templates/
│   └── api-crud-entity/
│       └── template_spec.json # Jinja2 template for CRUD spec
├── schema/
│   └── aisp_component.schema.json # JSON schema for validation
├── app/
│   ├── db.py               # Supabase client
│   ├── agent.py            # Generic agent stub
│   ├── dynamic_router.py   # FastAPI router that loads specs
│   └── main.py             # FastAPI app entry point
├── scripts/
│   └── seed.py             # Script to seed sample data
└── tests/
    └── test_health.py      # Health check test
```

## Component Details

### Idea Sheet (`examples/vehicle.yml`)

A simple YAML file defining the project name, entities, and features. The `features` list drives the spec generation.

```yaml
name: FleetTrack
entities:
  - Vehicle
  - Driver
features:
  - CRUD Vehicle
  - CRUD Driver
```

### Spec Generator (`generator/gen.py`)

This Python script reads the YAML idea sheet, processes features (currently only "CRUD"), and generates JSON specification files based on the `api-crud-entity` template. It validates the generated spec against the schema and uploads it to Supabase.

Key functions:
- `load_idea()`: Reads and parses the YAML file.
- `render()`: Uses Jinja2 to render the JSON spec from the template and context.
- `main()`: Orchestrates the process, iterates through features, generates specs, validates, and uploads to Supabase.

### CRUD Template (`templates/api-crud-entity/template_spec.json`)

A Jinja2 template defining the structure of a CRUD component specification in JSON format. It includes placeholders for `component_id` and `entity`. The `aisp` field contains a simplified AISP block.

```json
{
  "id": "{{ component_id }}",
  "json_spec": {
    "Template_Version": "0.1",
    "Functionality_ID": "{{ component_id }}",
    "Functionality_Name": "CRUD {{ entity }}",
    "Version": "0.1.0",
    "Status": "ready",
    "Short_Description": "Auto-generated CRUD endpoints for {{ entity }}.",
    "Input_Data": {
      "props": [
        { "name": "id", "type": "int", "required": false, "description": "Primary key" },
        { "name": "name", "type": "str", "required": true, "description": "{{ entity }} name" }
      ]
    }
  },
  "aisp": "Ω.entity:{{ entity }} api {id:{{ component_id }}}\nΨ.param.id int optional\nΨ.param.name str required\nΓ.requirement[1]:create read update delete\nΛ.test:health_check\n"
}
```

### Spec Schema (`schema/aisp_component.schema.json`)

A JSON schema defining the required structure and data types for the generated component specifications. This ensures consistency and validity of the specs.

### App Components (`app/`)

-   `db.py`: Provides a cached Supabase client instance.
-   `agent.py`: A minimal stub for a generic agent that currently just echoes the input payload. This is a placeholder for future logic.
-   `dynamic_router.py`: A FastAPI router that queries Supabase for "ready" components, dynamically creates Pydantic models based on the spec's `Input_Data`, and registers POST endpoints (`/{component_id}`) that invoke the `GenericAgent`.
-   `main.py`: The main FastAPI application instance. It includes a health check endpoint and includes the `dynamic_router`.

### Seed Script (`scripts/seed.py`)

A utility script to insert sample data into a Supabase table (e.g., "vehicle") for testing purposes.

### Tests (`tests/test_health.py`)

Contains a basic test using `starlette.testclient` to verify the health check endpoint is functioning correctly.