# import os
# import json
# import csv
# import shutil
# import hashlib
# from datetime import datetime

# DATA_DIR = 'data'
# CLEANED_DIR = 'cleaned'
# BACKUP_DIR = 'backup'
# JSON_FILE = 'employees.json'
# HASHES_FILE = 'hashes.json'
# LOG_FILE = 'logs.txt'


# def ensure_dirs():
#     os.makedirs(CLEANED_DIR, exist_ok=True)
#     os.makedirs(BACKUP_DIR, exist_ok=True)


# def log(msg):
#     with open(LOG_FILE, 'a') as f:
#         f.write(f"{datetime.now()} - {msg}\n")


# def get_hash(data) -> str:
#     return hashlib.md5(json.dumps(data, sort_keys=True).encode()).hexdigest()


# def email_valid(email):
#     return '@' in email and '.' in email


# def salary_valid(salary):
#     try:
#         float(salary.replace('$', '').replace(',', ''))
#         return True
#     except ValueError:
#         return False


# def load_existing_hashes():
#     if os.path.exists(HASHES_FILE):
#         with open(HASHES_FILE, 'r') as f:
#             return json.load(f)
#     return {}


# def save_hashes(hashes):
#     with open(HASHES_FILE, 'w') as f:
#         json.dump(hashes, f, indent=2)


# def backup_file(file_path, label):
#     timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#     filename = f"{label}_{timestamp}{os.path.splitext(file_path)[1]}"
#     shutil.copy(file_path, os.path.join(BACKUP_DIR, filename))


# def process_department(file, old_hashes, new_hashes, departments):
#     dept = os.path.splitext(file)[0]
#     filepath = os.path.join(DATA_DIR, file)
#     cleaned_employees = []
#     seen = set()

#     with open(filepath, 'r') as f:
#         for line in f:
#             parts = line.strip().split(',')
#             if len(parts) != 4:
#                 log(f"Invalid format in {file}: {line.strip()}")
#                 continue
#             emp_id, name, email, salary = parts
#             if not email_valid(email):
#                 log(f"Invalid email: {email}")
#                 continue
#             if not salary_valid(salary):
#                 log(f"Invalid salary: {salary}")
#                 continue
#             key = (emp_id, email)
#             if key in seen:
#                 log(f"Duplicate found in {file}: {emp_id}, {email}")
#                 continue
#             seen.add(key)
#             cleaned_employees.append([emp_id, name, email, salary])

#     hash_now = get_hash(cleaned_employees)
#     new_hashes[dept] = hash_now

#     if old_hashes.get(dept) != hash_now:
#         # Save cleaned CSV for this department
#         with open(os.path.join(CLEANED_DIR, f"{dept}.csv"), 'w') as csvfile:
#             writer = csv.writer(csvfile)
#             writer.writerow(["id", "name", "email", "salary"])
#             writer.writerows(cleaned_employees)
#         log(f"{dept}.csv updated")
#         departments[dept] = [
#             {"id": eid, "name": name, "email": email, "salary": salary}
#             for eid, name, email, salary in cleaned_employees
#         ]
#         return True  # Data changed
#     else:
#         return False  # No change


# def build_json(departments):
#     with open(JSON_FILE, 'w') as f:
#         json.dump({"departments": departments}, f, indent=2)
#     log("employees.json written")
#     backup_file(JSON_FILE, "employees")


def main():
    ensure_dirs()
    old_hashes = load_existing_hashes()
    new_hashes = {}
    departments = {}
    data_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.txt')]

    any_changes = False
    for file in data_files:
        changed = process_department(file, old_hashes, new_hashes, departments)
        if changed:
            any_changes = True

        if any_changes:
        # Load old JSON to merge unchanged departments
          if os.path.exists(JSON_FILE):
            with open(JSON_FILE, 'r') as f:
                old_json = json.load(f)
            old_depts = old_json.get("departments", {})
            for dept in old_depts:
                if dept not in departments:
                    departments[dept] = old_depts[dept]  # merge unchanged departments
        build_json(departments)

        save_hashes(new_hashes)
        for dept in departments:
            backup_file(os.path.join(CLEANED_DIR, f"{dept}.csv"), dept)
        log("Backup complete")
    else:
        log("No changes detected, skipping file write/backup")


# if __name__ == "__main__":
#     main()








# for by me =====================




import os
import json
import csv
import shutil
import hashlib
from datetime import datetime

DATA_DIR = 'data'
CLEANED_DIR = 'cleaned'
BACKUP_DIR = 'backup'
JSON_FILE = 'employees.json'
HASHES_FILE = 'hashes.json'
LOG_FILE = 'logs.txt'


def ensure_dirs():
    os.makedirs(CLEANED_DIR,exist_ok=True)
    os.makedirs(BACKUP_DIR,exist_ok=True)

def log(msg):
    with open(LOG_FILE, 'a') as f:
        f.write(f"{datetime.now()} - {msg}\n")


def email_valid(email):
    return '@' in email and '.' in email


def salary_valid(salary):
    try:
        float(salary.replace('$', '').replace(',', ''))
        return True
    except ValueError:
        return False
    
def backup_file(file_path, label):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{label}_{timestamp}.{file_path.split('.')[1]}"
    shutil.copy(file_path, os.path.join(BACKUP_DIR, filename))

def get_hashes(dept):
      return hashlib.md5(json.dumps(dept, sort_keys=True).encode()).hexdigest()


def create_hashFile(hash):
    with open(HASHES_FILE,'w') as f:
        json.dump(hash,HASHES_FILE,indent=2)




def load_all_hashes():
    if  os.path.exists(HASHES_FILE):   
        try:
            with open(HASHES_FILE,'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        

    
def emplyess_json(dept):
    with open(JSON_FILE,'w') as f:
        json.dump(f,JSON_FILE,indent=2)
    
    
        


is_dup = set()
def process_department(file,old_hashes,new_hashes,departments):
    dept =file.split('.')[0]
    filename = os.path.join(DATA_DIR,file)
    all_employees= []
    
    with open(filename,'r') as f:
         for line in f:
             parts = line.strip().split(',')
             emp_id,name,email,salary = parts

             if not email_valid(email):
                 log(f'the invalid email in {dept} which email is {email}')
                 continue 
             if not salary_valid(salary):
                 log(f'the invalid salary in {dept} which salary is {salary}')
                 continue
             check_dup = (email,emp_id)
             if check_dup in is_dup:
                 log(f'duplicate data in  {dept} which  is {check_dup}')
                 continue
             is_dup.add(check_dup)
             clean_Data = [emp_id,name,email,salary]
             all_employees.append(clean_Data)
    
    old_hashes =load_all_hashes()
    hashes = get_hashes(all_employees)
    new_hashes[dept]=hashes
    if old_hashes.get(dept) !=new_hashes:
        path= os.path.join(CLEANED_DIR,filename)
        with open(path,'w') as f:
            writer = csv.writer(f)
            writer.writerow({"id","name","email","salary"})
            return True
    else:
        return False


             

process_department('hr.txt')