#
#   Processes commands of the syntax /<command>
#

import server

def parse(cmdlist, response):

    print("Parsing command")

    cmd = cmdlist[0]

    if cmd == "start":
        response.set_text("PADORU PADORU")
        response.send()

    elif cmd == "goodbot":
        response.set_text(":^)")
        response.send()

    elif cmd == "badbot":
        response.set_text(":'(")
        response.send()
