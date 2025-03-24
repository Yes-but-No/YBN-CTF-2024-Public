
This is a basic ret2win challenge with a small twist, only accepting characters "yesbutnoYESBUTNO". As such, the cylic generator used has to be changed to use that charset. Other then that, it's a simple ret2win!

1. Find offset (using cyclic with a specific charset)
2. BOF with a ret, and then finally return again to win()

solve script [here](exp.py)
