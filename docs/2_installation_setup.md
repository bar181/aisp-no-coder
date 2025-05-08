# Installation and Setup

This guide will walk you through setting up and running the AISP PoC Creator.

## Prerequisites

- Python 3.8+
- Access to a Supabase instance
- An OpenAI API key

## Setup Steps

1.  **Prepare Environment and Install Dependencies**

    Navigate to the project root directory in your terminal.

    ```bash
    # Copy the example environment file
    cp .env.example .env

    # Create and activate a Python virtual environment
    python -m venv .venv
    source .venv/bin/activate

    # Install the required Python packages
    pip install -r requirements.txt
    ```

2.  **Configure Environment Variables**

    Edit the newly created `.env` file and replace the placeholder values with your actual Supabase URL, Supabase Service Key, and OpenAI API Key.

    ```dotenv
    # ===== Supabase =====
    SUPABASE_URL=https://your-project.supabase.co
    SUPABASE_SERVICE_KEY=your-service-key

    # ===== OpenAI =====
    OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    OPENAI_MODEL=gpt-4o-mini
    ```

3.  **Generate Component Specs**

    Run the generator script with a YAML idea sheet. This will create JSON specification files in the `generated_specs` directory and upload them to your Supabase instance.

    ```bash
    python generator/gen.py examples/vehicle.yml
    ```

4.  **Seed Sample Data (Optional)**

    If you want to populate your database with some initial data, run the seed script.

    ```bash
    python scripts/seed.py
    ```

5.  **Run the API**

    Start the FastAPI development server. The dynamic router will read the generated specs from Supabase and expose the corresponding CRUD endpoints.

    ```bash
    uvicorn app.main:app --reload
    ```

## Accessing the API

Once the server is running, you can access:

-   **Swagger UI**: `http://localhost:8000/docs` to explore the generated API endpoints.
-   **Health Probe**: `http://localhost:8000/healthz` to check the application status.