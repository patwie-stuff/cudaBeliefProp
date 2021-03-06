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

//Header for the kernal to apply a horizontal/vertical filter to image data

#ifndef KERNAL_FILTER_HEADER_CUH
#define KERNAL_FILTER_HEADER_CUH


//the filter and the size of the filter is held in constant memory as it is accessed by all threads at the same time,
//making it as fast as a register if in cache
__device__ __constant__ float imageFilterConst[MAX_SIZE_FILTER];
__device__ __constant__ int sizeFilterConst;
__device__ __constant__ int widthImageConstFilt;
__device__ __constant__ int heightImageConstFilt;

// declare texture reference for 1D float texture
texture<float, 1, cudaReadModeElementType> imagePixelsFloatToFilterTexture;
texture<unsigned int, 1, cudaReadModeElementType> imagePixelsUnsignedIntToFilterTexture;

//checks if the current point is within the image bounds
__device__ bool withinImageBoundsFilter(int xVal, int yVal, int width, int height);

//kernal to convert the unsigned int pixels to float pixels in an image when
//smoothing is not desired but the pixels need to be converted to floats
//the input image is stored as unsigned ints in the texture imagePixelsUnsignedIntToFilterTexture
//output filtered image stored in floatImagePixels
__global__ void convertUnsignedIntImageToFloat(float* floatImagePixels);

//kernal to apply a horizontal filter on each pixel of the image in parallel
//input image stored in texture imagePixelsFloatToFilterTexture
//output filtered image stored in filteredImagePixels
__global__ void filterFloatImageAcross(float* filteredImagePixels);


//kernal to apply a vertical filter on each pixel of the image in parallel
//input image stored in texture imagePixelsFloatToFilterTexture
//output filtered image stored in filteredImagePixels
__global__ void filterFloatImageVertical(float* filteredImagePixels);

//kernal to apply a horizontal filter on each pixel of the image in parallel
//the input image is stored as unsigned ints in the texture imagePixelsUnsignedIntToFilterTexture
//the output filtered image is returned as an array of floats
__global__ void filterUnsignedIntImageAcross(float* filteredImagePixels);


//kernal to apply a vertical filter on each pixel of the image in parallel
//the input image is stored as unsigned ints in the texture imagePixelsUnsignedIntToFilterTexture
//the output filtered image is returned as an array of floats
__global__ void filterUnsignedIntImageVertical(float* filteredImagePixels);


#endif //KERNAL_FILTER_HEADER_CUH
