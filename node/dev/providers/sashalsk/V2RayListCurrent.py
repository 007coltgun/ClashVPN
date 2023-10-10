import requests
import yaml
import json

def export_vmess_to_clash(vmess_url, output_file):
    """Exports VMESS proxies from a given URL to Clash proxy format.

    Args:
        vmess_url: The URL of the VMESS proxy list.
        output_file: The path to the output file.
    """

    response = requests.get(vmess_url)
    vmess_text = response.content.decode("utf-8")

    # Try to decode the text using a different encoding if necessary.
    try:
        vmess_text = vmess_text.decode("latin-1")
    except UnicodeDecodeError:
        pass

    # Remove any invalid characters from the text.
    vmess_text = "".join([c for c in vmess_text if c.isprintable()])

    vmess_proxies = json.loads(vmess_text)

    clash_proxies = []
    for vmess_proxy in vmess_proxies:
        clash_proxy = {
            "name": vmess_proxy["name"],
            "type": "vmess",
            "server": vmess_proxy["add"],
            "port": vmess_proxy["port"],
            "uuid": vmess_proxy["id"],
            "cipher": vmess_proxy["type"],
            "tls": vmess_proxy["tls"],
        }

        if vmess_proxy["tls"]:
            clash_proxy["tls-config"] = {
                "serverName": vmess_proxy["host"],
            }

        clash_proxies.append(clash_proxy)

    with open(output_file, "w") as f:
        f.write("proxies:\n")
        yaml.dump(clash_proxies, f, sort_keys=False)

if __name__ == "__main__":
    vmess_url = "https://raw.githubusercontent.com/sashalsk/V2Ray/main/V2Ray-list-current"
    output_file = "./node/sashalsk/V2RayListCurrent.yml"

    export_vmess_to_clash(vmess_url, output_file)
