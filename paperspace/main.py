import sys
import os

from .login import login, logout


def main():
    args = sys.argv[:]
    prog = os.path.basename(args.pop(0))

    if not args:
        usage(prog)

    cmd = args.pop(0)

    if cmd == 'login':
        email = None
        password = None
        apiToken = None
        while args:
            opt = args.pop(0)
            if opt == '--email':
                email = args.pop(0) if args else None
            elif opt == '--password':
                password = args.pop(0) if args else None
            elif opt == '--apiToken':
                apiToken = args.pop(0) if args else None
            elif not email:
                email = opt
            elif not password:
                password = opt
            elif not apiToken:
                apiToken = opt
        return not login(email, password, apiToken)

    if cmd == 'logout':
        return not logout()

    usage(prog)


def usage(prog):
    print('usage: %s login [[--email] <user@domain.com>] [[--password] <secretpw>] [[--apiToken] <api token name>]\n       %s logout' % (prog, prog))
    sys.exit(1)
