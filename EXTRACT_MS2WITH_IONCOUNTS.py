import os

extrac_path = r"E:\pFindStudio\ThermoRawRead-ctarn-with-extra"
os.chdir(extrac_path)
file_folder = r"M:\20200801\DSS"

for root, dirs, fls in os.walk(file_folder):
    for fl in fls:
        if fl.endswith(".raw"):
            raw_path = os.path.join(root, fl)
            output_path = root
            cmd = "ThermoRawRead.exe -D " + raw_path + "  -O " + output_path + " -c" 
            print(cmd)
            os.system(cmd)