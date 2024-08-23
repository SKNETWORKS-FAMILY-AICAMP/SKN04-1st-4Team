import subprocess

def run_script(script_name):
    try:
        process = subprocess.Popen(['python3', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()  # 스크립트가 종료될 때까지 대기
        stdout, stderr = process.communicate()

        if process.returncode == 0:
            print(f"Successfully ran {script_name}:\n{stdout}")
        else:
            print(f"Error running {script_name}:\n{stderr}")
            raise subprocess.CalledProcessError(process.returncode, script_name)
    
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        raise
    
if __name__ == "__main__":
    scripts = ['car2013to2022.py', 'car2024.py', 'en_coe.py', 'kia.py', 'merge_two_file.py', 'crawl_data_to_db.py',]
    
    for script in scripts:
        print(script)
        run_script(script)
