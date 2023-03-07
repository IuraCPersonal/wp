from app.go2web import Go2Web
from app.parser import CLIParser

arg, msg = CLIParser.take_input()

Go2Web.start(arg, msg)
