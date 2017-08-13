import json
from PIL import Image
from labelimage import label_image, loadingmodel
from testurlimage import getimage
from pprint import pprint
import sys


def runservice(input = 'testjsons/test1.json', threshold = 0.2):
    try:
        with open(input) as data_file:
            data = json.load(data_file)
        pprint(data['images'])
    except:
        print('Reading JSON Error, file not found or incorrect format. Please check ' + input)
        exit(1)

    detection_graph, category_index = loadingmodel('ssd_mobilenet_v1_coco_11_06_2017/frozen_inference_graph.pb',
                                                   'ssd_mobilenet_v1_coco_11_06_2017/mscoco_label_map.pbtxt')

    finallist = {}
    finallist['results'] = []
    for url in data['images']:
        status, img = getimage(url)

        jdict = {}
        jdict['url'] = url
        if status == 'Okay' and img is not None:
            currjson = label_image(Image.fromarray(img),detection_graph, category_index, displayimage=False, saveimage=False, threshold = threshold)
            jdict['classes'] = currjson
        else:
            jdict['error'] = status

        finallist['results'].append(jdict)

    print(finallist)

    output = input + '_output.json'
    with open(output, 'w', encoding='utf-8') as outfile:
        json.dump(finallist, outfile, indent=4, separators=(',', ': '))




def main():
    if len(sys.argv) > 3:
        print('Please input the json file only')
    elif len(sys.argv) == 3:
        runservice(input=sys.argv[1], threshold = float(sys.argv[2]));
    else:
        print('Json file and/or threshold are not given, using the default file:testjsons/test1.json, threshold = 0.2')
        runservice();


if __name__ == '__main__':
    main()