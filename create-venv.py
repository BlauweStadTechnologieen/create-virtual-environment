import os
import subprocess

def run_command(cmd: str, cwd:str) -> None:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)

def create_venv() -> None:
    """
    Scans all subdirectories in a specified base directory and creates a Python virtual environment (.venv)
    in each subdirectory that does not already have one. Handles errors for missing base directory and
    command failures, and prints status messages for each subdirectory.
    """
    try:
    
        BASE_DIR = "C:\\Users\\toddg\\OneDrive\\test"

        if not BASE_DIR:
            raise KeyError("Base Directory not specified")
        
        if not os.path.exists(BASE_DIR):
            raise FileNotFoundError(f"A base directory {BASE_DIR} is specified, but does not exist.")
         
        for package in os.listdir(BASE_DIR):

            cwd = os.path.join(BASE_DIR, package) 

            if not os.path.isdir(cwd):
                raise FileNotFoundError(f"{cwd} is not a, existing directory")
                
            venv_path = os.path.join(cwd, ".venv")

            if not os.path.exists(venv_path):
                
                create_venv = run_command(["python","-m", "venv", ".venv"], cwd)

                if create_venv.returncode != 0:
                    
                    raise Exception(create_venv.returncode, create_venv.stderr)
                                
                print(f"Virtual environment successfully installed in {package.title()}")

            else:
                
                print(f"{package.title()} already has a Virtual Environment installed.")

        return
    
    except KeyError as e:
        
        custom_message =f"Key Error in Constant {e}"
        
        print(custom_message)

    except FileNotFoundError as e:

        custom_message = f"{e}"

        print(custom_message)

    except Exception as e:
        
        custom_message =f"Exception Error {e}"
        
        print(custom_message)

if __name__ == "__main__":
    create_venv()