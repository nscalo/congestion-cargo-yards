# Congestion on Cargo Yards



# Model Downloader

## Downloading the Model

Try Model "Person-Vehicle-Bike":

```bash

root@docker-box:/opt/intel/openvino/deployment_tools/tools/model_downloader# python3 downloader.py --name "person-vehicle-bike-detection-crossroad-0078" --output_dir /home/project/models

```

Download TF Model "SSD-Mobilenet-v1-COCO":

[https://github.com/bkj/tf-models/blob/master/research/object_detection/object_detection_tutorial.ipynb](https://github.com/bkj/tf-models/blob/master/research/object_detection/object_detection_tutorial.ipynb)

```bash

python tensorflow_toolkit.py

```

```bash

python3 tensorflow_convert_pb_to_pbtxt.py

```

## Visualizing TensorflowModel using Tensorboard

```bash

root@docker-box:/home/project/toolkit# python3 tensorboard.py

```

![../images/tensorboard.PNG](../images/tensorboard.PNG)

## Visualizing TensorflowModel using Netron

```bash

root@37f902f9e5aa/home/project# pip3 install netron
root@37f902f9e5aa:/home/project/toolkit/ssd_mobilenet_v1_coco_2017_11_17# netron -b frozen_inference_graph.pb --host 0.0.0.0 --port 8080
Serving 'frozen_inference_graph.pb' at http://0.0.0.0:8080

```

![../images/netron-half.PNG](../images/netron-half.PNG)

## Detect Vehicles from OpenVINO Model

```bash

root@37f902f9e5aa:/home/project/congestion-cargo-yards# python3 main.py -m /home/project/models/intel/person-vehicle-bike-detection-crossroad-0078/FP32/person-vehicle-bike-detection-crossroad-0078.xml -vds "/home/project/images/automated-queue.png" -d CPU -bt 1 --batch_size 1 -pt 0.11

```

![../images/automated-queue.0.png](../images/automated-queue.0.png)



## Convert TF Model to OpenVINO
