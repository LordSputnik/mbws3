import sadisplay
from ws import schema

desc = sadisplay.describe([getattr(schema, attr) for attr in dir(schema)])
open('schema.dot', 'w').write(sadisplay.dot(desc))
