#include <stdint.h>

// lets just hope

int check_flag(char *str, uint32_t *strck, uint32_t *rounds) {
    uint32_t check = 0;
    uint32_t tmp;
    for(uint32_t i = 0; strck[i] != 0; i++) {
        tmp = str[i];
        for(uint32_t j = 0; j < rounds[i]; j++) {
            tmp ^= tmp << 13;
            tmp ^= tmp >> 17;
            tmp ^= tmp << 5;
        }
        //check |= tmp - strck[i];
        if(tmp != strck[i]) {
            return tmp - strck[i];
        }
    }
    return check;
}
