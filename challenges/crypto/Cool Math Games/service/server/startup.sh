#!/bin/bash

seed=$RANDOM
export seed # Credits to Jabriel for the idea
export FLAG="YBN24{wH0_kN0w5_8a5H_R4nD0m_w4sn7_s0_rAnD0m_4ft3r_4ll}"
socat -dd TCP-LISTEN:1337,fork,reuseaddr EXEC:"python server.py"