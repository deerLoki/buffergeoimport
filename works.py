import json

# Load the JSON data from the file
with open('trump/trump.json', 'r') as f:
    data = json.load(f)

# Prepare the output OBJ file
obj_file_path = 'output.obj'

# Extract vertex positions, UVs, and face indices
vertices = data['data']['attributes']['position']['array']
uvs = data['data']['attributes'].get('uv', {}).get('array', [])
indices = data['data']['index']['array']

# Writing to the OBJ file
with open(obj_file_path, 'w') as obj_file:
    obj_file.write("# BufferGeoImport\n")
    
    # Write vertices
    for i in range(0, len(vertices), 3):
        obj_file.write(f"v {vertices[i]} {vertices[i+1]} {vertices[i+2]}\n")

    # Write UVs (if available)
    if uvs:
        for i in range(0, len(uvs), 2):
            obj_file.write(f"vt {uvs[i]} {uvs[i+1]}\n")

    # Write faces (assuming triangles)
    for i in range(0, len(indices), 3):
        # OBJ format is 1-indexed, so we add 1 to each index
        v1, v2, v3 = indices[i]+1, indices[i+1]+1, indices[i+2]+1
        obj_file.write(f"f {v1} {v2} {v3}\n")

print(f"OBJ file saved as {obj_file_path}")
