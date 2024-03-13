import os

# os 는 python 표준 라이브러리로 운영체제와 상호작용하는
# 다양한 기능을 제공함 (파일시스템 탐색 및 삭제, 변경 ...)

dir = os.getcwd() #현재 파일 위치
print(dir)
file_list = os.listdir(dir) # 현재 위치에 있는 파일이나 폴더들

for f in file_list:
    print(f)
    file_path = os.path.join(dir, f) #경로 결합
    if os.path.isfile(file_path):    #파일이면 True 리턴
        print("파일임:",file_path)
    elif os.path.isdir(file_path):
        print("폴더임:",file_path)
# 파일 삭제 os.remove(), 빈폴더 삭제 os.rmdir()

# os.remove('C:\dev\pythonProject\pythonProject\python_base\delay.txt')
# os.rmdir('C:\dev\pythonProject\pythonProject\python_base\\test') #관리자 권한으로 실행해야 함
#
# import shutil
# shutil.rmtree('C:\dev\pythonProject\pythonProject\python_base\\test')

root = 'C:\\'
for dirpath, dirname, filename in os.walk(root):
    print(dirpath, dirname, filename)