import os
import tempfile
import argparse
import json

# parser = argparse.ArgumentParser()
# parser.add_argument("--key")
# parser.add_argument("--val")
# args = parser.parse_args()
# if args.key:
#     pass
#     # print ("YEP it's a KEY {}, and a value {}".format(args.key, args.val))

# a = json.dumps({args.key: args.val})

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
with open(storage_path, 'r+') as f:
    # pass
    # f.write(a + '\n')
    b = f.readlines()
    n = 0
    for i in range (len(b)):
        print (b[i], 'this is {} line'.format(n))
        print ('####')
        n += 1



# if args.key in a:
#      print (a.key)

