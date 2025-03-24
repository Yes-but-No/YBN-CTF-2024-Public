#!/bin/bash

sudo apt install socat -y
sudo apt install python3 -y

seed=$RANDOM
export seed # Credits to Jabriel for the idea
export FLAG="YBN24{this_is_a_fake_flag}"

pip install -r requirements.txt
socat -dd TCP-LISTEN:1337,fork,reuseaddr EXEC:"python server.py"