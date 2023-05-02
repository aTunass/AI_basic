import tensorflow as tf

def _downsample_cnn_block(block_input, channel, is_first = False):
  if is_first:  
    conv1 = tf.keras.layers.Conv2D(filters=channel, kernel_size=3, strides=1)(block_input)
    conv2 = tf.keras.layers.Conv2D(filters=channel, kernel_size=3, strides=1)(conv1)
    return [block_input, conv1, conv2]
  else:
    maxpool = tf.keras.layers.MaxPool2D(pool_size=2)(block_input)
    conv1 = tf.keras.layers.Conv2D(filters=channel, kernel_size=3, strides=1)(maxpool)
    conv2 = tf.keras.layers.Conv2D(filters=channel, kernel_size=3, strides=1)(conv1)
    return [maxpool, conv1, conv2]

ds_block1 = _downsample_cnn_block(tf.keras.layers.Input(shape=(572, 572, 1)), channel=64, is_first = True)
print(ds_block1)
ds_block2 = _downsample_cnn_block(ds_block1[-1], channel=128)
ds_block3 = _downsample_cnn_block(ds_block2[-1], channel=256)
ds_block4 = _downsample_cnn_block(ds_block3[-1], channel=512)
ds_block5 = _downsample_cnn_block(ds_block4[-1], channel=1024)