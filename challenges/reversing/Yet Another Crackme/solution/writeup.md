## Yet Another Crackme

1. Open the program in any disassembler of your choice. I'm using IDA Pro for this.
2. On disassembly, you would see that it calls login, and returns.
3. Analysing login, you can see a sequence of checks that are done before it branches to either a block that prints `can't crack me :p` or a block that calls a win function.
4. Set breakpoints on all the conditional jumps `ja/jz`  that branch into the lose block.
5. Run the program, input whatever (it's impossible to get the right password, the password is `how to get right password!?!?!?!?!` which is probably over 16 chars long but the input is truncated to 16)
6. On the `ja` instruction, set `CF (Carry Flag)` and `ZF (Zero Flag)` to zero. This will prevent the jump to the lose block from happening.
7. The next few conditional jumps are `jz` instructions. Set `ZF` to 1 to prevent the jump to the lose block.
8. The flag should be printed out.