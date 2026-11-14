#工廠機台健康度統計系統

def check_machine(machine):
    if machine["is_running"] == True and machine["temp"] > 80 :
        print(f"【緊急警報】運轉中機台 機台編號{machine["id"]}過熱（溫度{machine["temp"]}度）！")
        return True
    else:
        print(f"【安全】機台 機台編號{machine["id"]}狀態正常")
        return False

machines_data = [
    {"id" : "EQP-01","temp" : 65,"is_running" : True},
    {"id" : "EQP-02","temp" : 92,"is_running" : True},
    {"id" : "EQP-03","temp" : 88,"is_running" : False},
    {"id" : "EQP-04","temp" : 78,"is_running" : True},
    {"id" : "EQP-05","temp" : 84,"is_running" : True}
    ]
alert_count = 0
for i in machines_data:
    if check_machine(i) == True:
        alert_count += 1
print(f"巡檢結束，總共有異常數量{alert_count}台運轉中機台發生過熱警報！")