import requests

output_file = "./node/sashalsk/V2RayListCurrent.yml"

def convert_line(line):
  """Converts a line from the V2Ray list to a YAML format."""
  server, port, type, uuid, alter_id, cipher, tls, skip_cert_verify, network, ws_path = line.split()
  return f"  - {{'name': '{server}-{port}', 'server': '{server}', 'port': {port}, 'type': '{type}', 'uuid': '{uuid}', 'alterId': {alter_id}, 'cipher': '{cipher}', 'tls': {tls}, 'skip-cert-verify': {skip_cert_verify}, 'network': '{network}', 'ws-opts': {{'path': '{ws_path}'}}}}\n"

def main():
  """Converts the V2Ray list to a YAML file."""
  response = requests.get("https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Ray-list-current")
  lines = response.content.decode().splitlines()

  converted_lines = [convert_line(line) for line in lines]

  with open(output_file, "w") as f:
    f.write("proxies:\n")
    f.writelines(converted_lines)

if __name__ == "__main__":
  main()
