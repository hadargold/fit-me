import os
import sys
import random
import signal
import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from neuralnet import *
from nnmath import *
from genetics import GeneticAlgorithm, GAKill
from PIL import Image

# https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html

def read_data(path):
    data = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        for dirname in dirnames:
            for f in os.listdir(dirpath + dirname):
                try:
                    # image = Image.open(dirpath + dirname + '/' + f)
                    # image = image.resize((100, 100))
                    # img = np.ravel(image) / 255
                    # img = np.ravel(misc.imread((dirpath + dirname + '/' + f).resize((100, 100)), flatten=True)) / 255
                    img = np.ravel(misc.imread(dirpath + dirname + '/' + f, flatten=True)) / 255
                    data.append((dirname, img))
                except:
                    pass
    return data


def process(target, url, epochs, vis):

    # Set Numpy warning level
    np.seterr(over='ignore')

    # Define target shapes
    targets = np.array(['Inverted Triangle', 'Hourglass','Triangle', 'Rectangle', "Round"]) #



    if target == 'train':
        # Check the input arguments
        # if len(argv) < 5:
        #     print ("Usage: python shape.py train <GA-epochs> <SGD-epochs> <visFlag>")
        #     sys.exit()

        # Load the training data
        training_data = read_data('training_data/')
        test_data = read_data('test_data/')

        # Shuffle for more randomness
        random.shuffle(training_data)

        # Create a GA of neural nets
        print training_data
        img_len = len(training_data[0][1])
        ga = GeneticAlgorithm(epochs=int(epochs),
                              mutation_rate=0.01,
                              data=training_data,
                              targets=targets,
                              obj=NeuralNet,
                              args=[img_len, 10, 4, 5]) # num of classes

        # Create the 1st generation
        print "Creating population..."
        ga.populate(200)

        print "Initiating GA heuristic approach..."

        # Start evolution
        errors = []
        while ga.evolve():
            try:
                ga.evaluate()
                ga.crossover()
                ga.epoch += 1

                # Store error
                errors.append(ga.error)
                print "error: " + str(ga.error)
            except GAKill as e:
                print e.message
                break

        vis = bool(vis)
        if vis:
            # Plot error over time
            fig = plt.figure()
            plt.plot(range(ga.epoch), errors)
            plt.xlabel('Time (Epochs)')
            plt.ylabel('Error')
            plt.show()

        print "--------------------------------------------------------------\n"

        nn = ga.fittest()
        epochs = int(epochs)
        if epochs:
            print "Initiating Gradient Descent optimization..."
            try:
                nn.gradient_descent(training_data, targets, epochs, test_data=test_data, vis=vis)
            except GAKill as e:
                print e.message

        nn.save("neuralnet.pkt")
        print "Done!"

    elif target == "validate":
        test_data = read_data('test_data/')

        nn = NeuralNet([], build=False)
        nn.load("neuralnet.pkt")

        accuracy = nn.validate(targets, test_data)
        print "Accuracy: " + str(accuracy)

    elif target == "predict":
        # Check the arguments
        # if len(argv) < 3:
        #     print "Usage: python shape.py test <image>"
        #     sys.exit()

        # Read the test image
        img = np.ravel(misc.imread(url, flatten=True)) / 255

        # Build the neural net from file
        nn = NeuralNet([], build=False)
        nn.load("neuralnet.pkt")

        # Predict
        activations, zs = nn.feed_forward(img)
        outfile = open("output.txt", "w")
        outfile.writelines(targets[np.argmax(activations[-1])])
        outfile.close()
        print targets[np.argmax(activations[-1])]
        return targets[np.argmax(activations[-1])]

    else:
        print "ERROR: Unknown command " + target


def signal_handler(signal, frame):
    raise (GAKill("\nAborting Search..."))


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    arguments = sys.argv
    target = arguments[0]
    url = arguments[1]
    epochs = arguments[2]
    vis = arguments[3]
    process(target, url, epochs, vis)
