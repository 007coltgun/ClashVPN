import urllib.request
import re

url = "https://raw.githubusercontent.com/mahdibland/V2RayAggregator/master/sub/sub_merge_yaml.yml"

def export_content(output_file, pattern):
    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
    filtered_content = re.findall(pattern, content, flags=re.MULTILINE)
    with open(output_file, "w") as f:
        f.write("proxies:\n")  # Add proxies: at the beginning of the file
        for line in filtered_content:
            f.write(line + "\n")
    print(f"{pattern} exported.")

export_content("./node/ae.yml", r'^.*🇦🇪.*')
export_content("./node/am.yml", r'^.*🇦🇲.*')
export_content("./node/au.yml", r'^.*🇦🇺.*')
export_content("./node/ba.yml", r'^.*🇧🇦.*')
export_content("./node/bg.yml", r'^.*🇧🇬.*')
export_content("./node/br.yml", r'^.*🇧🇷.*')
export_content("./node/ca.yml", r'^.*🇨🇦.*')
export_content("./node/ch.yml", r'^.*🇨🇭.*')
export_content("./node/cl.yml", r'^.*🇨🇱.*')
export_content("./node/cn.yml", r'^.*🇨🇳.*')
export_content("./node/cy.yml", r'^.*🇨🇾.*')
export_content("./node/cz.yml", r'^.*🇨🇿.*')
export_content("./node/de.yml", r'^.*🇩🇪.*')
export_content("./node/ee.yml", r'^.*🇪🇪.*')
export_content("./node/fi.yml", r'^.*🇫🇮.*')
export_content("./node/fr.yml", r'^.*🇫🇷.*')
export_content("./node/gb.yml", r'^.*🇬🇧.*')
export_content("./node/nowhere.yml", r'^.*🇦🇶.*')
export_content("./node/hk.yml", r'^.*🇭🇰.*')
export_content("./node/id.yml", r'^.*🇮🇩.*')
export_content("./node/ie.yml", r'^.*🇮🇪.*')
export_content("./node/in.yml", r'^.*🇮🇳.*')
export_content("./node/ir.yml", r'^.*🇮🇷.*')
export_content("./node/it.yml", r'^.*🇮🇹.*')
export_content("./node/jp.yml", r'^.*🇯🇵.*')
export_content("./node/kr.yml", r'^.*🇰🇷.*')
export_content("./node/lt.yml", r'^.*🇱🇹.*')
export_content("./node/lv.yml", r'^.*🇱🇻.*')
export_content("./node/mo.yml", r'^.*🇲🇴.*')
export_content("./node/mx.yml", r'^.*🇲🇽.*')
export_content("./node/nl.yml", r'^.*🇳🇱.*')
export_content("./node/no.yml", r'^.*🇳🇴.*')
export_content("./node/pl.yml", r'^.*🇵🇱.*')
export_content("./node/relay.yml", r'^.*🏁.*')
export_content("./node/ru.yml", r'^.*🇷🇺.*')
export_content("./node/sa.yml", r'^.*🇸🇦.*')
export_content("./node/se.yml", r'^.*🇸🇪.*')
export_content("./node/sg.yml", r'^.*🇸🇬.*')
export_content("./node/tr.yml", r'^.*🇹🇷.*')
export_content("./node/tw.yml", r'^.*🇹🇼.*')
export_content("./node/ua.yml", r'^.*🇺🇦.*')
export_content("./node/us.yml", r'^.*🇺🇸.*')
export_content("./node/vn.yml", r'^.*🇻🇳.*')
