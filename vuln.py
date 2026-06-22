import subprocess

# SECURE: Using subprocess prevents argument injection
safe_folder = input("Enter the folder name to list: ")
# Pass arguments as a list to avoid shell interpretation
subprocess.run(["ls", "-la", safe_folder])
