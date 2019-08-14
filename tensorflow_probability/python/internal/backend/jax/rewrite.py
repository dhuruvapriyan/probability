# Copyright 2019 The TensorFlow Probability Authors.
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
# ============================================================================
"""Rewrite script for NP->JAX."""

from __future__ import absolute_import
from __future__ import division
# [internal] enable type annotations
from __future__ import print_function

import re

from absl import app


def main(argv):
  contents = open(argv[1]).read()
  contents = contents.replace(
      "tensorflow_probability.python.internal.backend.numpy",
      "tensorflow_probability.python.internal.backend.jax")
  contents = contents.replace(
      "from tensorflow_probability.python.internal.backend import numpy",
      "from tensorflow_probability.python.internal.backend import jax")
  contents = contents.replace("scipy.linalg", "jax.scipy.linalg")
  contents = contents.replace("scipy.special", "jax.scipy.special")
  contents = contents.replace(
      "SKIP_JAX_DISABLED = False",
      "SKIP_JAX_DISABLED = True\n"
      "from jax.config import config; config.update('jax_enable_x64', True)")
  contents = re.sub("^import numpy", "import jax.numpy", contents)
  print(contents)


if __name__ == "__main__":
  app.run(main)