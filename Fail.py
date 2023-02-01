import json
def get_all():
    fail1 = []
    with open("fail.json", "r", encoding="utf-8") as json_file:
        a = json.load(json_file)
    for name in a:
        fail1.append(name["name"])
    return fail1
def get_score():
    fail2 = []
    with open("fail.json", "r", encoding="utf-8") as json_file:
        a = json.load(json_file)
    for best_result in a:
        fail2.append(best_result["best_result"])
    return fail2
def get_password():
    fail3 = []
    with open("fail.json", "r", encoding="utf-8") as json_file:
        a = json.load(json_file)
    for password in a:
        fail3.append(password["password"])
    return fail3