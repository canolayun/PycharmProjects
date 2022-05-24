import os


def create_folder(directory):
    try:
        if not os.path.exists(directory): #os.path.exist(directory)->directory가 존재하면 True를 반환
            os.makedirs(directory)
            #os.mkdir -> 한폴더만 생성 가능
            #os.makedirs -> 원하는 만큼 디렉토리 생성 가능
    except OSError: #
        print('Error: Creating directory. ' + directory)

#try -> 실행할 코드 except 예외가 발생했을 때 실행