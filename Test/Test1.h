// Functions
void Func1();
void Func2(int val);
bool Func2(const char* str);
int Func3(int& outParam);

// Methods
class TestClass {
public:
    TestClass();
    ~TestClass();

    void Method1();
    bool Method2(const char* inPtr, char* outPtr, const int& inRef, short& outRef);
};
