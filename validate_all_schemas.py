import os
import json
from jsonschema import Draft202012Validator

SCHEMA_DIR = "schemas"

def validate_schema_file(path):
    with open(path, "r") as f:
        schema = json.load(f)
    Draft202012Validator.check_schema(schema)

def main():
    print("Starting full schema validation...\n")

    for filename in os.listdir(SCHEMA_DIR):
        if filename.endswith(".schema.json"):
            full_path = os.path.join(SCHEMA_DIR, filename)
            try:
                validate_schema_file(full_path)
                print(f"✔ {filename} — VALID")
            except Exception as e:
                print(f"✖ {filename} — INVALID")
                print(f"  Error: {e}\n")

    print("\nSchema validation pass complete.")

if __name__ == "__main__":
    main()
