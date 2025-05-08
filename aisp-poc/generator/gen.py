"""
Sprint 1 – gen.py
Generate component specs and AISP blocks from a simple idea sheet.
"""
from __future__ import annotations
import os, sys, uuid, json, pathlib, hashlib, yaml
from dotenv import load_dotenv
from supabase_py import create_client
from jinja2 import Environment, FileSystemLoader
from jsonschema import validate, ValidationError

load_dotenv()
SB = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_SERVICE_KEY"))

BASE = pathlib.Path(__file__).resolve().parent.parent
TPL_DIR = BASE / "templates"
SCHEMA = json.load(open(BASE / "schema" / "aisp_component.schema.json"))
OUT_DIR = BASE / "generated_specs"; OUT_DIR.mkdir(exist_ok=True)

env = Environment(loader=FileSystemLoader(str(TPL_DIR)), trim_blocks=True, lstrip_blocks=True)

def load_idea(path: pathlib.Path) -> dict:
    with open(path) as fp:
        return yaml.safe_load(fp)

def render(template_dir: pathlib.Path, ctx: dict) -> dict:
    tpl = env.get_template(str(template_dir / "template_spec.json"))
    return json.loads(tpl.render(**ctx))

def main(yaml_path: str):
    idea = load_idea(pathlib.Path(yaml_path))
    for feature in idea["features"]:
        if feature.startswith("CRUD"):
            entity = feature.split()[-1]
            cid = f"API-CRUD-{entity.upper()}-{uuid.uuid4().hex[:4].upper()}"
            ctx = {"entity": entity, "component_id": cid}
            spec = render(TPL_DIR / "api-crud-entity", ctx)
            try:
                validate(spec, SCHEMA)
            except ValidationError as e:
                sys.exit(f"❌ schema error: {e.message}")
            (OUT_DIR / f"{cid}.json").write_text(json.dumps(spec, indent=2))
            SB.table("components").upsert({"id": cid, "json_spec": spec, "status": "ready"}).execute()
            SB.table("aisp_raw").upsert({"component_id": cid, "aisp": spec["aisp"]}).execute()
            print(f"✓ generated {cid}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python generator/gen.py <idea.yml>")
    main(sys.argv[1])