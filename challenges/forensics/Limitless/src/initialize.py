from tqdm import tqdm
import os
import random
import zipfile
import pathlib
import json


def __salt(salt_chars, salt_data):
    salt_length = int(salt_data.split(".")[-1])
    return "".join([random.choice(salt_chars) for _ in range(salt_length)])

def __parse_challdata():
    with open("__challdata/__challdata.json", "r") as data:
        _challdata = json.load(data)
    
    salt_chars = _challdata["flags"]["salt_chars"]
    salt_data = _challdata["flags"]["flag_salt"]
    chall_dir = _challdata["challenge_directory"]
    chall_size = int(_challdata["challenge_size"])
    flag = _challdata["flags"]["flag_format"].replace("*", _challdata["flags"]["valid_flag"])
    herr_flag = _challdata["flags"]["flag_format"].replace("*", _challdata["flags"]["invalid_flags"])
    return {
        "salt_chars": salt_chars,
        "salt_data": salt_data,
        "chall_dir": chall_dir,
        "chall_size": chall_size,
        "flag": flag,
        "herr_flag": herr_flag
    }

def __update_challdata(flag, flag_file, flag_salt):
    with open("__challdata/__challdata.json", "r") as f:
        data = json.load(f)
    
    data["postcreate_data"] = {
        "valid_flag": flag,
        "flag_salt": flag_salt,
        "flag_file": flag_file,
        "dist_zip": f"_chall_{flag_file}_{flag_salt}"
    }
    with open("__challdata/__challdata.json", "w") as f:
        f.write(json.dumps(data, indent=4))


def __zip_chall_folder(file_path):
    zipf = zipfile.ZipFile(f"../dist/challenge.zip", "w", zipfile.ZIP_DEFLATED)
    for root, _, files in os.walk(file_path):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), file_path))
    zipf.close()

def __generate_chall_file(_challdata: dict):
    file_path = _challdata["chall_dir"]
    flag_file = random.randint(1, int(_challdata["chall_size"]) + 1)
    flag_salt = __salt(_challdata["salt_chars"], _challdata["salt_data"])
    flag = _challdata["flag"].replace("*", flag_salt)

    try:
        os.mkdir(file_path)
    except FileExistsError as f:
        pass
    except Exception as e:
        raise e
    
    for i in tqdm(range(1, _challdata["chall_size"] + 1)):
        y = ""
        for _ in range(random.randint(1000, 2500)):
            y += random.choice("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        
        s = random.randint(len(y) // 2, len(y))
        if i == flag_file:
            x = y[:s] + flag + y[s+len(flag):]
            print(f"flag written to file {i}: {flag}")
        else:
            z = _challdata["herr_flag"].replace("*", __salt(_challdata["salt_chars"], _challdata["salt_data"]))
            x = y[:s] + z + y[s+len(z):]
        with open(f"{file_path}/flag_{i}.txt", "w") as f:
            f.write(x)

    __zip_chall_folder(file_path)
    return flag, flag_file, flag_salt

if __name__ == "__main__":
    _challdata = __parse_challdata()
    flag, flag_file, flag_salt = __generate_chall_file(_challdata)
    __update_challdata(flag, flag_file, flag_salt)
    os.rmdir(_challdata["chall_dir"])