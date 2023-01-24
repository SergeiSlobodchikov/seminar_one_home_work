
path = 'Tel.txt'

def readFile():
    result = []
    with open(path, 'r+', encoding='utf8') as data:
        for line in data:
            result.append(line.replace('\n', '').split(','))
    return result

def add_new_contact(new_contact: list):
        data_to_save = ",".join(new_contact)+"\n"
        print(data_to_save)
        with open(path, 'a', encoding='utf8') as datafile:
            datafile.write(data_to_save)

def search_contact(find: str):
    result = []
    with open(path, 'r+', encoding='utf8') as phone_book:
        for contact in phone_book:
            for field in contact:
                if find in field:
                    result.append(contact)
                    break
    
    return result