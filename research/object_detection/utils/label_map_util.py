# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import logging

import tensorflow as tf
from google.protobuf import text_format
from object_detection.protos import string_int_label_map_pb2


def _validate_label_map(label_map):
  for item in label_map.item:
    if item.id < 1:
      raise ValueError('Label map ids should be >= 1.')


def create_category_index(categories):
  category_index = {}
  for cat in categories:
    category_index[cat['id']] = cat
  return category_index


def get_max_label_map_index(label_map):
  return max([item.id for item in label_map.item])


def convert_label_map_to_categories(label_map,
                                    max_num_classes,
                                    use_display_name=True):
  categories = []
  list_of_ids_already_added = []
  if not label_map:
    label_id_offset = 1
    for class_id in range(max_num_classes):
      categories.append({
          'id': class_id + label_id_offset,
          'name': 'category_{}'.format(class_id + label_id_offset)
      })
    return categories
  for item in label_map.item:
    if not 0 < item.id <= max_num_classes:
      logging.info('Ignore item %d since it falls outside of requested '
                   'label range.', item.id)
      continue
    if use_display_name and item.HasField('display_name'):
      name = item.display_name
    else:
      name = item.name
    if item.id not in list_of_ids_already_added:
      list_of_ids_already_added.append(item.id)
      categories.append({'id': item.id, 'name': name})
  return categories


def load_labelmap(path):
  with tf.gfile.GFile(path, 'r') as fid:
    label_map_string = fid.read()
    label_map = string_int_label_map_pb2.StringIntLabelMap()
    try:
      text_format.Merge(label_map_string, label_map)
    except text_format.ParseError:
      label_map.ParseFromString(label_map_string)
  _validate_label_map(label_map)
  return label_map


def get_label_map_dict(label_map_path, use_display_name=False):
  label_map = load_labelmap(label_map_path)
  label_map_dict = {}
  for item in label_map.item:
    if use_display_name:
      label_map_dict[item.display_name] = item.id
    else:
      label_map_dict[item.name] = item.id
  return label_map_dict


def create_category_index_from_labelmap(label_map_path):
  label_map = load_labelmap(label_map_path)
  max_num_classes = max(item.id for item in label_map.item)
  categories = convert_label_map_to_categories(label_map, max_num_classes)
  return create_category_index(categories)


def create_class_agnostic_category_index():
  return {1: {'id': 1, 'name': 'object'}}
