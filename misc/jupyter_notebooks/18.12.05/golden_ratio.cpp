#include <chrono>
#include <iostream>

using namespace std;
using namespace std::chrono;

double golden_ratio(size_t n){
	double s = 1.;
	for (size_t i = 0; i < n; i++) {
		s = 1. + 1. / s;
	}
	return s;
}

int main(){
    const size_t n = 100000;
	const size_t repeat = 1000;
	double phi;
	const auto t1 = high_resolution_clock::now();
	for (size_t i = 0; i < repeat; i++) {
		phi = golden_ratio(n);
	}
	const auto t2 = high_resolution_clock::now();
	const auto duration = duration_cast<microseconds>(t2 - t1).count();
    cout << duration / repeat << endl;
	cout << phi << endl;
    return 0;
}