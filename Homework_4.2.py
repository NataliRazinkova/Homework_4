def get_cats_info(path):
    cats_info = []
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_dict = {
                        'id': cat_data[0],
                        'name': cat_data[1],
                        'age': int(cat_data[2])
                    }
                    cats_info.append(cat_dict)
                else:
                    print(f"Illegal format in line: {line}")
    
    except FileNotFoundError:
        print(f"The file '{path}' does not exist.")
    
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    
    return cats_info


cats_data = get_cats_info(r"D:\\cats.txt")

for cat in cats_data:
    print(cat)