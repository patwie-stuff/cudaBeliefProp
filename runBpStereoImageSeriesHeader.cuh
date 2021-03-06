/*
Copyright (C) 2009 Scott Grauer-Gray, Chandra Kambhamettu, and Kannappan Palaniappan

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307 USA
*/

//Declares the methods to run Stereo BP on a series of images

#ifndef RUN_BP_STEREO_IMAGE_SERIES_HEADER_CUH
#define RUN_BP_STEREO_IMAGE_SERIES_HEADER_CUH

#include "bpStereoCudaParameters.cuh"

float averageRunTimeGpuNotIncludingMemoryTransfer = 0.0;
float averageRunTimeGpuIncludingMemoryTransfer = 0.0;

//run the disparity map estimation BP on a series of stereo images and save the results between each set of images if desired
void runStereoEstOnImageSeries(const char* imageFiles[], int numImages, unsigned int& widthImages, unsigned int& heightImages, BPsettings algSettings, bool saveResults, const char* saveDisparityMapImagePaths[], FILE* resultsFile);

#endif //RUN_BP_STEREO_IMAGE_SERIES_HEADER_CUH
