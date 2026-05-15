#!/usr/bin/env bash
set -e

python ci/preprocess.py hugo
python ci/preprocess.py zola

(cd hugo && hugo server --bind 0.0.0.0) &
(cd zola && zola serve --interface 0.0.0.0) &
