import json
import os
import hashlib

blockchain_dir = os.curdir + '/blockchain/'

def get_hash(filename):
    file = open(blockchain_dir + filename, 'rb').read()#read binary
    return hashlib.md5(file).hexdigest()

def get_files():
    files =os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])


def check_integrity():
    files = get_files()

    results = []

    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['prev_hash']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'ok'
        else:
            res = 'Corrupted'

        results.append({'block':prev_file, 'result':res})

    return results

def write_block(name, amount, to_who, prev_hash=''):
    files = get_files()
    prev_file = files[-1]
    NewFile = str(prev_file + 1)

    prev_hash = get_hash(str(prev_file))

    data = {'name':name,
            'amount':amount,
            'to_who':to_who,
            'prev_hash':prev_hash
    }

    with open(blockchain_dir + NewFile, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def main():
    check_integrity()
    #write_block(name='Anton', amount=200, to_who='Vasy')

if __name__ == '__main__':
    main()
