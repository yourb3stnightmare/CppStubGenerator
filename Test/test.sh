#!/bin/bash
python ../CppStubGen.py Test1.h
# TODO For now, just do binary comparisons. 
# In the future, write some unit tests for the output file.
if [[ $(cmp Test1_Stub.cpp ExpectedOutput/Test1_Stub.cpp) -eq 0 ]]; then echo "Test1_Stub.cpp matches expected"; else echo "Test1_Stub.cpp does not match expected"; fi
if [[ $(cmp Test1_Stub.h ExpectedOutput/Test1_Stub.h) -eq 0 ]]; then echo "Test1_Stub.h matches expected"; else echo "Test1_Stub.h does not match expected"; fi
