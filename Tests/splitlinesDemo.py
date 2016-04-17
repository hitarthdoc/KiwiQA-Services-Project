lines = """aesdrfgh
drxtfygvhbjni
gvbhn
hbjn
njm
"""

err_lines = lines.splitlines()

err = ""
for i in err_lines:
     if "dr" in i:
         err += i
print err
