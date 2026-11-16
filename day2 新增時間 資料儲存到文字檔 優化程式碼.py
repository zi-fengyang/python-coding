#新增時間 資料儲存到文字檔 優化程式碼
from datetime import datetime
def check_machine(machine,now_time):
  if machine["is_running"] and machine["temp"] > 80 :
    return f"{now_time}【過熱警報】機台編號{machine['id']}溫度異常，目前溫度{machine['temp']}度！\n"
  return
machines_data= [
  {"id" : "EQP-01","temp" : 65,"is_running" : True},
  {"id" : "EQP-02","temp" : 92,"is_running" : True},
  {"id" : "EQP-03","temp" : 88,"is_running" : False},
  {"id" : "EQP-04","temp" : 78,"is_running" : True},
  {"id" : "EQP-05","temp" : 84,"is_running" : True}
  ]
now_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
alert = []
for i in machines_data:
    msg = check_machine(i,now_time)
if msg:
    alert.append(msg)
if alert:
    with open("machine_alarms.txt" , "a" , encoding = "utf-8" )as file:
        file.writelines(alert)
print(f"巡檢完成，共新增{len(alert)}筆異常紀錄至 machine_alarms.txt")
