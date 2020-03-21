import shutil
import os
import time

path = r"C:/Users/user/Desktop/ts"

destinations = {
    'dpdf': r"C:\Users\user\Desktop\Ebook",
    'dmp3': r"C:\Users\user\Desktop\MUSIC",
    'dmkv': r"C:\Users\user\Desktop\flims",
    'djpg': r"C:\Users\user\Desktop\Widget Code",
}


def filemover():
    for folders, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename.endswith('{}'.format('.pdf')) or filename.endswith('{}'.format('.epub')):
                shutil.move(os.path.join(folders, filename), os.path.join(destinations['dpdf'], filename))
                print('Moving done!!')

            elif filename.endswith('{}'.format('.mobi')):
                shutil.move(os.path.join(folders, filename), os.path.join(destinations['dpdf'], filename))
                print('Moving done!!')

            elif filename.endswith('{}'.format('.mp3')):
                shutil.move(os.path.join(folders, filename), os.path.join(destinations['dmp3'], filename))

                print('Moving done!!')

            elif filename.endswith('{}'.format('.mp4')) or filename.endswith('{}'.format('.mkv')):
                shutil.move(os.path.join(folders, filename), os.path.join(destinations['dmkv'], filename))

                print('Moving done!!')

            elif filename.endswith('{}'.format('.jpg')):
                shutil.move(os.path.join(folders, filename), os.path.join(destinations['djpg'], filename))

                print('Moving done!!')

            else:
                print("Nothing to move")


while True:
    filemover()
    time.sleep(5)
