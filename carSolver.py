import models as m
import csv

# input: {名前、直進OR右折OR左折、Arrival、緑時間}のリスト
params = [
  {"name": "NE", "mode": "left", "arrival": 97.2, "gt": 55},
  {"name": "NS", "mode": "straight", "arrival": 477, "gt": 48},
  {"name": "NW", "mode": "right", "arrival": 191.2, "gt": 55},
  {"name": "EN", "mode": "right", "arrival": 69.2, "gt": 53},
  {"name": "ES", "mode": "left", "arrival": 169.2, "gt": 53},
  {"name": "EW", "mode": "straight", "arrival": 393.2, "gt": 46},
  {"name": "SE", "mode": "right", "arrival": 122, "gt": 55},
  {"name": "SN", "mode": "straight", "arrival": 515.6, "gt": 48},
  {"name": "SW", "mode": "left", "arrival": 161.6, "gt": 55},
  {"name": "WE", "mode": "straight", "arrival": 394, "gt": 46},
  {"name": "WN", "mode": "left", "arrival": 137.2, "gt": 53},
  {"name": "WS", "mode": "right", "arrival": 159.2, "gt": 53},
]

# inputリストlのgt書き換え
def changeGT():
  csv_file = open("./data.csv", "r", encoding="ms932", errors="", newline="")
  f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
  for row in f:
    for i in range(len(params)):
      params[i]["gt"] = int(row[i])

# DataFrame用の配列処理
def listCarTraffic():
  val = []
  for road in params:
    x = m.carTraffic(road["name"], road["mode"], road["arrival"], road["gt"])
    val.append(x.makeParamsIntoList())
  return val

# test用
if __name__ == "__main__":
  csv_file = open("./data.csv", "r", encoding="ms932", errors="", newline="")
  f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
  for row in f:
    for i in range(len(params)):
      params[i]["gt"] = int(row[i])
    data = listCarTraffic()
    print(data)