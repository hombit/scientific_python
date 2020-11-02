#include <random>


int autoreg(double a, size_t n, double* result) {
    std::random_device rd;
    std::minstd_rand gen(rd());
    std::normal_distribution<> d(0, 1);
    
    result[0] = d(gen);
    
    for (size_t i = 1; i < n; i++) {
        result[i] = a * result[i - 1] + d(gen);
    }
    return 0;
}