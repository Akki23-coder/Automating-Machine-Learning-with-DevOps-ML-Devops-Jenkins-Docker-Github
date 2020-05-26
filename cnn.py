# create model
model = Sequential()


convlayers = int(input())
first_layer_nfilter = int(input())
first_layer_filter_size = int(input())
first_layer_pool_size = int(input())

this_layer = 'No. of convolve layers : ' + str(convlayers)
this_layer = this_layer + '\nLayer 1'
this_layer = this_layer + '\nNo of filters : ' + str(first_layer_nfilter) + '\nFilter Size : ' + str(first_layer_filter_size) + '\nPool Size : ' + str(first_layer_pool_size)

model.add(Conv2D(first_layer_nfilter, (first_layer_filter_size, first_layer_filter_size),
                 padding = "same",
                 input_shape = input_shape))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (first_layer_pool_size, first_layer_pool_size)))

#Subsequent CRP sets
for i in range(1,convlayers):
    nfilters = int(input())
    filter_size = int(input())
    pool_size = int(input())
    this_layer = this_layer + '\nLayer ' + str(i+1) + ': '
    this_layer = this_layer + '\nNo of filters : ' + str(nfilters) + '\nFilter Size : ' + str(filter_size) + '\nPool Size : ' + str(pool_size)
    model.add(Conv2D(nfilters, (filter_size, filter_size),padding = "same"))
    model.add(Activation("relu"))
    model.add(MaxPooling2D(pool_size = (pool_size, pool_size)))

# Fully connected layers (w/ RELU)
model.add(Flatten())

fc_input = int(input())

this_layer = this_layer + '\nNo. of FC Layers : ' + str(fc_input+1)

for i in range(0,fc_input):
    no_neurons = int(input())
    this_layer = this_layer + '\nNeurons in Layer ' + str(i+1) + ' : ' + str(no_neurons)
    model.add(Dense(no_neurons))
    model.add(Activation("relu"))

# Softmax (for classification)
model.add(Dense(num_classes))
model.add(Activation("softmax"))
           
this_layer = this_layer + '\nNeurons in Layer ' + str(fc_input + 1) + ' : ' + str(num_classes)

model.compile(loss = 'categorical_crossentropy',
              optimizer = keras.optimizers.Adadelta(),
              metrics = ['accuracy'])
    
print(model.summary())





