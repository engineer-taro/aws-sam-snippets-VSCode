import glob
import json

result = {}

file_paths = glob.glob('./snippets/parts/**/*.json', recursive=True)
print("Target files: ", file_paths)
for file_path in file_paths:
    with open(file_path) as f:
        d = json.load(f)
        result.update(d)

output_file = 'snippets/yaml-snippets.json'
with open(output_file, 'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('Output:', output_file)