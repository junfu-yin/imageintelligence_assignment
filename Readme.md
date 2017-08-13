# Image Intelligence TakeHome Assignment

This is an assignment from Image Intelligence to detect objects in the user-given images. A tipical example of the input and output is as follows.

**Request:**

```json
{
  "images": [
    "http://example.com/image1",
    "http://example.com/image2",
    "http://badurl.com/image3",
  ]
}
```

**Success Response:**

```json
{
  "results": [
    {
      "url": "http://example.com/image1",
      "classes": [
        {
          "class": "person",
          "confidence": 0.8641
        },
        {
          "class": "dog",
          "confidence": 0.00516
        }
      ]
    },
    {
      "url": "http://example.com/image2",
      "classes": [
        {
          "class": "cat",
          "confidence": 0.2115
        }
      ]
    },
    {
      "url": "http://example.badurl.com/image3",
      "error": "Invalid URL"
    }
  ]
}
```

Basically, the program needs to retrieve every image from the input json file, and perform object detection on the image (if the url is valid), and output the objects detected and the corresponding confidences. Some low confident items are filtered.


## Before you start:

This program is running on python 3.6, Windows 10. Please Make sure you have installed tensorflow, opencv2, PIL, matplotlib and object_detection@tensorflow.

Since the instllations of other packages are well-known and can be easily found, I only illustrate how to install object_detection.


* Download https://github.com/tensorflow/models
* Before start installation, have a look at https://github.com/tensorflow/models/blob/master/object_detection/g3doc/installation.md
* In Windows, the statement "protoc object_detection/protos/*.proto --python_out=." may not be working. You can download the protoc exe from https://repo1.maven.org/maven2/com/google/protobuf/protoc/3.3.0/
* Choose the right executable for your pc and download it to the models-master folder, then run runproto.bat
* Follow https://github.com/tensorflow/models/blob/master/object_detection/g3doc/installation.md to finish the rest

python object_detection/builders/model_builder_test.py should return OK if you have successfully installed object_detection.


## How to use:

Simpily type:

``` bash
python main.py
```

you can also put the json file and the threshold as the parameters:

``` bash
python main.py testjsons/test2.json 0.3
```

where test2.json will be parsed and any object with confidence less than 0.3 will be filtered.


Please let me know if you need to know more.

Junfu


