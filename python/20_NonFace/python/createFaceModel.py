import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Create the model
model = Sequential()

# Add convolutional layers for face recognition
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D(2, 2))
model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Create a training data generator
train_datagen = ImageDataGenerator(rescale=1.0/255)
train_generator = train_datagen.flow_from_directory('images/non', target_size=(150, 150), batch_size=32, class_mode='binary')

# Calculate steps_per_epoch
total_samples = len(train_generator.filenames)
batch_size = train_generator.batch_size
steps_per_epoch = total_samples // batch_size

# Train the model
model.fit(train_generator, epochs=15, steps_per_epoch=steps_per_epoch, verbose=0)

# Save the model
model.save('face_recognition_model.h5')
