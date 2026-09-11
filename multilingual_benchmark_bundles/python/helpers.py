import argparse
parser = argparse.ArgumentParser()
parser.add_argument('name')
print(parser.parse_args().name)
