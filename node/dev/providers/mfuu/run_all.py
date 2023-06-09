import urllib.request
import re

url = "https://raw.githubusercontent.com/mfuu/v2ray/master/clash.yaml"

def export_content(output_file, pattern):
    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
    filtered_content = re.findall(pattern, content, flags=re.MULTILINE)
    filtered_content = [line for line in filtered_content if "UUID" in line]  # Add a filter to include only lines that contain UUID
    with open(output_file, "w") as f:
        f.write("proxies:\n")  # Add proxies: at the beginning of the file
        for line in filtered_content:
            f.write(line + "\n")
    print(f"{pattern} exported.")

export_content("./node/mfuu/ae.yml", r'^.*🇦🇪.*')
export_content("./node/mfuu/am.yml", r'^.*🇦🇲.*')
export_content("./node/mfuu/au.yml", r'^.*🇦🇺.*')
export_content("./node/mfuu/ba.yml", r'^.*🇧🇦.*')
export_content("./node/mfuu/bg.yml", r'^.*🇧🇬.*')
export_content("./node/mfuu/br.yml", r'^.*🇧🇷.*')
export_content("./node/mfuu/ca.yml", r'^.*🇨🇦.*')
export_content("./node/mfuu/ch.yml", r'^.*🇨🇭.*')
export_content("./node/mfuu/cl.yml", r'^.*🇨🇱.*')
export_content("./node/mfuu/cn.yml", r'^.*🇨🇳.*')
export_content("./node/mfuu/cy.yml", r'^.*🇨🇾.*')
export_content("./node/mfuu/cz.yml", r'^.*🇨🇿.*')
export_content("./node/mfuu/de.yml", r'^.*🇩🇪.*')
export_content("./node/mfuu/ee.yml", r'^.*🇪🇪.*')
export_content("./node/mfuu/fi.yml", r'^.*🇫🇮.*')
export_content("./node/mfuu/fr.yml", r'^.*🇫🇷.*')
export_content("./node/mfuu/gb.yml", r'^.*🇬🇧.*')
export_content("./node/mfuu/nowhere.yml", r'^.*🇦🇶.*')
export_content("./node/mfuu/hk.yml", r'^.*🇭🇰.*')
export_content("./node/mfuu/id.yml", r'^.*🇮🇩.*')
export_content("./node/mfuu/ie.yml", r'^.*🇮🇪.*')
export_content("./node/mfuu/in.yml", r'^.*🇮🇳.*')
export_content("./node/mfuu/ir.yml", r'^.*🇮🇷.*')
export_content("./node/mfuu/it.yml", r'^.*🇮🇹.*')
export_content("./node/mfuu/jp.yml", r'^.*🇯🇵.*')
export_content("./node/mfuu/kr.yml", r'^.*🇰🇷.*')
export_content("./node/mfuu/lt.yml", r'^.*🇱🇹.*')
export_content("./node/mfuu/lv.yml", r'^.*🇱🇻.*')
export_content("./node/mfuu/mo.yml", r'^.*🇲🇴.*')
export_content("./node/mfuu/mx.yml", r'^.*🇲🇽.*')
export_content("./node/mfuu/nl.yml", r'^.*🇳🇱.*')
export_content("./node/mfuu/no.yml", r'^.*🇳🇴.*')
export_content("./node/mfuu/pl.yml", r'^.*🇵🇱.*')
export_content("./node/mfuu/relay.yml", r'^.*🏁.*')
export_content("./node/mfuu/ru.yml", r'^.*🇷🇺.*')
export_content("./node/mfuu/sa.yml", r'^.*🇸🇦.*')
export_content("./node/mfuu/se.yml", r'^.*🇸🇪.*')
export_content("./node/mfuu/sg.yml", r'^.*🇸🇬.*')
export_content("./node/mfuu/tr.yml", r'^.*🇹🇷.*')
export_content("./node/mfuu/tw.yml", r'^.*🇹🇼.*')
export_content("./node/mfuu/ua.yml", r'^.*🇺🇦.*')
export_content("./node/mfuu/us.yml", r'^.*🇺🇸.*')
export_content("./node/mfuu/vn.yml", r'^.*🇻🇳.*')
