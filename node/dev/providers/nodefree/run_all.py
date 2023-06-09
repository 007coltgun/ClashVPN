import urllib.request
import re

url = "https://raw.githubusercontent.com/mlabalabala/v2ray-node/main/nodefree4clash.txt"

def export_content(output_file, pattern):
    with urllib.request.urlopen(url) as f:
        content = f.read().decode('utf-8')
    filtered_content = re.findall(pattern, content, flags=re.MULTILINE)
    with open(output_file, "w") as f:
        f.write("proxies:\n")  # Add proxies: at the beginning of the file
        for line in filtered_content:
            f.write(line + "\n")
    print(f"{pattern} exported.")

export_content("./node/nodefree/cn.yml", r'^.*_CN_.*')
export_content("./node/nodefree/sg.yml", r'^.*_SG_.*')
export_content("./node/nodefree/kr.yml", r'^.*_KR_.*')
export_content("./node/nodefree/us.yml", r'^.*_US_.*')
export_content("./node/nodefree/hk.yml", r'^.*_HK_.*')
export_content("./node/nodefree/jp.yml", r'^.*_JP_.*')
export_content("./node/nodefree/nl.yml", r'^.*_NL_.*')
export_content("./node/nodefree/tw.yml", r'^.*_TW_.*')
export_content("./node/nodefree/nl.yml", r'^.*_NL_.*')
export_content("./node/nodefree/fr.yml", r'^.*_FR_.*')
export_content("./node/nodefree/in.yml", r'^.*_IN_.*')
export_content("./node/nodefree/de.yml", r'^.*_DE_.*')
export_content("./node/nodefree/ru.yml", r'^.*_RU_.*')
