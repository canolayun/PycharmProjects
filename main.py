import os

import xml.etree.ElementTree as ET
# global wafer_id
import glob

#find wafer ID path

wafer_id = str(input("Wafer ID:"))
wafer_path = "C:/Users/유채윤/finalproject/HY202103/"+wafer_id+"/20190715_190855"
file_list = os.listdir(wafer_path)

#get the structure
wafer_coordinate=str(input('coordinate:'))
wafer_name_path= wafer_path + '/HY202103_'+ wafer_id + '_' + wafer_coordinate + '_LION1_DCM_LMZC.xml'

print(wafer_name_path)
tree = ET.parse(wafer_name_path)
root = tree.getroot()

#IV-measurement
# values = []
#
# for child in root.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement'):
#     values.append(child.text)
#
# # load the iv measurement
# voltage_string = values[0].split(',')
# voltage = []
# for i in voltage_string:
#     voltage.append(float(i))
#
# current_string = values[1].split(',')
# current = []
# for i in current_string:
#     current.append(float(i))
#
# # pandas
# element = root.find('.//TestSiteInfo')
# lot = element.attrib['Batch']
# wafer = element.attrib['Wafer']
# mask = element.attrib['Maskset']
# testSite = element.attrib['TestSite']
# row = element.attrib['DieRow']
# column = element.attrib['DieColumn']
# element1 = root.find('.//Modulator')
# name = element1.attrib['Name']
#
# operator = root.attrib['Operator']
# date = root.attrib['CreationDate']
# des_par = root.findall('.//DesignParameter')[1].text


# get input a certain wafer
# wafer_id = input('wafer_id :')

file_path = glob.glob('C:/Users/유채윤/finalproject/HY202103/**/*.xml',recursive=True)
print(file_path)

wafer_id2 = str(input('Wafer ID:'))

# print(len(file_path))
#
# wafer_list = ['D07','D08','D23','D24']
# while True:
#     wafer_id = input('wafer_id : ')
#     if wafer_id in wafer_list:
#         print(wafer_id)
#         break
#     else:
#         if wafer_id == '':
#             for wafer_id in wafer_list:
#                 print(wafer_id)
#             break
#         else:
#             print("This is not a file")

# # get the data structure
# tree = ET.parse(wafer_id)
# root = tree.getroot()
# values = []
#
# for child in root.find(''):
#     values.append(child.text)
#
# # load the iv measurement
# voltage_string = values[0].split(',')
# voltage = []
# for i in voltage_string:
#     voltage.append(float(i))
#
# current_string = values[1].split(',')
# current = []
# for i in current_string:
#     current.append(float(i))
#
# # get the data structure
# import xml.etree.ElementTree as ET
# tree = ET.parse(wafer_id)
# root = tree.getroot()
# values = []
# for child in root.find('./ElectroOpticalMeasurements/ModulatorSite/Modulator/PortCombo/IVMeasurement'):
#     values.append(child.text)
#
# # load the iv measurement
# voltage_string = values[0].split(',')
# voltage = []
# for i in voltage_string:
#     voltage.append(float(i))
#
# current_string = values[1].split(',')
# current = []
# for i in current_string:
#     current.append(float(i))
#
#
#
# # def create_folder(directory):
# #     try:
# #         if not os.path.exists(directory):
# #             os.makedirs(directory)
# #     except OSError:
# #         print('Error: Creating directory. ' + directory)

