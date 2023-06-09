import urllib.request
import re

url = "https://raw.githubusercontent.com/a2470982985/getNode/main/clash.yaml"

def export_content(output_file, pattern):
    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
    filtered_content = re.findall(pattern, content, flags=re.MULTILINE)
    with open(output_file, "w") as f:
        f.write("proxies:\n")  # Add proxies: at the beginning of the file
        for line in filtered_content:
            f.write(line + "\n")
    print(f"{pattern} exported.")

export_content("./node/getnode/ae.yml", r'^.*🇦🇪.*')
export_content("./node/getnode/am.yml", r'^.*🇦🇲.*')
export_content("./node/getnode/au.yml", r'^.*🇦🇺.*')
export_content("./node/getnode/ba.yml", r'^.*🇧🇦.*')
export_content("./node/getnode/bg.yml", r'^.*🇧🇬.*')
export_content("./node/getnode/br.yml", r'^.*🇧🇷.*')
export_content("./node/getnode/ca.yml", r'^.*🇨🇦.*')
export_content("./node/getnode/ch.yml", r'^.*🇨🇭.*')
export_content("./node/getnode/cl.yml", r'^.*🇨🇱.*')
export_content("./node/getnode/cn.yml", r'^.*🇨🇳.*')
export_content("./node/getnode/cy.yml", r'^.*🇨🇾.*')
export_content("./node/getnode/cz.yml", r'^.*🇨🇿.*')
export_content("./node/getnode/de.yml", r'^.*🇩🇪.*')
export_content("./node/getnode/ee.yml", r'^.*🇪🇪.*')
export_content("./node/getnode/fi.yml", r'^.*🇫🇮.*')
export_content("./node/getnode/fr.yml", r'^.*🇫🇷.*')
export_content("./node/getnode/gb.yml", r'^.*🇬🇧.*')
export_content("./node/getnode/nowhere.yml", r'^.*🇦🇶.*')
export_content("./node/getnode/hk.yml", r'^.*🇭🇰.*')
export_content("./node/getnode/id.yml", r'^.*🇮🇩.*')
export_content("./node/getnode/ie.yml", r'^.*🇮🇪.*')
export_content("./node/getnode/in.yml", r'^.*🇮🇳.*')
export_content("./node/getnode/ir.yml", r'^.*🇮🇷.*')
export_content("./node/getnode/it.yml", r'^.*🇮🇹.*')
export_content("./node/getnode/jp.yml", r'^.*🇯🇵.*')
export_content("./node/getnode/kr.yml", r'^.*🇰🇷.*')
export_content("./node/getnode/lt.yml", r'^.*🇱🇹.*')
export_content("./node/getnode/lv.yml", r'^.*🇱🇻.*')
export_content("./node/getnode/mo.yml", r'^.*🇲🇴.*')
export_content("./node/getnode/mx.yml", r'^.*🇲🇽.*')
export_content("./node/getnode/nl.yml", r'^.*🇳🇱.*')
export_content("./node/getnode/no.yml", r'^.*🇳🇴.*')
export_content("./node/getnode/pl.yml", r'^.*🇵🇱.*')
export_content("./node/getnode/relay.yml", r'^.*🏁.*')
export_content("./node/getnode/ru.yml", r'^.*🇷🇺.*')
export_content("./node/getnode/sa.yml", r'^.*🇸🇦.*')
export_content("./node/getnode/se.yml", r'^.*🇸🇪.*')
export_content("./node/getnode/sg.yml", r'^.*🇸🇬.*')
export_content("./node/getnode/tr.yml", r'^.*🇹🇷.*')
export_content("./node/getnode/tw.yml", r'^.*🇹🇼.*')
export_content("./node/getnode/ua.yml", r'^.*🇺🇦.*')
export_content("./node/getnode/us.yml", r'^.*🇺🇸.*')
export_content("./node/getnode/vn.yml", r'^.*🇻🇳.*')
