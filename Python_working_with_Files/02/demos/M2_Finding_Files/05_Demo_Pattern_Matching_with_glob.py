from pathlib import Path

#only search of matching files in a dir rather that all files
def glob_match(fld, search):
    p = Path(fld)
    for n in p.glob(search):
        print(n)

#glob_match('./files', '*2*.t*')
glob_match('./files/subfolder', '*1_t*file_*c*.t*')