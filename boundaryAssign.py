print("//////////////////////////////////////////////////////////////////////")
print("                 Mechanical Engineering Software Club                 ")
print("         Research and Human Resources Development Department          ")
print("                  Codes Compiled by Anas Nur Fauzan                   ")
print("//////////////////////////////////////////////////////////////////////")
print("              WELCOME TO OPENFOAM CASE FOLDER GENERATOR")
print("--------------------------FLOW SIMULATION-----------------------------")
print("//////////////////////////////////////////////////////////////////////")

import linecache
import os

def inputValues():
    global turbIntensity
    turbIntensity = 0.01
    global Cu
    Cu = 0.09
    print("Assigned coefficients list check...")
    print("I : " + str(turbIntensity))
    print("Cu: " + str(Cu))
    print("Input Flow Velocity: ")
    global flowVelocity
    flowVelocity = float(input())
    print("Input Reference Length Scale = ")
    global refLength
    refLength = float(input())

def kwSST():
    inputValues()
    turbKE = pow(flowVelocity * turbIntensity, 2) * 1.5
    turbSpecDiss = pow(turbKE, 0.5) / (pow(Cu, 0.25) * refLength)
    print("Freestream Velocity = " + str(flowVelocity) + " m/s")
    print("Calculated Initial Turbulence Kinetic Energy = " + str(turbKE))
    print("Calculated Initial Turbulence Specific Dissipation = " + str(turbSpecDiss))

def kEpsilon():
    inputValue()
    turbKE = pow(flowVelocity * turbIntensity, 2) * 1.5
    turbDissRate = pow(turbKE, 1.5) * pow(cu, 0.75) / refLength
    print("Freestream Velocity = " + str(flowVelocity) + "m/s")
    print("Calculated Initial Turbulence Kinetic Energy = " + str(turbKE))
    print("Calculated Initial Turbulence Dissipation Rate = " + str(turbDissRate))

def writeBoundary():
    boundary_1 = linecache.getline('boundary', 23)
    boundary_2 = linecache.getline('boundary', 30)
    boundary_3 = linecache.getline('boundary', 36)
    boundary_4 = linecache.getline('boundary', 42)
    print("Detected boundaries: ")
    print(boundary_1,boundary_2,boundary_3,boundary_4)
    os.mkdir()

print("Initial Condition Values Calculator Initiated....")
print("Available Turbulence Models: ")
print("1. k-W SST")
print("2. k-Epsilon")
print("Choose Turbulence Model: ")
choosenTurbModel = float(input())
if choosenTurbModel == 1 :
    kwSST()
    writeBoundary()
elif choosenTurbModel == 2 :
    kEpsilon()
else :
    print("Please choose available models!")
