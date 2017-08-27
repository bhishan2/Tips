#!/bin/bash

# Usage: bash notify.sh hello this is a test.
# Usage: sleep 1; bash notify.sh Slow command finished
/usr/bin/osascript -e "display notification \"$*\""
