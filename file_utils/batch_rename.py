import os

def batch_rename(target_dir, new_name, num_digits, source_ext, target_ext, name_range):

    files = [f for f in os.listdir(target_dir) if f.endswith(source_ext)]
    
    files.sort()
    
    for i, filename in enumerate(files, 1):

        base_name = os.path.splitext(filename)[0]        

        renamed_part = base_name[name_range[0]-1:name_range[1]]
        
        new_filename = f"{renamed_part}{new_name}{i:0{num_digits}d}.{target_ext}"
        
        old_file_path = os.path.join(target_dir, filename)
        new_file_path = os.path.join(target_dir, new_filename)
        
        os.rename(old_file_path, new_file_path)
        print(f"Renamed {filename} to {new_filename}")

