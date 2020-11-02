#include <iostream>
#include <chrono>


using namespace std;
using namespace std::chrono;

double golden_ratio(size_t n) {
    double s = 1.0;
    for (size_t i = 0; i < n; i++){
        s = 1.0 + 1.0 / s;
    }
    return s;
}

int main() {
    const size_t n = 1000000;
    const size_t repeat = 1000;
    double phi;
    const auto t1 = high_resolution_clock::now();
    for (size_t i = 0; i < repeat; i++) {
        phi = golden_ratio(n);
    }
    const auto t2 = high_resolution_clock::now();
    const auto dt = duration_cast<microseconds>(t2 - t1).count();
    cout << phi << endl;
    cout << static_cast<double>(dt) / repeat << endl;
    
    return 0;
}