import tensorflow as tf
import tensorflow_datasets as tfds
from IPython.display import clear_output
from tensorflow_examples.models.pix2pix import pix2pix
dataset,info=tfds.load('oxford_iiit_pet:3.*.*',with_info=True)
import matplotlib.pyplot as plt

def normalize(input_image, input_mask):
    input_image=tf.cast(input_image,tf.float32)/255.0
    input_mask-=1
    return input_image,input_mask

@tf.function
def load_image_train(datapoint):
    input_image=tf.image.resize(datapoint['image'],(128,128))
    input_mask = tf.image.resize(datapoint['segmentation_mask'], (128, 128))
    if tf.random.uniform(())>0.5:
        input_image=tf.image.flip_left_right(input_image)
        input_mask = tf.image.flip_left_right(input_mask)
    input_image,input_mask=normalize(input_image,input_mask)
    return input_image,input_mask

def load_image_test(datapoint):
    input_image = tf.image.resize(datapoint['image'], (128, 128))
    input_mask = tf.image.resize(datapoint['segmentation_mask'], (128, 128))
    input_image,input_mask=normalize(input_image,input_mask)
    return input_image,input_mask

TRAIN_LENGTH=info.splits['train'].num_examples
BATCH_SIZE=64
BUFFEE_SIZE=1000
STEPS_PER_EPOCH=TRAIN_LENGTH

train=dataset['train'].map(load_image_train,num_parallel_calls=tf.data.experimental.AUTOTUNE)
test=dataset['test'].map(load_image_test())

train_dataset=train.cache().shuffle(BUFFEE_SIZE).batch(BATCH_SIZE).repeat()
train_dataset=train_dataset.prefetch(buffer_size=tf.data.experimental.AUTOTUNE)
test_dataset=test.batch(BATCH_SIZE)

def display(display_list):
    plt.figure(figsize=(15,15))
    title=['Imagen de entrada','Mascara verdadera','Prediccion']
    for i in range(len(display_list)):
        plt.subplot(1,len(display_list),i+1)
        plt.title(title[i])
        plt.imshow(tf.keras.preprocessing.image.array_to_img(display_list[i]))
    plt.show()

for image,mask in train.take(1):
    example_image, example_mask=image,mask
display([example_image,example_mask])