import os
import subprocess

class DBTNavigator:
    def __init__(self,path_dbt_project):
        self.path = path_dbt_project
        self.relative_path = self.get_path()

    def get_path(self):
        current_dir = os.getcwd()
        relative_path = os.path.relpath(self.path, start=current_dir)
        script_bash = f"cd {relative_path} ;"
        return script_bash

    def execute(self,model_path):
        complete_path = self.relative_path + 'dbt run --select ' + f'{model_path}'
        try:
            out = subprocess.run(["powershell", "-Command", f"{complete_path}"],check=False,capture_output=True, text=True)
            print(out.stdout)
        except RuntimeError:
            print('Nao foi possivel')