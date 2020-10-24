import os
import numpy as np
import cv2
import random
import gdal
from lxml import etree as ET

def simple_xml_dump_(infos, key_list, objects, filename, label_save_file):
    ## infos开头的信息dict, key_list关键字列表
    root=ET.Element("annotations")
    for key, val in infos.items():
        ET.SubElement(root, key).text = str(val)

    ET.SubElement(root, "filename").text = filename

    size = ET.SubElement(root,"size")
    ET.SubElement(size, "width").text = str(1024)
    ET.SubElement(size, "height").text = str(1024)
  
    for obj in objects:

        single_object=ET.SubElement(root, "object")

        #写入检测框的位置信息
        ET.SubElement(single_object,"name").text = obj['label']
        ET.SubElement(single_object,"typename").text = obj['typename']
        ET.SubElement(single_object,"classname").text = obj['classname']
        ET.SubElement(single_object,"modelname").text = obj['modelname']
        robndbox=ET.SubElement(single_object,"robndbox")
        cx, cy, w, h, theta = obj['bbox']
        ET.SubElement(robndbox,"cx").text = str(cx)
        ET.SubElement(robndbox,"cy").text = str(cy)
        ET.SubElement(robndbox,"w").text = str(w)
        ET.SubElement(robndbox,"h").text = str(h)
        ET.SubElement(robndbox,"angle").text = str(theta)
        
    tree = ET.ElementTree(root)
    tree.write(label_save_file, pretty_print=True, xml_declaration=True, encoding='utf-8')
    
def rovoc_parse_(label_file, key_dict):
    """parse rotation VOC style dataset label file
    
    Arguments:
        label_file {str} -- label file path
    
    Returns:
        dict, {'bbox': [cx, cy, w, h, theta (rad/s)], 'label': class_name} -- objects' location and class
    """
    objects = []
    global_infos ={}
    #key_dict, key: new_key  value: old_key
    tree = ET.parse(label_file)
    root = tree.getroot()

    for new_key, old_key in key_dict.items():
        global_infos[new_key] = root.find(old_key).text


    for single_object in root.findall('object'):
        robndbox = single_object.find('robndbox')
        object_struct = {}

        cx = float(robndbox.find('cx').text)
        cy = float(robndbox.find('cy').text)
        w = float(robndbox.find('w').text)
        h = float(robndbox.find('h').text)
        theta = float(robndbox.find('angle').text)

        object_struct['bbox'] = [cx, cy, w, h, theta]
        object_struct['label'] = single_object.find('name').text
        
        object_struct['typename']=single_object.find('typename').text
        object_struct['classname']=single_object.find('classname').text
        object_struct['modelname']=single_object.find('modelname').text

        
        objects.append(object_struct)
    return global_infos, objects
def split_image(img, subsize=1024, gap=200, mode='keep_all'):
    img_height, img_width = img.shape[0], img.shape[1]

    start_xs = np.arange(0, img_width, subsize - gap)
    if mode == 'keep_all':
        start_xs[-1] = img_width - subsize if img_width - start_xs[-1] <= subsize else start_xs[-1]
    elif mode == 'drop_boundary':
        if img_width - start_xs[-1] < subsize - gap:
            start_xs = np.delete(start_xs, -1)
    start_xs[-1] = np.maximum(start_xs[-1], 0)

    start_ys = np.arange(0, img_height, subsize - gap)
    if mode == 'keep_all':
        start_ys[-1] = img_height - subsize if img_height - start_ys[-1] <= subsize else start_ys[-1]
    elif mode == 'drop_boundary':
        if img_height - start_ys[-1] < subsize - gap:
            start_ys = np.delete(start_ys, -1)
    start_ys[-1] = np.maximum(start_ys[-1], 0)

    subimages = dict()
    for start_x in start_xs:
        for start_y in start_ys:
            end_x = np.minimum(start_x + subsize, img_width)
            end_y = np.minimum(start_y + subsize, img_height)
            subimage = img[start_y:end_y, start_x:end_x, ...]
            coordinate = (start_x, start_y)
            subimages[coordinate] = subimage
    return subimages


