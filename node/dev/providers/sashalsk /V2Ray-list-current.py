import requests
import yaml

# Fetch the data from the URL
url = "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Ray-list-current"
response = requests.get(url)
lines = response.text.splitlines()

# Convert each line to the desired format
converted_lines = []
for line in lines:
    parts = line.split(" ")
    name = parts[0]
    server = parts[1].split(":")[0]
    port = int(parts[1].split(":")[1])
    type_ = parts[2]
    uuid = parts[3]
    alterId = int(parts[4])
    cipher = parts[5]
    tls = bool(parts[6])
    skip_cert_verify = bool(parts[7])
    network = parts[8]
    ws_path = parts[9]
    
    converted_line = {
        'name': name,
        'server': server,
        'port': port,
        'type': type_,
        'uuid': uuid,
        'alterId': alterId,
        'cipher': cipher,
        'tls': tls,
        'skip-cert-verify': skip_cert_verify,
        'network': network,
        'ws-opts': {'path': ws_path}
    }
    
    converted_lines.append(converted_line)

# Create the YAML content
yaml_content = yaml.dump({'proxies': converted_lines})

# Save the YAML content to a file
with open('V2Ray-list-current.yml', 'w') as file:
    file.write(yaml_content)
