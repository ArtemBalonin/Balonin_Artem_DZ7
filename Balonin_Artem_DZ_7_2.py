import os

setting = {}
with open("date/config.yaml") as f:
    lines = dict(map(str.split, f.readlines()))

basedir = lines.pop("base")
for k, v in lines.items():
    os.makedirs(os.path.join(os.curdir, basedir, k), exist_ok=True)
    print(f"Создан каталог: {k}")
    for i in v.split(","):
        with open(os.path.join(os.curdir, basedir, k, i), "w") as f:
            print(f"Создан файл: {i} в каталоге {k} ")