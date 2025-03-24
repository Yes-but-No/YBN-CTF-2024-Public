#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <time.h>

/* Taken from Wikipedia! */
#define ROTL(a,b) (((a) << (b)) | ((a) >> (32 - (b))))
#define QR(a, b, c, d)(  \
        b ^= ROTL(a + d, 7), \
        c ^= ROTL(b + a, 9), \
        d ^= ROTL(c + b,13), \
        a ^= ROTL(d + c,18))
#define ROUNDS 20

void salsa20_block(uint32_t out[16], uint32_t const in[16])
{
    int i;
    uint32_t x[16];

    for (i = 0; i < 16; ++i)
        x[i] = in[i];
    // 10 loops × 2 rounds/loop = 20 rounds
    for (i = 0; i < ROUNDS; i += 2) {
        // Odd round
        QR(x[ 0], x[ 4], x[ 8], x[12]); // column 1
        QR(x[ 5], x[ 9], x[13], x[ 1]); // column 2
        QR(x[10], x[14], x[ 2], x[ 6]); // column 3
        QR(x[15], x[ 3], x[ 7], x[11]); // column 4
                                        // Even round
        QR(x[ 0], x[ 1], x[ 2], x[ 3]); // row 1
        QR(x[ 5], x[ 6], x[ 7], x[ 4]); // row 2
        QR(x[10], x[11], x[ 8], x[ 9]); // row 3
        QR(x[15], x[12], x[13], x[14]); // row 4
    }
    for (i = 0; i < 16; ++i)
        out[i] = x[i] + in[i];
}
/* Taken from Wikipedia! */

uint32_t xorshift32(uint32_t x) {
    x ^= x << 13;
    x ^= x >> 17;
    x ^= x << 5;
    return x;
}

int main() {
    char flag[] = "YBN24{w3_g01ng_4t_88_m1l3s_p3r_h0ur_away_n_away,_h1p_h1p_h00r4y!_fd4eacc3e919e7}";
    //char flag[] = "ybn";
    printf("%lu\n", sizeof(flag));
    // one more then middle
    uint32_t mid = (UINT32_MAX >> 1) + 1;
    time_t tseed = time(NULL);
    uint32_t seed = tseed; //honestly I dont think this is needed LOL

    // xxd -ps -l 16 /dev/random #4 times
    uint32_t randomstaticval[16] = {
        0xde977e9c, 0xa7012a8f, 0x3fb3fd00, 0xf3a595f5,
        0x73d3db37, 0x68f50294, 0xfd8bbfab, 0x71f44229,
        0x4ae147db, 0xb736d257, 0xef5e9925, 0xd010833c,
        0x0c651db0, 0x639bf0e9, 0xe6953fb8, 0x9e974454,
    };
    uint32_t out[16];
    uint32_t encrypted_flag[sizeof(flag)];
    uint32_t encrypted_flag_offset[sizeof(flag)];

    for(size_t i = 0; i < strlen(flag); i++) {
        salsa20_block(out, randomstaticval);
        memcpy(randomstaticval, out, sizeof(out));
        puts("salsa20_block");
        uint32_t offset = mid + ((out[0] - 3) % mid);
        encrypted_flag[i] = xorshift32(flag[i]);
        for(size_t j = 1; j < offset; j++) {
            encrypted_flag[i] = xorshift32(encrypted_flag[i]);
        }
        encrypted_flag_offset[i] = offset;
    }
    time_t end = time(NULL);
    uint32_t diff_time =  end - tseed;
    printf("Time taken: %dh %dm %ds\n", ((diff_time/60)/60), (diff_time/60) % 60, (diff_time % 60));

    printf("uint32_t enc_flag[] = {");
    for(size_t i = 0; i < sizeof(flag); i++) {
        printf("%u, ", encrypted_flag[i]);
    }
    printf("};\n");
    printf("uint32_t enc_flag_rounds[] = {");
    for(size_t i = 0; i < sizeof(flag); i++) {
        printf("%u, ", encrypted_flag_offset[i]);
    }
    printf("};\n");

    return 0;
}
