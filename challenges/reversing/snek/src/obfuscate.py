from dis import dis, opmap
from marshal import dumps, loads
from types import CodeType

old_to_new_opcodes = {
    opmap["MAKE_FUNCTION"]: 201,
    opmap["STORE_NAME"]: 223,
    opmap["RETURN_VALUE"]: 204,
    opmap["STORE_FAST"]: 209,
    opmap["LOAD_FAST"]: 233,
    opmap["BINARY_MULTIPLY"]: 214,
    opmap["BINARY_ADD"]: 217,
    # opmap["LOAD_METHOD"]: 221,
    # opmap["LOAD_GLOBAL"]: 206,
    opmap["CALL_FUNCTION"]: 203,
    # opmap["GET_ITER"]: 222,
    # opmap["CALL_METHOD"]: 238,
    # opmap["BUILD_LIST"]: 211,
    # opmap["FOR_ITER"]: 202,
    # opmap["UNPACK_SEQUENCE"]: 231,
    # opmap["BINARY_XOR"]: 210,
    # opmap["LIST_APPEND"]: 226,
    # opmap["JUMP_ABSOLUTE"]: 228,
}

with open("enc.cpython-310.pyc", "rb") as f:
    header = f.read(16)
    code = loads(f.read())

print(code)

dis(code)


enc_co = code.co_consts[0]

listcomp = enc_co.co_consts[-2]


def replace_opcodes(co: CodeType) -> CodeType:
    code = co.co_code
    # new_code = [0] * len(code)
    # for i, op in enumerate(code):
    #     if i % 2 == 0:
    #         if op in old_to_new_opcodes:
    #             new_code[i] = old_to_new_opcodes[op]
    #     else:
    #         new_code[i] = op

    new_code = []
    for op, arg in zip(code[::2], code[1::2]):
        if op in old_to_new_opcodes:
            new_code.append(old_to_new_opcodes[op])
        else:
            new_code.append(op)
        new_code.append(arg)

    dis(bytes(new_code))
    return co.replace(co_code=bytes(new_code))


new_listcomp = replace_opcodes(listcomp)

new_enc_co = replace_opcodes(enc_co)
new_enc_co = new_enc_co.replace(
    co_consts=(*enc_co.co_consts[:-2], new_listcomp, enc_co.co_consts[-1])
)

new_code = replace_opcodes(code)
new_code = new_code.replace(co_consts=(new_enc_co, *code.co_consts[1:]))

with open("enc.pyc", "wb") as f:
    f.write(header)
    f.write(dumps(new_code))
