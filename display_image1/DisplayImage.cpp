#include <stdio.h>
#include <opencv2/opencv.hpp>

using namespace cv;

int main( int argc, char** argv ) {
	if ( argc !=2 ) {
		fprintf(stderr, "Not enough args. Usage: DisplayImage.out /path/to/image\n");
		return -1;
	}
	Mat image;
	image = imread( argv[1], 1 );
	if ( !image.data ) {
		fprintf(stderr, "No image data \n" );
		return -1;
	}
	namedWindow("Display Image", WINDOW_AUTOSIZE );
	imshow("Display Image", image);

	waitKey(0);
	
	return 0;
}