def read_gaofen(img_file):
    # 返回的图像uint8类型，[r,g,b]
    '''
    if imgFormat == "png" or imgFormat=="jpg":
        img_bgr = cv2.imread(img_file)
        [img_b, img_g, img_r] = cv2.split(img_bgr)
        img_rgb = cv2.merge([img_r, img_g, img_b])
        img_bgr = cv2.merge([img_b, img_g, img_r])
    elif imgFormat == "tif" or imgFormat=="tiff":
    '''
    if img_file is not None:
        data = gdal.Open(img_file)
        #print("finished gdal.Open")
        width = data.RasterXSize
        height = data.RasterYSize

        if data.RasterCount==4:
            #高分2多光谱，4bands，[b,g,r,Nr]
            band1 = data.GetRasterBand(3)
            img_r = band1.ReadAsArray(0,0,width,height)
            img_r = (img_r-img_r.min())/(img_r.max()-img_r.min())
            img_r = np.round(img_r*255)
            img_r = np.uint8(img_r)

            band2 = data.GetRasterBand(2)
            img_g = band2.ReadAsArray(0,0,width,height)
            img_g = (img_g-img_g.min())/(img_g.max()-img_g.min())
            img_g = np.round(img_g*255)
            img_g = np.uint8(img_g)

            band3 = data.GetRasterBand(1)
            img_b = band3.ReadAsArray(0,0,width,height)
            img_b = (img_b-img_b.min())/(img_b.max()-img_b.min())
            img_b = np.round(img_b*255)
            img_b = np.uint8(img_b)
            img_rgb = cv2.merge([img_r, img_g, img_b])
            img_bgr = cv2.merge([img_b, img_g, img_r])

        elif data.RasterCount==3:
            #高分1三通道图
            band1 = data.GetRasterBand(1)
            img_r = band1.ReadAsArray(0,0,width,height)
            img_r = (img_r-img_r.min())/(img_r.max()-img_r.min())
            img_r = np.round(img_r*255)
            img_r = np.uint8(img_r)

            band2 = data.GetRasterBand(2)
            img_g = band2.ReadAsArray(0,0,width,height)
            img_g = (img_g-img_g.min())/(img_g.max()-img_g.min())
            img_g = np.round(img_g*255)
            img_g = np.uint8(img_g)

            band3 = data.GetRasterBand(3)
            img_b = band3.ReadAsArray(0,0,width,height)
            img_b = (img_b-img_b.min())/(img_b.max()-img_b.min())
            img_b = np.round(img_b*255)
            img_b = np.uint8(img_b)
            img_rgb = cv2.merge([img_r, img_g, img_b])
            img_bgr = cv2.merge([img_b, img_g, img_r])

        elif data.RasterCount == 1:
            band1 = data.GetRasterBand(1)
            img_arr = band1.ReadAsArray(0,0,width,height)
            img_arr = (img_arr-img_arr.min())/(img_arr.max()-img_arr.min())
            img_arr = np.uint8(np.round(img_arr*255))

            img_rgb = cv2.merge([img_arr,img_arr,img_arr])
            img_bgr = cv2.merge([img_arr,img_arr,img_arr])
    else:
        #raise TypeError("Please input correct image format: png, jpg, tif/tiff!")
        img_rgb = None
        img_bgr = None
    return img_rgb, img_bgr

def crop_image_main(image_path, label_path, image_save_path, label_save_path):

    for idx, label_file in enumerate(os.listdir(label_path)):
        print(idx, label_file)
        file_name = label_file.split('.xml')[0]
        label_file = os.path.join(label_path, file_name + '.xml')
        
        image_file = os.path.join(image_path, file_name + '.tiff')
        if not os.path.exists(image_file):
            image_file = os.path.join(image_path, file_name + '.tif')
        
        _, img = read_gaofen(image_file)

        key_dict = {"data":"filename","SatelliteID":"SatelliteID","SensorID":"SensorID","ReceiveTime":"ReceiveTime","OrbitID":"OrbitID",\
            "ProduceType":"ProduceType","SceneID":"SceneID","ProductID":"ProductID","ProductLevel":"ProductLevel","Target_location":"Target_location"}

        infos, objects = rovoc_parse_(label_file, key_dict)

        bboxes = np.array([obj['bbox'] for obj in objects])

        labels = [obj['label'] for obj in objects]
        typename = [obj['typename'] for obj in objects]
        classname = [obj['classname'] for obj in objects]
        modelname = [obj['modelname'] for obj in objects]

        subimages = split_image(img, subsize=1024, gap=200)
        subimage_coordinates = list(subimages.keys())

        bboxes_ = bboxes.copy()
        labels_ = labels.copy()
        for subimage_coordinate in subimage_coordinates:
            sub_objects = []
            subimage_labels, subimage_typename, subimage_classname, subimage_modelname = [], [], [], []
            bboxes_[:, 0] = bboxes[:, 0] - subimage_coordinate[0]
            bboxes_[:, 1] = bboxes[:, 1] - subimage_coordinate[1]
            cx_bool = np.logical_and(bboxes_[:, 0] >= 0, bboxes_[:, 0] < 1024)
            cy_bool = np.logical_and(bboxes_[:, 1] >= 0, bboxes_[:, 1] < 1024)
            #subimage_bboxes = bboxes_[np.logical_and(cx_bool, cy_bool)]
            subimage_objects = {}
            mm = np.logical_and(cx_bool, cy_bool)
            for idx, flag in enumerate(mm):
                if flag:
                    subimage_objects = objects[idx]
                    subimage_objects['bbox'] = bboxes_[idx].tolist()
                    subimage_objects['label'] = labels_[idx]
                    subimage_objects['typename'] = typename[idx]
                    subimage_objects['classname'] = classname[idx]
                    subimage_objects['modelname'] = modelname[idx]
                    sub_objects.append(subimage_objects)

            if len(sub_objects) == 0:
                continue
            img = subimages[subimage_coordinate]

            if np.mean(img) == 0:
                continue

            label_save_file = os.path.join(label_save_path, '{}__{}_{}.xml'.format(file_name, subimage_coordinate[0], subimage_coordinate[1]))
            image_save_file = os.path.join(image_save_path, '{}__{}_{}.png'.format(file_name, subimage_coordinate[0], subimage_coordinate[1]))

            cv2.imencode('.png', img)[1].tofile(image_save_file)
            
            filename = '{}__{}_{}'.format(file_name, subimage_coordinate[0], subimage_coordinate[1])
            simple_xml_dump_(infos, list(key_dict.keys()), sub_objects, filename, label_save_file)

if __name__=='__main__':

    image_path = 'H:/测试数据0615/123/images'
    label_path = 'H:/测试数据0615/123/labels'

    image_save_path = 'H:/测试数据0615/123/切片数据/images'
    if not os.path.isdir(image_save_path):
        os.makedirs(image_save_path)

    label_save_path = 'H:/测试数据0615/123/切片数据/labelxmls'
    if not os.path.isdir(label_save_path):
        os.makedirs(label_save_path)

    crop_image_main(image_path, label_path, image_save_path, label_save_path)

