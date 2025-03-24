from dis import dis, opmap
from marshal import dumps, loads  # noqa: F401
from types import CodeType

new_to_old_opcodes = {
    201: opmap["MAKE_FUNCTION"],
    223: opmap["STORE_NAME"],
    204: opmap["RETURN_VALUE"],
    209: opmap["STORE_FAST"],
    233: opmap["LOAD_FAST"],
    214: opmap["BINARY_MULTIPLY"],
    217: opmap["BINARY_ADD"],
    # 221: opmap["LOAD_METHOD"],
    # 206: opmap["LOAD_GLOBAL"],
    203: opmap["CALL_FUNCTION"],
    # 222: opmap["GET_ITER"],
    # 238: opmap["CALL_METHOD"],
    # 211: opmap["BUILD_LIST"],
    # 202: opmap["FOR_ITER"],
    # 231: opmap["UNPACK_SEQUENCE"],
    # 210: opmap["BINARY_XOR"],
    # 226: opmap["LIST_APPEND"],
    # 228: opmap["JUMP_ABSOLUTE"],
}

with open("../dist/enc.pyc", "rb") as f:
    header = f.read(16)
    code = loads(f.read())

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
        if op in new_to_old_opcodes:
            new_code.append(new_to_old_opcodes[op])
        else:
            new_code.append(op)
        new_code.append(arg)

    return co.replace(co_code=bytes(new_code))


new_listcomp = replace_opcodes(listcomp)

new_enc_co = replace_opcodes(enc_co)
new_enc_co = new_enc_co.replace(
    co_consts=(*enc_co.co_consts[:-2], new_listcomp, enc_co.co_consts[-1])
)

new_code = replace_opcodes(code)
new_code = new_code.replace(co_consts=(new_enc_co, *code.co_consts[1:]))

print(new_code)
dis(new_code)

with open("enc.gen.pyc", "wb") as f:
    f.write(header)
    f.write(dumps(new_code))
