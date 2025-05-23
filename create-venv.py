import os
import subprocess
import env_vars

def run_command(cmd: str, cwd:str) -> None:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True)

def install_dependancies(venv_path: str, cwd: str) -> None:
    """
    Installs Python dependencies from a requirements.txt file into the specified virtual environment.
    Dot notation: create_venv.install_dependancies(venv_path, cwd)
    Args: 
        venv_path (str): Path to the virtual environment directory.
        cwd (str): Current working directory where requirements.txt is expected.
    Raises:
        FileNotFoundError: If the requirements.txt file is not found in the specified directory.
        Exception: If pip install command fails.
    Returns:
        None
    """
    
    venv_python = os.path.join(venv_path, "Scripts", "python.exe")
    
    requirements_file = os.path.join(cwd, "requirements.txt")

    try:
    
        if os.path.exists(requirements_file):
            
            print(f"Installing requirements from {requirements_file}...")
            
            install_reqs = run_command([venv_python, "-m", "pip", "install", "-r", requirements_file], cwd)

            if install_reqs.returncode != 0:

                raise Exception(install_reqs.returncode, install_reqs.stderr)
            
            else:

                print(f"Requirements installed successfully")

                return
        
        else:
            
            raise FileNotFoundError(f"Requirements file {requirements_file} not found in {cwd}")

    except FileNotFoundError as e:
        
        custom_message = f"{e.__class__.__name__} {e}"

        print(custom_message)

    except Exception as e:
        
        custom_message = f"{e.__class__.__name__} {e}"

        print(custom_message)

def create_env(cwd: str) -> None:
    """
    Creates a '.env' file in the specified current working directory (cwd).
    This file is typically used to store environment variables, not related to the Python virtual environment itself.
    Args:
        cwd (str): The current working directory where the '.env' file should be created.
    Returns:
        None
    Notes:
        - If the '.env' file already exists, the function returns without making changes.
        - If an exception occurs during file creation, it prints a custom error message.
    """
    env_file = os.path.join(cwd, ".env")

    if os.path.exists(env_file):
        
        print(f".env file already exists in {cwd}")
        
        return

    try:
        
        with open(env_file, "w") as f:
                        
            f.write("# Environment variables\n")

            print(f"Creating keys & values in {env_file}...")
            
            for key, value in env_vars.env_vars.items():
                
                f.write(f"{key}={value}\n")

        print(f".env file created in {cwd}")

    except Exception as e:

        custom_message = f"{e.__class__.__name__} {e}"

        print(custom_message)


def create_venv() -> None:
    """
    Scans all subdirectories in a specified base directory and creates a Python virtual environment (.venv)
    in each subdirectory that does not already have one. If a virtual environment already exists, it installs
    dependencies from requirements.txt if present. Handles errors for missing base directory, missing subdirectories,
    and command failures, and prints status messages for each subdirectory.
    """
    try:
    
        BASE_DIR = "E:\\packages"

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

            create_env(cwd)
            
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
