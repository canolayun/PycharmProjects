import glob
from glob import glob
from tqdm import tqdm
from . import path
from . import graph
from . import extract
import datetime
import os
from tqdm import tqdm
from . import wtw


now = datetime.datetime.now()               #datetime 빼고 싶음
nowDatetime = now.strftime('%Y%m%d_%H%M%S')

#define work function
def work(wafer, coordinate, save, show, csv, data_path): #wafer, coordinate, save, show, csv, data_path 를 갖는 함수
    file = []
    if data_path == '': #data path가 없다면,
        if wafer == 'All' and coordinate == 'All': #gui에서 받은 input이 모두 초기값인 경우
            file = glob(path.path() + '/data/**/*LMZ*.xml', recursive=True) #path.path -> path 모듈의 path 함수를 통해 찾은경로에서 LMZ 파일 다 불러옴
        elif coordinate == 'All':#gui에서 받은 input중 coordinate만 초기값인 경우
            file = glob(path.path() + '/data/**/{}/**/*LMZ*.xml'.format(wafer), recursive=True)#wafer이름이 들어간 xml 파일 불러오기
        else:   #gui input이 모두 초기값이 아닌 경우
            file = glob(path.path() + '/data/**/{}/**/*{}*LMZ*.xml'.format(wafer, coordinate), recursive=True)#wafer와 coordinate가 들어간 xml 파일 불러오기

    else: #data path가 있다면 -->이게 멀까
        if wafer == 'All' and coordinate == 'All':
            file = glob(data_path + '/**/*LMZ*.xml', recursive=True)
        elif coordinate == 'All':
            file = glob(data_path + '/**/{}/**/*LMZ*.xml'.format(wafer), recursive=True)
        else:
            file = glob(data_path + '/**/{}/**/*{}*LMZ*.xml'.format(wafer, coordinate), recursive=True)

    if not file:
        raise ValueError('Could not find data')

    for i in tqdm(file):
        graph.graph(i, save, show, nowDatetime)
        if csv is True: #csv 파일이 존재한다면,
            extract.data_save(i, nowDatetime) #extract 모듈의 data_save 함수로 추출
    if csv is True:
        wtw.analyze(nowDatetime)


def open():
    os.startfile(path.path() + '/result')
