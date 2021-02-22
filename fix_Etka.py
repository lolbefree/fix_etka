import os
import shutil
import getpass

win_user = getpass.getuser()
class etka_fix:
    def __init__(self):
        self.marks = ["au", "se", "sk", "vw"]

        self.repldata = "COUNTRY_PRS=UKR\n"        # страна
        self.data = []
        import psutil
        # killing process
        for proc in psutil.process_iter():
            if any(procstr in proc.name() for procstr in ['MFC', 'etka', 'lexcom']):
                print(f'Killing {proc.name()}')
                proc.kill()
        # killing process end

        for item in self.marks:
            try:
                shutil.move(f'c:\\ProgramData\\LexCom\\ETKA\\DATA\\{item}\\Data1\\preissvv.log',f'c:\\ProgramData\\LexCom\\ETKA\\DATA\\{item}\\Data1\\preissvv_back.log')
            except:
                print("no file")
            try:

                shutil.move(f'c:\\ProgramData\\LexCom\\ETKA\\DATA\\{item}\\Data2\\preissvv.log',f'c:\\ProgramData\\LexCom\\ETKA\\DATA\\{item}\\Data2\\preissvv_back.log')
            except:
                print("no file")

    def fixing_job(self):
        for item in self.marks:
            with open(f'C:\\Users\\{win_user}\AppData\Local\lexcom\etka\config\Etka_User_{item}.ini', 'r') as ini_file:
                for row in ini_file:
                    if not "COUNTRY_PRS=" in row:
                        self.data.append(row)
                    if "COUNTRY_PRS=" in row:
                        self.data.append(self.repldata)
                print(self.data)
                with open(f'C:\\Users\\{win_user}\AppData\Local\lexcom\etka\config\Etka_User_{item}.ini', 'w') as new_ini_file:
                    for line in self.data:
                        new_ini_file.write(line)
                    self.data.clear()


app = etka_fix().fixing_job()