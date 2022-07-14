import os
import fileinput
import sys
import time

project_name = input(" Enter project name: ")

print("\n==> Creating new project... \n")

os.system(f"npx create-react-app {project_name}")
os.chdir(project_name)

print("\n==> Installing tailwindcss... \n")

os.system("npm install -D tailwindcss postcss autoprefixer")
os.system("npx tailwindcss init -p")

print("\n==> Editing files... \n")

def remove_unused_styles(file, searchExp, replaceExp):
    for line in fileinput.input(file, inplace=1):
        line = line.replace(searchExp, replaceExp)
        sys.stdout.write(line)     
old_txt = 'content: [],'
new_txt = 'content: ["./src/**/*.{js,jsx,ts,tsx}",],'
File = "tailwind.config.js"
remove_unused_styles(File, old_txt, new_txt)
os.chdir("src")
f = open("index.css", 'w')
f.write("@tailwind base;\n")
f.write("@tailwind components;\n")
f.write("@tailwind utilities;\n")
f.close()
os.chdir("..")

print("\n==> Project build compelete. Opening in VScode.")
time.sleep(1)

os.system("code .")
