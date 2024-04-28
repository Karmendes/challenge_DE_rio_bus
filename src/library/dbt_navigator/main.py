import os
import subprocess
from library.logger.main import Logger

class DBTNavigator:
    def __init__(self,path_dbt_project,env = 'PROD'):
        self.path = path_dbt_project
        self.relative_path = self.get_path()
        self.enviroment = env

    def get_path(self):
        current_dir = os.getcwd()
        relative_path = os.path.relpath(self.path, start=current_dir)
        script_bash = f"cd {relative_path} ;"
        return script_bash

    def execute(self, model_path):
        complete_path = self.relative_path + 'dbt run --select ' + f'{model_path}'
        # Use a logger for consistent error handling and logging
        if self.enviroment == 'DEV':
            try:
                out = subprocess.run(
                    ["powershell", "-Command", complete_path],
                    check=True,  # Raise an exception on non-zero return code
                    capture_output=True,
                    text=True,
                    encoding="utf-8",  # Explicitly set encoding for proper output display
                )
                print(out.stdout)
            except subprocess.CalledProcessError as e:
                Logger.emit(f"dbt execution failed: {e.output}",'ERROR')
                return e.returncode

        else:  # Production environment
            try:
                out = subprocess.Popen(complete_path, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = out.communicate(timeout=60)  # Set a timeout for dbt execution
                print(stdout.decode("utf-8"))  # Decode output for proper display

                if out.returncode != 0:
                    Logger.emit(f"dbt execution failed (stderr): {stderr.decode('utf-8')}",'ERROR')
                    return out.returncode

            except (subprocess.TimeoutExpired, subprocess.CalledProcessError) as e:
                Logger.emit(f"dbt execution failed: {e}",'ERROR')
                return 1  # Return generic error code for production environment

        return 0  # Return success code