# This file is useful for reading the contents of the ops generated by ruby.
# You can read any graph defination in pb/pbtxt format generated by ruby
# or by python and then convert it back and forth from human readable to binary format.

import tensorflow.compat.v1 as tf
from google.protobuf import text_format

def pbtxt_to_graphdef(filename):
  with open(filename, 'r') as f:
    graph_def = tf.GraphDef()
    file_content = f.read()
    text_format.Merge(file_content, graph_def)
    tf.import_graph_def(graph_def, name='')
    tf.train.write_graph(graph_def, 'pbtxt/', 'protobuf.pb', as_text=False)

def graphdef_to_pbtxt(filename): 
  with tf.gfile.FastGFile(filename,'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')
    tf.train.write_graph(graph_def, 'pbtxt/', 'protobuf.pbtxt', as_text=True)
  return

if __name__ == "__main__":

    graphdef_to_pbtxt('ssd_mobilenet_v1_coco_2017_11_17/frozen_inference_graph.pb')  # here you can write the name of the file to be converted
    # and then a new file will be made in pbtxt directory.