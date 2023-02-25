#include <iostream>
#include "pointmatcher/PointMatcher.h"
#include <cassert>
#include "boost/filesystem.hpp"

int main(int argc, char *argv[]){
	std::cout << "Hello World" << std::endl;

	typedef PointMatcher<float> PM;
	typedef PM::DataPoints DP;
	

	const DP ref(DP::load(argv[1]));
	const DP data(DP::load(argv[2]));

	PM::ICP icp;
	icp.setDefault();
	PM::TransformationParameters T = icp(data, ref);

	DP data_out(data);
	icp.transformations.apply(data_out, T);

	ref.save("test_ref.vtk");
	data.save("test_data_in.vtk");
	data_out.save("test_data_out.vtk");
	std::cout << "Final transformation:" << std::endl << T << std::endl;

	return 0;
}