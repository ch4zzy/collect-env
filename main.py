variable_names = []

with open("config/settings.py", "r") as f:
    content = f.read()

for line in content.split("\n"):
    if 'env(' in line:
        env_start = line.find('env(')
        if env_start != -1:
            env_end = line.find(')', env_start)
            if env_end != -1:
                variable_name = line[env_start + 4:env_end].strip('"\' ')
                if variable_name.isupper():
                    variable_names.append(variable_name)

    elif ' = env.bool(' in line:
        parts = line.split('=')
        if len(parts) > 1:
            variable_name = parts[0].strip()
            if variable_name.isupper():
                variable_names.append(variable_name)

with open("config/.env", "w") as env_f:
    for var in variable_names:
        env_f.write(f"{var}=\n")
