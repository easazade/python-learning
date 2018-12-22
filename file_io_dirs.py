import os
import doc_scripts

folder_name = "python"
items = os.listdir("c:/")
if folder_name not in items:
    os.mkdir(f"c:/{folder_name}")

print(doc_scripts.__doc__)

