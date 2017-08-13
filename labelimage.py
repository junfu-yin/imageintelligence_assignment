import numpy as np
import tensorflow as tf
import datetime

import json
from matplotlib import pyplot as plt
from PIL import Image

from object_detection.utils import label_map_util

from object_detection.utils import visualization_utils as vis_util

from pprint import pprint


def makejson(scores, classes, labels, threshold):
    myscore = scores[0]
    myclass = classes[0].astype(np.int32)

    if(myscore[0] < threshold):
        return''
    myscore,myclass = zip(*((score, cls) for score, cls in zip(myscore, myclass) if score >= threshold))

    score_titles = [{'class': labels[t]['name'], 'confidence': str(s)} for t, s in zip(myclass, myscore)]
    # json_data = json.dumps(score_titles)
    return score_titles
    # pprint(score_titles)
    # json_data = json.dump(json_data)
    # pprint(json_data)


def loadingmodel(model, label):
    NUM_CLASSES = 90


    detection_graph = tf.Graph()
    with detection_graph.as_default():
      od_graph_def = tf.GraphDef()
      with tf.gfile.GFile(model, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')
    #
    #
    label_map = label_map_util.load_labelmap(label)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    return detection_graph, category_index
    # print(category_index)


def label_image(image, detection_graph, category_index, outputimagepath = 'testimages/', displayimage=True, saveimage=True, threshold = 0.5):
    print('Labelling the image...')
    IMAGE_SIZE = (12, 8)

    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
            # for image_path in TEST_IMAGE_PATHS:

            # the array based representation of the image will be used later in order to prepare the
            # result image with boxes and labels on it.
            # image = Image.open(imagepath)
            (im_width, im_height) = image.size
            image_np = np.array(image.getdata()).reshape((im_height, im_width, 3)).astype(np.uint8)
            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
            image_np_expanded = np.expand_dims(image_np, axis=0)
            image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
            # Each box represents a part of the image where a particular object was detected.
            boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
            # Each score represent how level of confidence for each of the objects.
            # Score is shown on the result image, together with the class label.
            scores = detection_graph.get_tensor_by_name('detection_scores:0')
            classes = detection_graph.get_tensor_by_name('detection_classes:0')
            num_detections = detection_graph.get_tensor_by_name('num_detections:0')
            # Actual detection.
            (boxes, scores, classes, num_detections) = sess.run(
              [boxes, scores, classes, num_detections],
              feed_dict={image_tensor: image_np_expanded})

            # print(scores)
            # with open(outputjsonpath, 'w') as f:
            #     f.write()

            json_data = makejson(scores, classes, labels =category_index, threshold=threshold)

            # Visualization of the results of a detection.
            if(displayimage and saveimage):
                vis_util.visualize_boxes_and_labels_on_image_array(
                  image_np,
                  np.squeeze(boxes),
                  np.squeeze(classes).astype(np.int32),
                  np.squeeze(scores),
                  category_index,
                  use_normalized_coordinates=True,
                  line_thickness=8)

                if(displayimage):
                    plt.figure(figsize=IMAGE_SIZE)
                    plt.imshow(image_np)
                    plt.show()

                if (saveimage):
                    im = Image.fromarray(image_np)
                    im.save(outputimagepath + str(datetime.datetime.now()) + '_labeled.jpg')

            return json_data
              # print("here already")



def main():
    imagepath='testimages/image1.jpg'
    image = Image.open(imagepath)
    label_image(image,imagepath, False, False)

    imagepath='testimages/image1.jpg'
    image = Image.open(imagepath)
    label_image(image,imagepath, False, False)


if __name__ == "__main__":
    main()

