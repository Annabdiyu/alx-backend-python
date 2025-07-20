def access_nested_map(nested_map, path):
    """Access a nested object in `nested_map` with `path`."""
    for key in path:
        nested_map = nested_map[key]
    return nested_map
