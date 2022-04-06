#
# pulp_nn_init.py
# Nazareno Bruschi <nazareno.bruschi@unibo.it>
#
# Copyright (C) 2019-2020 University of Bologna
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

PULPNNDataPrecisions = [8, 4, 2]
PULPNNWeightsPrecisions = [8, 4, 2]
PULPNNQuantizationMethods = ['shift_clip'] #,'thresholds']
BN_ACTIVATIONS = ['32bit', '64bit']
CORE_EXTENTIONS = ['XpulpV2', 'XpulpNN', 'XpulpNN-mixed']
MATMUL_FORMAT = ['4x2', '4x4']
PULPNNAPI = ""
PULPNNMAKE = ""
PULPNNINCLUDE = ""
PULPNNCALL = ""
PULPNNGOLDEN = ""