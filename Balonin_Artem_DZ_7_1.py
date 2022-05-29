import os.path
progect_path = "my_project"
paths = ["settings", "mainapp", "adminapp", "authapp"]
for d in paths:
    os.makedirs(os.path.join(os.curdir, progect_path, d), exist_ok=True)

