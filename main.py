import os
import shutil

user_dir_path = str(input("Enter path of directory to be sorted: "))
user_log_name = str(input("Enter name for output log: "))
create_output_log = user_log_name.strip() + ".txt"
current_working_directory = os.getcwd()
dir_list = os.listdir(user_dir_path)
error = None

img_list = []
video_list = []
audio_list = []
doc_list = []
exe_list = []
zip_list = []
web_list = []
folder_list = []
misc_list = []

sorted_folder_names = ("Images", "Video", "Audio", "Docs", "Programs", \
                       "Packages", "Web_Pages", "Folders", "MISC")

for x in dir_list:
    try:
        if x.endswith(('.jpg', '.jpeg', '.bmp', '.webp', '.png', '.svg')):
            img_list.append(x)
        elif x.endswith(('.mov', '.mp4', '.avi', '.wmv', '.avchd')):
            video_list.append(x)
        elif x.endswith(('.wav', '.aiff', '.mp3', '.m4a', '.flac')):
            audio_list.append(x)
        elif x.endswith(('.pdf', '.doc', '.docx', '.rtf', '.txt', '.xls', \
                         '.xlsx', '.xml', '.csv')):
            doc_list.append(x)
        elif x.endswith(('.exe', '.msi', '.app', '.run', '.sh', '.cmd')):
            exe_list.append(x)
        elif x.endswith(('.zip', '.dmg', '.pkg', '.tar')):
            zip_list.append(x)
        elif x.endswith(('.html', '.htm')):
            web_list.append(x)
        elif os.path.isdir(user_dir_path + "/" + x):
            folder_list.append(x)
        else:
            misc_list.append(x)
    
    except Exception as e:
        error = e
        print("Error in loop: {}".format(error))

if (error == None):
    try:
        with open(create_output_log, 'w') as f:
            f.write("IMAGES: {}".format(img_list) \
                    + "\n" + "VIDEO: {}".format(video_list) \
                    + "\n" + "AUDIO: {}".format(audio_list) \
                    + "\n" + "DOCS: {}".format(doc_list) \
                    + "\n" + "PROGRAMS: {}".format(exe_list) \
                    + "\n" + "PACKAGES: {}".format(zip_list) \
                    + "\n" + "WEB PAGES: {}".format(web_list) \
                    + "\n" + "FOLDERS: {}".format(folder_list) \
                    + "\n" + "MISC: {}".format(misc_list)
                    )
        
        for y in sorted_folder_names:
            os.mkdir(user_dir_path + '/' + y)

        all_sorted_lists = [img_list, video_list, audio_list, doc_list, \
                            exe_list, zip_list, web_list, folder_list, misc_list]
        
        i = 0
        while i < len(all_sorted_lists):
            for j in all_sorted_lists:
                for k in j:
                    shutil.move(user_dir_path + '/' + k, \
                                user_dir_path + '/' + sorted_folder_names[i])
                i += 1

        shutil.move(current_working_directory + '/' + create_output_log, \
                    user_dir_path)

        print("Hooray! Your files are sorted!")

    except Exception as e:
        if os.path.exists(create_output_log):
            os.remove(create_output_log)
        print("Error in write: {}".format(e))
