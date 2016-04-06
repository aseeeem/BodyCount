#include <opencv2/opencv.hpp>
#include <iostream>
#include <highgui.h>
#include <cv.h>

using namespace cv;

double alpha;
int beta;

int main( int argc, char **argv ) {
	Mat image = imread( argv[1] );
	
	if( argc != 2 ) {
		std::cout << "Usage is [./executable filename]" << std::endl;
	}

	Mat new_image = Mat::zeros( image.size(), image.type() );

	std::cout << "Enter the alpha value [1.0 - 3.0]: ";
	std::cin >> alpha;
	std::cout << "Enter the beta value [0 - 100]: ";
	std::cin >> beta;
	for( int y = 0; y < image.rows; y++ ) {
		for( int x = 0; x < image.cols; x++ ) {
			for( int c = 0; c < 3; c++ ) {
				new_image.at<Vec3b>(y,x)[c] = saturate_cast<uchar>( alpha*( image.at<Vec3b>(y,x)[c] ) + beta );
			}
		}
	}
	namedWindow( "Original Image", 1 );
	namedWindow( "New Image", 1 );

	imshow( "Original Image", image );
	imshow( "New Image", new_image );

	waitKey();
	return 0;
}
