import ida_funcs, Heads, idaapi, ida_idp, get_operand_value, print_insn_mnem

addr = 0x088B6A 
x = int.from_bytes(b"yesbutno", "big")
print_flag = 0x185F2F
insn = idaapi.insn_t()

while addr != print_flag:
    f = ida_funcs.get_func(addr)
    # note you might need to undefine and redefine some misplaced functions for this to work
    # (eg. the disassembly might do `call sub_1248 + 1` in one of the functions, you'll need to change it to `call sub_1249`)
    # print(hex(addr))
    ptr, y = 0, 0
    for ea in Heads(f.start_ea, f.end_ea):
        length = idaapi.decode_insn(insn, ea)
        if y:
            mnem = print_insn_mnem(ea)
            if mnem == "add":
                x = (x+y) % 2**64
            elif mnem == "xor":
                x ^= y
            else:
                x = (x*y) % 2**64
            y = 0
        if length == 10:
            y = get_operand_value(ea, 1)
        if ida_idp.is_call_insn(insn):
            ptr += 1
        if ptr == 4:
            break
    addr = get_operand_value(ea, 0)

print("flag: ", end="")
ct = [0xE7BAFE26410C70D7, 0x34E684DB45D0F19D, 0xC509D7D70532D3F1, 0x38B138414733224C, 0x600F6A36F068DE0B, 0xC70EC0297516AF32, 0x37977F6DB2DF31F1]
for i in ct:
    i = (i*x) % 2**64
    while i:
        print(chr(i % 256),end="")
        i //= 256

# flag: YBN24{y3s_bUt_No_w4!t_actU4lly_ye5_buTt_n0_mAYb3_yEs}