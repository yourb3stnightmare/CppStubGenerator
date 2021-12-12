#!/usr/bin/env python
#
# This is a modified version of the stub generator (gmock_gen.py) provided with 
# Google Test. This version is intended to generate c++ mock files of the
# functions/classes/methods defined in a given header file. This script will 
# generate a mock version of each function/method defined in a header file, 
# with global data to allow the user to set the return value, output parameters, 
# and to check the perform analysis on the data passed to all of the given 
# functions/methods.
#
# Copyright 2008 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Driver for starting up Google Mock class generator."""

# Note: Original Google author, do not contact the original author with issues
# found in this modified copy of the scripts.
__author__ = 'nnorwitz@google.com (Neal Norwitz)'

import os
import sys

if __name__ == '__main__':
  # Add the directory of this script to the path so we can import gmock_class.
  sys.path.append(os.path.dirname(__file__))

  from cpp import CppStubGenerator
  # Fix the docstring in case they require the usage.
  CppStubGenerator.__doc__ = CppStubGenerator.__doc__.replace('CppStubGenerator.py', __file__)
  CppStubGenerator.main()
