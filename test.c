#ifndef __unix
__declspec(dllexport)
#endif
int sum(int a, int b) {
    return a + b;
}
