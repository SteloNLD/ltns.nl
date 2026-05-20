#!/usr/bin/env bash
set -e

python ci/preprocess.py hugo
python ci/preprocess.py zola
python ci/preprocess.py quartz

(cd hugo && hugo server --bind 0.0.0.0) &
(cd zola && zola serve --interface 0.0.0.0) &
(cd quartz && npm install --silent && npx quartz build --serve) &
