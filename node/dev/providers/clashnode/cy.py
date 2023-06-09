import urllib.request
import re

url = "https://raw.githubusercontent.com/mlabalabala/v2ray-node/main/clashnode4clash.txt"
output_file = "./node/clashnode/cy.yml"

def export_us_content():
    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
    filtered_content = re.findall(r'^.*name: 🇨🇾.*', content, flags=re.MULTILINE)
    with open(output_file, "w") as f:
        f.write("proxies:\n")  # Add proxies: at the beginning of the file
        for line in filtered_content:
            f.write(line + "\n")
    print("🇨🇾CY exported.")

export_us_content()
