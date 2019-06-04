import random
import matplotlib.pyplot as pyplot
import matplotlib.pyplot as inversePlot
import math

maxRandValue = float(input(" Enter the max range of the random Value"))
firstValue = float(input("Enter the first seed value to generate random sequence"))
totalNumber = float(input("Enter the number of random numbers to be generated"))
randomSequence = []
counter = 0

while (counter < totalNumber):
     randomSequence.append(round((((firstValue * random.randint(1, 100) +
                                    random.randint(1,100)) % maxRandValue)/maxRandValue), 5))
     counter = counter + 1
print("The random sequence generated :")
randomSequence.sort()
print(randomSequence)


def switchInput():
    print("Select the distribution for which CDF is to be generated: \n "
          "1. GEOMETRIC 2.EXPONENTIAL 3.UNIFORM 4.EXIT")
    inputSelection = int(input("Enter the integer corresponding to the distribution"))
    if(inputSelection ==  1 ):
        geometricDistribution()
    elif(inputSelection == 2 ):
        exponentialDistribution()
    elif(inputSelection == 3):
        uniformDistribution()
    else:
        exitFunction()

def geometricDistribution():
    print("Geometric Distribution")
    propabilityValue = float(input("Enter the probability value for the distribution"))
    counter = 0
    geometricFile = open("Geometric Distribution.txt", 'w')
    geometricFile.write("The coordinate valued for the geometric distribution \n")

    geometric =[]
    while(counter < totalNumber):
        geometric.append(round( 1 - math.pow(1 - propabilityValue,randomSequence[counter]),4))
        geometricFile.write("(" + str(randomSequence[counter]) + "," + str(geometric[counter]) + ")\n")
        counter= counter+1

    plotData  = pyplot.gcf()
    pyplot.title("Geometric Distribution")
    pyplot.xlabel("Random Numbers")
    pyplot.ylabel("F(x)")
    pyplot.plot(randomSequence, geometric, 'o')
    pyplot.show()
    plotData.savefig('Geometric.pdf' , dpi = 100)

    # Inverse Function
    geometricFile.write("\n The coordinate values for the geometric inverse function CDF \n")
    geoInverse = []
    counter = 0
    while( counter < totalNumber):
        geoInverse.append(math.log(1 - geometric[counter])/math.log(1- propabilityValue))
        geometricFile.write("(" + str(randomSequence[counter]) + "," + str(geoInverse[counter]) + ")\n")
        counter = counter + 1
    inverseGraph = inversePlot.gcf()
    inversePlot.title("Inverse Geometric")
    inversePlot.xlabel("Random Numbers")
    inversePlot.ylabel("Inverse F(x)")
    inversePlot.plot(randomSequence,geoInverse,'o')
    inversePlot.show()
    inverseGraph.savefig('Geometric_Inverse.pdf', dpi = 100)
    print(" File has been generated with coordinate values")
    geometricFile.close()
    switchInput()

def exponentialDistribution():
    print(" Exponential Distribution")
    lambdaValue = float(input("Enter the parameter Lambda for the distribution"))
    exponential = []
    exponentialFile = open("Exponential.txt", 'w')
    exponentialFile.write(" The coordinate value for Exponential Distribution CDF \n")
    counter = 0

    while (counter < totalNumber):
        exponential.append(1 - math.exp(-lambdaValue*randomSequence[counter]))
        exponentialFile.write("(" + str(randomSequence[counter]) + "," +
                              str(exponential[counter]) + ")\n")
        counter = counter + 1
    plotFig = pyplot.gcf()
    pyplot.title("Exponential Distribution")
    pyplot.xlabel("Random Number")
    pyplot.ylabel("F(x)")
    pyplot.plot(randomSequence,exponential)
    pyplot.show()
    plotFig.savefig('Exponential_Graph.pdf', dpi = 100)

    exponentialFile.write(" The coordinate value for Inverse Exponential Distribution CDF \n")

    counter = 0
    exponentialInverse = []
    while(counter < totalNumber):
        exponentialInverse.append(math.exp(-lambdaValue*exponential[counter]))
        exponentialFile.write("(" + str(randomSequence[counter]) + "," +
                              str(exponentialInverse[counter]) + ")\n")
        counter= counter+1
        inverseFig = inversePlot.gcf()
    inversePlot.title("Inverse Exponential")
    inversePlot.xlabel("Random Numbers")
    inversePlot.ylabel("F(x)")
    inversePlot.plot(randomSequence,exponentialInverse)
    inversePlot.show()
    inverseFig.savefig('Exponential_Inverse_Graph.pdf', dpi=100, )
    print(" File has been generated with coordinate values")
    exponentialFile.close()
    switchInput()

def uniformDistribution():
    print("Uniform Distribution")
    a = float(input(" Enter the first parameter"))
    b = float(input(" Enter the second parameter"))
    uniform =[]
    counter = 0
    uniformFile = open("Uniform Distribution.txt", 'w')
    uniformFile.write(" The CDF Plot coordinates are as follows: \n ")
    while(counter < totalNumber):
        randomSequence[counter] = randomSequence[counter]* maxRandValue
        uniform.append(round((randomSequence[counter] - a)/(b - a),2))
        uniformFile.write("(" +str(randomSequence[counter]) + "," + str(uniform[counter]) + ")" + "\n")
        counter = counter + 1

    plotGraph = pyplot.gcf()
    pyplot.plot(randomSequence,uniform)
    pyplot.title(" Uniform Distribution")
    pyplot.xlabel("Random Number ")
    pyplot.ylabel("F(x)")
    pyplot.show()
    plotGraph.savefig("Uniform_Distribution.pdf", dpi = 100)

    uniformFile.write("\n The coordinate values for the Inverse Uniform Distribution :\n")
    inverseUniform =[]
    counter = 0;
    while(counter< totalNumber):
        inverseUniform.append(b - math.pow(uniform[counter],-1) / (b - a), )
        uniformFile.write("(" + str(randomSequence[counter]) + "," + str(inverseUniform[counter]) + ")\n")
        counter = counter + 1
    inversePlot.title("Inverse Uniform Distribution")
    inversePlot.xlabel("Random Numbers")
    inversePlot.ylabel("Inverse Function")
    inversePlot.plot(randomSequence,inverseUniform)
    inverseGraph = inversePlot.gcf()
    inversePlot.show()
    inverseGraph.savefig("Uniform_Inverse.pdf", dpi = 100)
    print(" File has been generated with coordinate values")
    uniformFile.close()
    switchInput()

def exitFunction():
    print("The program has been terminated")
switchInput()

