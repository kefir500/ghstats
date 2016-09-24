import ghstats
import sys

try:
    ghstats.main_cli(sys.argv[1:])
except KeyboardInterrupt:
    pass
