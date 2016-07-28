#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;

int main( int argc, char **argv ) {
	char* imageName = argv[1];

	Mat image;
	image = imread( imageName, 1);
	if( argc !=2 || !image.data ){
		fprintf(stderr, "No image data \n");
		return -1;
	}

	Mat gray_image;
	cvtColor( image, gray_image, CV_BGR2GRAY );

	imwrite( "/home/asim/Picture/opencv/small-cat-gray.jpg", gray_image );
	namedWindow( imageName, CV_WINDOW_AUTOSIZE );
	namedWindow( "Gray Image", CV_WINDOW_AUTOSIZE );
	imshow( imageName, image );
	imshow( "Gray Image", gray_image );

	waitKey(0);
	return 0;
}
