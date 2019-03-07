from client import arguments_validation
from client.client_handler import *

if __name__ == "__main__":
    args = arguments_validation.init_args()
    client = Client()
    client.run(args.ip, args.port, args.login, args.password)
