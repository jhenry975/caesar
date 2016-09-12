#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
import webapp2
from caesar import encrypt
import cgi
#from caesar import alphabet_position

form="""
<form method="post">
    <div>
        <label> Rotate by:
            <input type="char" name="rot">
        </label>
    </div>
    <br>
    <textarea type="letter" name="textbox">
    </textarea>
    <br>
    <br>
    <input type="submit">
    </input>
</form>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(form)

    def post(self):

        rotateBy = self.request.get("rot")
        text = self.request.get("textbox")

        # position = alphabet_position

        text = cgi.escape(text)
        rotateBy = int(rotateBy)
        text = str(text)
        encrypt_text = encrypt(text, rotateBy)



        self.response.out.write(encrypt_text)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
