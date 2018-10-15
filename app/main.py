# Copyright 2016 Google Inc.
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

import logging

from flask import Flask
from jinja2 import Environment, PackageLoader

env = Environment(
    loader=PackageLoader('main', 'templates'),
    autoescape=True
)

app = Flask(__name__)


@app.route('/')
def index():
    template = env.get_template('index.html')
    return template.render()


@app.route('/about')
def about():
    template = env.get_template('about.html')
    return template.render()


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
