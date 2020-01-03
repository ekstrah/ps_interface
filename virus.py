from virustotal_python import Virustotal
from pprint import pprint
from json2html import *
import json


vtotal = Virustotal("50473a41f47913496c613e67dee646f6a36ebf434ce4e99fec30198f5014d29c")

resp = vtotal.file_report(
    ["09de776902ca7d32abdab8a7ccd177fb917addf502bd4bd5aa25a93ab41cc869"]
)
data = json.dumps(resp)
data = data.replace("'", '"')
html_parser = json2html.convert(json=data)
with open("./templates/program/data_tep.html", "w") as f:
    f.write(html_parser)