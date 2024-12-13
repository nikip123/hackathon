import yaml

def parse_openapi(api_spec_file):
    try:
        api_spec = yaml.safe_load(api_spec_file.read())
        return api_spec
    except Exception as e:
        raise ValueError(f"Failed to parse OpenAPI spec: {e}")
