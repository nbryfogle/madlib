#
#  Madlib Generator - example
#    model website to mimic: https://kids.wclibrary.info/do/madlibs/robot/
#    sample madlib generator site: http://www.redkid.net/madlibs/
#  
#  CONSIDER: separate word entry (Post) and story display (Get)
#            not both on same template ... 
#.           use html variables {{ }} for substitution

from flask import Flask, render_template
from flask import request

app = Flask(__name__)

madlib_key = {
    "nounA": "noun",
    "nameA": "name",
    "adjective1": "adjective",
    "verb1": "verb ending in -ing",
    "verb2": "verb",
    "noun1": "noun",
    "nounD": "noun",
    "verb3": "past tense verb",
    "verbA": "verb",
    "verbAIng": "same verb ending in -ing",
    "nounB": "noun",
    "noun2": "proper noun or name",
    "noun3": "noun",
    "nounC": "noun",
    "nounE": "noun",
    "nounF": "noun",
    "number": "number",
    "verb4": "past tense verb",
    "noun4": "noun",
    "adverb1": "adverb",
    "verb5": "past tense verb",
    "noun5": "noun",
    "adjective2": "adjective",
    "adverb2": "adverb",
    "noun6": "noun",
    "verb6": "verb",
    "nounF": "noun",
    "nounD": "noun"
}

# assign home route to function named index  
@app.route("/", methods=['GET', 'POST'])
def index():
  # get words entered in form, that are available as
  # URL arguments, with http GET, then reassign to variable,
  # set to default value if none entered
  
  ## print('request.args', request.args)
  # default value used when no arguments in URL
  key_copy = madlib_key.copy()
  
  i = False
  for req in request.args.items():
    key_copy[req[0]] = req[1] or madlib_key[req[0]]
    i = True
  
  template, story = open("madlib-text.txt").read().split("\n\n")
  template.format(**key_copy)

  return render_template("index.html", madlib=madlib_key, story=template if i else story)

# following must be last lines of flask app
if __name__ == "__main__":
  app.run()