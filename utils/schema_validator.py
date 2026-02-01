import json
from jsonschema import validate, ValidationError


def validate_schema(schema_path, data):
    try:
        with open(schema_path) as f:
            schema = json.load(f)

        validate(instance=data, schema=schema)
        return True, "Validation successful"

    except ValidationError as e:
        return False, f"Schema validation error: {e.message}"

    except FileNotFoundError:
        return False, "Schema file not found"

    except Exception as e:
        return False, f"Unexpected error: {str(e)}"
