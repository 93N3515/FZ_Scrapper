import os
import zipfile
import datetime

time = datetime.datetime.now().strftime("%d.%m.%y %H-%M-%S")
path = input("Путь к логам")
res_path = "FileZilla_result "+time
os.mkdir(res_path)
i=0
f=0
print("Работа")
for file in os.listdir(path):
    if zipfile.is_zipfile(path+"\\"+file):
        f+=1
        print(f)
        zip = zipfile.ZipFile(path+"\\"+file)
        for zip_file in zipfile.ZipFile.infolist(zip):
            if zip_file.filename.find("FileZilla") and zip_file.filename.find(".xml") >=1:
                i+=1
                lines = zip.open(zip_file)
                new_file = open(res_path+f"\\FileZilla#recentservers ({i}).xml","w+")
                new_file.write(lines.read().decode())
                new_file.close()
        os.system("CLS")
print("\nВсего найдено: "+str(i))