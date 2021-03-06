#!/usr/bin/env python
#make executable in bash chmod +x PyRun

import sys
import inspect
import importlib
import os
import time

if __name__ == "__main__":
	
	#conesQuarterImageSet = {"RefImage" : "\"conesQuarter2.pgm\"", "TestImage" : "\"conesQuarter6.pgm\"", "CompGpuDispMap" : "\"computedDisparityConesQuarterGPU.pgm\"", "CompCpuDispMap" : "\"computedDisparityConesQuarterCPU.pgm\"", "NumDispVals" : "63", "ScaleBp" : "4.0f", "GroundTruthDisp" : "\"conesQuarterGroundTruth.pgm\"", "GroundTruthDispScale" : "4.0f"}
	#conesHalfImageSet = {"RefImage" : "\"conesHalf2.pgm\"", "TestImage" : "\"conesHalf6.pgm\"", "CompGpuDispMap" : "\"computedDisparityConesHalfGPU.pgm\"", "CompCpuDispMap" : "\"computedDisparityConesQuarterCPU.pgm\"", "NumDispVals" : "90", "ScaleBp" : "2.0f", "GroundTruthDisp" : "\"conesHalfGroundTruth.pgm\"", "GroundTruthDispScale" : "2.0f"}

	tsukubaImageSet = {"RefImage" : "\"tsukuba/scene1.row3.col3.ppm\"", "TestImage" : "\"tsukuba/scene1.row3.col4.ppm\"", "CompGpuDispMap" : "\"tsukuba/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"tsukuba/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "16", "ScaleBp" : "16.0f", "GroundTruthDisp" : "\"tsukuba/truedisp.row3.col3.pgm\"", "GroundTruthDispScale" : "16.0f"}
	venusImageSet = {"RefImage" : "\"venus/im2.ppm\"", "TestImage" : "\"venus/im6.ppm\"", "CompGpuDispMap" : "\"venus/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"venus/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "21", "ScaleBp" : "8.0f", "GroundTruthDisp" : "\"venus/disp2.pgm\"", "GroundTruthDispScale" : "8.0f"}

	barn1ImageSet = {"RefImage" : "\"barn1/im2.ppm\"", "TestImage" : "\"barn1/im6.ppm\"", "CompGpuDispMap" : "\"barn1/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"barn1/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "32", "ScaleBp" : "8.0f", "GroundTruthDisp" : "\"barn1/disp2.pgm\"", "GroundTruthDispScale" : "8.0f"}
	barn2ImageSet = {"RefImage" : "\"barn2/im2.ppm\"", "TestImage" : "\"barn2/im6.ppm\"", "CompGpuDispMap" : "\"barn2/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"barn2/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "32", "ScaleBp" : "8.0f", "GroundTruthDisp" : "\"barn2/disp2.pgm\"", "GroundTruthDispScale" : "8.0f"}
	bullImageSet = {"RefImage" : "\"bull/im2.ppm\"", "TestImage" : "\"bull/im6.ppm\"", "CompGpuDispMap" : "\"bull/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"bull/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "32", "ScaleBp" : "8.0f", "GroundTruthDisp" : "\"bull/disp2.pgm\"", "GroundTruthDispScale" : "8.0f"}
	mapImageSet = {"RefImage" : "\"map/im0.pgm\"", "TestImage" : "\"map/im1.pgm\"", "CompGpuDispMap" : "\"map/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"map/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "32", "ScaleBp" : "8.0f", "GroundTruthDisp" : "\"map/disp0.pgm\"", "GroundTruthDispScale" : "8.0f"}
	posterImageSet = {"RefImage" : "\"poster/im2.ppm\"", "TestImage" : "\"poster/im6.ppm\"", "CompGpuDispMap" : "\"poster/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"poster/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "32", "ScaleBp" : "8.0f", "GroundTruthDisp" : "\"poster/disp2.pgm\"", "GroundTruthDispScale" : "8.0f"}
	sawtoothImageSet = {"RefImage" : "\"sawtooth/im2.ppm\"", "TestImage" : "\"sawtooth/im6.ppm\"", "CompGpuDispMap" : "\"sawtooth/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"sawtooth/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "32", "ScaleBp" : "8.0f", "GroundTruthDisp" : "\"sawtooth/disp2.pgm\"", "GroundTruthDispScale" : "8.0f"}
	

	conesImageSetQuarterSize = {"RefImage" : "\"cones/im2.ppm\"", "TestImage" : "\"cones/im6.ppm\"", "CompGpuDispMap" : "\"cones/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"cones/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "63", "ScaleBp" : "4.0f", "GroundTruthDisp" : "\"cones/disp2.pgm\"", "GroundTruthDispScale" : "4.0f"}
	teddyImageSetQuarterSize = {"RefImage" : "\"teddy/im2.ppm\"", "TestImage" : "\"teddy/im6.ppm\"", "CompGpuDispMap" : "\"teddy/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"teddy/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "63", "ScaleBp" : "4.0f", "GroundTruthDisp" : "\"teddy/disp2.pgm\"", "GroundTruthDispScale" : "4.0f"}

	conesImageSetHalfSize = {"RefImage" : "\"conesH/im2.ppm\"", "TestImage" : "\"conesH/im6.ppm\"", "CompGpuDispMap" : "\"conesH/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"conesH/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "90", "ScaleBp" : "2.0f", "GroundTruthDisp" : "\"conesH/disp2.pgm\"", "GroundTruthDispScale" : "2.0f"}
	teddyImageSetHalfSize = {"RefImage" : "\"teddyH/im2.ppm\"", "TestImage" : "\"teddyH/im6.ppm\"", "CompGpuDispMap" : "\"teddyH/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"teddyH/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "90", "ScaleBp" : "2.0f", "GroundTruthDisp" : "\"teddyH/disp2.pgm\"", "GroundTruthDispScale" : "2.0f"}

	conesImageSetHalfSizeAdjusted = {"RefImage" : "\"conesHAdjusted/im2.ppm\"", "TestImage" : "\"conesHAdjusted/im6.ppm\"", "CompGpuDispMap" : "\"conesHAdjusted/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"conesHAdjusted/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "127", "ScaleBp" : "2.0f", "GroundTruthDisp" : "\"conesHAdjusted/disp2.pgm\"", "GroundTruthDispScale" : "2.0f"}
	teddyImageSetHalfSizeAdjusted = {"RefImage" : "\"teddyHAdjusted/im2.ppm\"", "TestImage" : "\"teddyHAdjusted/im6.ppm\"", "CompGpuDispMap" : "\"teddyHAdjusted/computedDisparityMapTsukubaGPU.pgm\"", "CompCpuDispMap" : "\"teddyHAdjusted/computedDisparityMapTsukubaCPU.pgm\"", "NumDispVals" : "127", "ScaleBp" : "2.0f", "GroundTruthDisp" : "\"teddyH/disp2.pgm\"", "GroundTruthDispScale" : "2.0f"}

	imageSets = [tsukubaImageSet, venusImageSet, barn1ImageSet, barn2ImageSet, bullImageSet, mapImageSet, posterImageSet, sawtoothImageSet, conesImageSetQuarterSize, teddyImageSetQuarterSize, conesImageSetHalfSize, teddyImageSetHalfSize, conesImageSetHalfSizeAdjusted, teddyImageSetHalfSizeAdjusted]
	#imageSets = [tsukubaImageSet]
	#refImages = ["\"tsukuba1.pgm\"", "\"conesQuarter2.pgm\"", "\"conesHalf2.pgm\""]
	#testImages = ["\"tsukuba2.pgm\"", "\"conesQuarter6.pgm\"", "\"conesHalf6.pgm\""]
	#saveDispGpuOutput = ["\"computedDisparityMapTsukubaGPU.pgm\"", "\"computedDisparityConesQuarterGPU.pgm\"", "\"computedDisparityConesHalfGPU.pgm\""]
	#saveDispCpuOutput = ["\"computedDisparityMapTsukubaCPU.pgm\"", "\"computedDisparityConesQuarterCPU.pgm\"", "\"computedDisparityConesHalfCPU.pgm\""]
	#numPossDispVals = ["16", "63", "90"]
	#scaleBp = ["16.0f", "4.0f", "2.0f"]
	#groundTruthDisp = ["\"groundTruthDispTsukuba.pgm\"", "\"conesQuarterGroundTruth.pgm\"", "\"conesHalfGroundTruth.pgm\""]
	#groundTruthDispScale = ["16.0f", "4.0f", "2.0f"]
	
	#uncomment if using multiple disparity values on single image	
	#numDispVals = ["15", "16", "17", "18"]	
	numBpLevelsAndIters = [{"bpLevels" : 1, "bpIters" : 6}, {"bpLevels" : 1, "bpIters" : 10}, {"bpLevels" : 1, "bpIters" : 25}, {"bpLevels" : 1, "bpIters" : 50}, {"bpLevels" : 1, "bpIters" : 100}, {"bpLevels" : 1, "bpIters" : 250}, {"bpLevels" : 1, "bpIters" : 500}, {"bpLevels" : 1, "bpIters" : 1000}, {"bpLevels" : 2, "bpIters" : 6}, {"bpLevels" : 2, "bpIters" : 10}, {"bpLevels" : 2, "bpIters" : 25}, {"bpLevels" : 2, "bpIters" : 50}, {"bpLevels" : 3, "bpIters" : 6}, {"bpLevels" : 3, "bpIters" : 10}, {"bpLevels" : 3, "bpIters" : 25}, {"bpLevels" : 3, "bpIters" : 50}, {"bpLevels" : 4, "bpIters" : 6}, {"bpLevels" : 4, "bpIters" : 10}, {"bpLevels" : 4, "bpIters" : 25}, {"bpLevels" : 4, "bpIters" : 50}, {"bpLevels" : 5, "bpIters" : 6}, {"bpLevels" : 5, "bpIters" : 10}, {"bpLevels" : 5, "bpIters" : 25}, {"bpLevels" : 6, "bpIters" : 6}, {"bpLevels" : 6, "bpIters" : 10}, {"bpLevels" : 6, "bpIters" : 25}, {"bpLevels" : 7, "bpIters" : 6}, {"bpLevels" : 7, "bpIters" : 10}, {"bpLevels" : 7, "bpIters" : 25}] 
	truncationDiscontCost = ["2.0f"]
	truncationDataCost = ["20.0f"]
	dataCostWeight = ["0.1f"]
	smoothImagesSigma = ["0.7f"]
	fileOutput = open("outputPython.txt", "w")
	currTime = time.time()
	fileOutputCsv = open("outputPythonTestManyImageSets2" + str(currTime) + ".csv", "w")
	outputLabels = []
	outputData = []
	firstLine = True
	for imageSet in imageSets:
		for currNumBpLevelsAndIters in numBpLevelsAndIters:
			for currTruncationDiscontCost in truncationDiscontCost:
				for currTruncationDataCost in truncationDataCost:
					for currDataCostWeight in dataCostWeight:
						for currSmoothImagesSigma in smoothImagesSigma:
							#uncomment if using multiple disparity values on single image	
							#for currNumDispVals in numDispVals:
								numDispLevels = imageSet["NumDispVals"]
								currTruncationDiscontCost = float(numDispLevels) / 7.5
								file = open("bpParametersFromPython.h", "w")
								file.write("#ifndef BP_STEREO_FROM_PYTHON_H\n")
								file.write("#define BP_STEREO_FROM_PYTHON_H\n")
								file.write("#define REF_IMAGE_FROM_PYTHON %s\n" % imageSet["RefImage"])
								file.write("#define TEST_IMAGE_FROM_PYTHON %s\n" % imageSet["TestImage"])
								file.write("#define SAVE_DISPARITY_IMAGE_PATH_GPU_FROM_PYTHON %s\n" % imageSet["CompGpuDispMap"])
								file.write("#define SAVE_DISPARITY_IMAGE_PATH_CPU_FROM_PYTHON %s\n" % imageSet["CompCpuDispMap"])
								file.write("#define SCALE_BP_FROM_PYTHON %s\n" % imageSet["ScaleBp"])
								file.write("#define DEFAULT_GROUND_TRUTH_DISPARITY_FILE_FROM_PYTHON %s\n" % imageSet["GroundTruthDisp"])
								file.write("#define DEFAULT_GROUND_TRUTH_DISPARITY_SCALE_FROM_PYTHON %s\n" % imageSet["GroundTruthDispScale"])
								#uncomment if using multiple disparity values on single image	
								#file.write("#define NUM_POSSIBLE_DISPARITY_VALUES_FROM_PYTHON %s\n" % currNumDispVals)
								file.write("#define NUM_POSSIBLE_DISPARITY_VALUES_FROM_PYTHON %s\n" % imageSet["NumDispVals"])
								file.write("#define ITER_BP_FROM_PYTHON %s\n" % currNumBpLevelsAndIters["bpIters"])
								file.write("#define LEVELS_BP_FROM_PYTHON %s\n" % currNumBpLevelsAndIters["bpLevels"])
								file.write("#define DISC_K_BP_FROM_PYTHON %s\n" % currTruncationDiscontCost)
								file.write("#define DATA_K_BP_FROM_PYTHON %s\n" % currTruncationDataCost)
								file.write("#define LAMBDA_BP_FROM_PYTHON %s\n" % currDataCostWeight)
								file.write("#define SIGMA_BP_FROM_PYTHON %s\n" % currSmoothImagesSigma)
								file.write("#endif")
								file.close()
	
								os.system("make clean")
								os.system("make")
								os.system("./driverCudaBp")
 	
								file = open("output.txt", "r") 
								numLabel = 0
								for line in file:
									lineSplit = line.split(":")
									if (len(lineSplit) > 0):
										if (firstLine):
											labelNoNewLine = lineSplit[0].replace("\n", "")
											outputLabels.append(labelNoNewLine)
											outputData.append([])
										if (len(lineSplit) > 1):
											dataNoNewLine = lineSplit[1].replace("\n", "")
											outputData[numLabel].append(dataNoNewLine)
										numLabel += 1			
									print(line)
									fileOutput.write(line)
				
								fileOutput.write("\n\n")
								firstLine = False

	for label in outputLabels:
		fileOutputCsv.write("%s," % label)
	fileOutputCsv.write("\n")
	#uncomment if using multiple disparity values on single image	
	#for i in range(len(imageSets)*len(numDispVals)*len(numBpIters)*len(numBpLevels)*len(truncationDiscontCost)*len(truncationDataCost)*len(dataCostWeight)*len(smoothImagesSigma)):
	for i in range(len(imageSets)*len(numBpLevelsAndIters)*len(truncationDiscontCost)*len(truncationDataCost)*len(dataCostWeight)*len(smoothImagesSigma)):
		for data in outputData:
			if (len(data) == 0):
				fileOutputCsv.write(",")
			else:
				fileOutputCsv.write("%s," % data[i])
		fileOutputCsv.write("\n")
	print outputLabels
	print outputData
	fileOutput.close()
	fileOutputCsv.close()
