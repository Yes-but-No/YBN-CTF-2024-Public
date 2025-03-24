#include <stdio.h>
#include <stdint.h>

uint32_t lcg(uint32_t x) {
    return 134775813*x + 1;
}

int main() {
    char flag[] = "YBN24{n0th1ng_l1k3_s0m3_x0rs_t0_Ge7_r1d_Of_b0red0m...}";
    uint32_t seed = 0x1321de03;
    char buf[sizeof(flag)-1];
    printf("unsigned char xor_vals[] = { ");
    for(int i = 0; i < sizeof(flag)-1; i++) {
        seed = lcg(seed);
        printf("0x%02x, ", seed & 0xff);
        buf[i] ^= flag[i] ^ (seed & 0xff);
    }
    printf("};\n");
    printf("unsigned char flag[] = { ");
    for(int i = 0; i < sizeof(flag)-1; i++) {
        printf("0x%02x, ", (buf[i] & 0xff));
    }
    printf("};\n");
    return 0;
}
