import yaml

with open("../data/data01.yaml", "r", encoding="utf-8")as f:
    print(yaml.load(f))