import osquery
import re
import json


def process_by_username():
    instance = osquery.SpawnInstance()
    instance.open()
    a = str(instance.client.query("SELECT pid, username, name FROM processes p JOIN users u ON u.uid = p.uid ORDER BY start_time"))
    aSplited = a.rsplit("response=")
    #print(aSplited[0][:-2]) #This is the statusContext
    data = aSplited[1][:-1] #This is the conetent 
    data = data.replace("'", '"')
    return data

def process_by_cpu_from_bootup():
    instance = osquery.SpawnInstance()
    instance.open()
    a = str(instance.client.query("SELECT pid, uid, name, ROUND((\
                                  (user_time + system_time) / (cpu_time.tsb - cpu_time.itsb)\
                                  ) * 100, 2) AS percentage\
                                  FROM processes, (\
                                  SELECT (\
                                  SUM(user) + SUM(nice) + SUM(system) + SUM(idle) * 1.0) AS tsb,\
                                  SUM(COALESCE(idle, 0)) + SUM(COALESCE(iowait, 0)) AS itsb\
                                  FROM cpu_time\
                                  ) AS cpu_time\
                                  ORDER BY user_time+system_time DESC;"))
    aSplited = a.rsplit("response=")
    #print(aSplited[0][:-2]) #This is the statusContext
    data = aSplited[1][:-1] #This is the conetent 
    data = data.replace("'", '"')
    print(data)
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




