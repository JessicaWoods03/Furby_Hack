import os
script_dir = os.path.dirname(__file__)
directory_path =os.path.join(script_dir, 'enwiki-20240701-pages-meta-history1.xml')
print(os.getcwd())

if os.path.exists(directory_path):
    print(f"Directory '{directory_path}' exists.")
else:
    print(f"Directory '{directory_path}' does not exists.")
