# Project Overview

This project, AISP PoC Creator, is a proof-of-concept demonstrating a zero-boilerplate approach to generating CRUD API endpoints. It takes a simple YAML idea sheet as input, generates component specifications, and uses FastAPI to dynamically expose CRUD endpoints based on these specifications at runtime.

## Key Features

- YAML-based idea sheet input
- Automatic generation of component specifications
- Dynamic API routing based on generated specs
- CRUD endpoint generation
- Integration with Supabase for data persistence (via generated specs)

## Architecture

The system consists of:
- A `generator` script that processes YAML idea sheets and creates JSON specifications.
- A `schema` for validating the generated specifications.
- `templates` used by the generator to structure the specifications.
- An `app` directory containing the FastAPI application, including a dynamic router that reads the generated specs and creates API routes.
- A `scripts` directory for utility scripts like seeding data.
- `tests` for basic health checks.

## Workflow

1. Define entities and features in a YAML file (idea sheet).
2. Run the `generator` script with the YAML file to produce JSON specifications in the `generated_specs` directory and upload them to Supabase.
3. (Optional) Run the `seed` script to populate the database with sample data.
4. Run the FastAPI application. The dynamic router reads the specs from Supabase and creates the corresponding CRUD endpoints.
5. Access the API endpoints via the generated Swagger UI (`/docs`).