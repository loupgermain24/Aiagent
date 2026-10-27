import os
for root, dirs, files in os.walk("."):
    if any(x in root for x in [".git", "__pycache__", "node_modules"]):
        continue
    print(root)
    for f in files:
        p = os.path.join(root, f)
        print(" ", p, os.path.getsize(p))
