import osquery
import re
import json
from json2html import *


def send_and_receive_all():
    instance = osquery.SpawnInstance()
    instance.open()
    a = str(instance.client.query("SELECT pid, username, name FROM processes p JOIN users u ON u.uid = p.uid ORDER BY start_time"))
    aSplited = a.rsplit("response=")
    #print(aSplited[0][:-2]) #This is the statusContext
    data = aSplited[1][:-1] #This is the conetent 
    data = data.replace("'", '"')
    return data


def assign_status_dict(status): #ExtensionResponse(status=ExtensionStatus(code=0, message='OK', uuid=0),
    m = re.search('ExtensionStatus(.*)', status)
    if m:
        found = m.group(1)
    status_code= found[1:-1]
    status_code_list = status_code.split(",")
    print(status_code_list)

    #converting to dictionary
    #Need to work on this later but for now i pause this it here

if __name__ == "__main__":
    instance = osquery.SpawnInstance()
    instance.open()
    a = str(instance.client.query("SELECT pid, username, name FROM processes p JOIN users u ON u.uid = p.uid ORDER BY start_time"))
    aSplited = a.rsplit("response=")
    #print(aSplited[0][:-2]) #This is the statusContext
    print(aSplited[1][:-1]) #This is the conetent 
    data = aSplited[1][:-1]
    data = data.replace("'", '"')
    with open("test.txt", "w") as f:
        f.write(data)

    with open("test.html", "w") as f:
        f.write(json2html.convert(json = data))


