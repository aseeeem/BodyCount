#include <stdio.h>
#include <opencv2/opencv.p>
#include <iostream>
#include <sstream>

using namespace std;
using namespace cv;

int main( int argc, char **argv ) {
	char* imageName = argv[1];
	image = imread( imageName, 1 );	
	if( argc != 2) {
		fprintf(stderr, "Not enough args!" );
	}
	if( !image.data ) {
		fprintf(stderr, "No image data!" );
	}

	Mat image;


return 0;
}
