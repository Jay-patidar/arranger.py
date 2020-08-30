import os, shutil
dict_extension = {
'audio_extensions':('.mp3' ,'.m4a'),
'video_extensions':('.mp4','.webm'),
'document_extensions':('.pdf','.txt','.xlsx','.docx'),
'image_extensions':('.jpg','.jpeg','.png'),
'setup_extensions':('.exe','.c'),
}

path = input('enter the path to sort:')

def file_sep(path ,tup):
    files = []
    for file in os.listdir(path):
        for i in tup:
           if file.endswith(i):
                files.append(file)
    return files

for extension_type ,tup_name in dict_extension.items():
    print('calling File seperator Function ....')
    folder_name = extension_type.split('_')[0]
    folder_path = os.path.join(path , folder_name)
    print(f'creating folder{folder_name}')
    if os.path.exists(folder_path) == True:
        print('folder already exist')
    else:
        os.mkdir(folder_path)
        print('folder created sucessfully')
    print(f'Moving the {folder_name} files ')
    for fl in file_sep(path , tup_name):
        fl_path = os.path.join(path ,fl)
        mv_path = os.path.join(path, folder_name)
        shutil.move(fl_path, mv_path)
other_file_path = os.path.join(path,'others')
if os.path.exists(other_file_path) == True:
    print('already exist')
    print('moving files')
else:
    print('making folder')
    os.mkdir(other_file_path)


for fl in os.listdir(path):
    if fl == 'setup' or fl == 'audio' or fl == 'video' or fl == 'document' or fl == 'image':
        print('moving .......')
    else:
        shutil.move(os.path.join(path,fl),other_file_path)
        





