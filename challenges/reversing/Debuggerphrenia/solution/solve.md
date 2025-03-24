# Debuggerphrenia

## Summary
- Description: The debuggers... they're everywhere! Under my skin, even!

## Static Analysis
1. Put the binary into Ghidra (I've left some stuff in there that makes IDA tweak out and generate weird stuff :p ~~sorry if you tried this challenge and used IDA~~)
2. Locate main. One might notice that the binary is heavily obfuscated, but the following line gives us a clue as to what's happening: `ptrace(PTRACE_TRACEME,0,0);` We can infer with decent confidence that this has something to do with detecting debuggers.
3. We can also spot a recurring pattern with the giant `do` loops with a bunch of stuff going on. Seems to be an artifact from obfuscation, so we can ignore it. 
4. Searching around a little more, we find this function call `FUN_0010c460(&local_27e8,&LAB_0010f100,&LAB_0010f1a0);`, and following `LAB_0010f1a0` leads us to this piece of code:
```
        0010f1a0 b8 65 00        MOV        EAX,0x65
                 00 00
        0010f1a5 48 31 ff        XOR        RDI,RDI
        0010f1a8 48 31 f6        XOR        RSI,RSI
        0010f1ab 48 31 d2        XOR        RDX,RDX
        0010f1ae 4d 31 d2        XOR        R10,R10
        0010f1b1 0f 05           SYSCALL
        0010f1b3 48 83 f8 ff     CMP        RAX,-0x1
        0010f1b7 75 05           JNZ        LAB_0010f1be
        0010f1b9 e9 ec ff        JMP        LAB_7790f1aa
                 7f 77
                             LAB_0010f1be                                   
        0010f1be c3              RET
        0010f1bf 00              ??         00h
```
5. What this piece of code does is call `ptrace` on itself, and if it fails (debugger is present!) it'll jump to an invalid address and crash itself.
6. The code around is an unreadable mess, but with the shellcode spotted, we could infer that it's using this piece of code to stop you from getting the flag.
7. There's also an easier way to do this by running it in a debugger (ironic)

## Dynamic Analysis 
1. Put this into GDB
2. Let it run its course and crash
3. Use `x/10i $rip-25` to look at where it crashed and the previous few instructions.
4. You would see something like this:
```
gef➤  x/10i $rip-25
   0x7ffff7fc0000:      mov    eax,0x65
   0x7ffff7fc0005:      xor    rdi,rdi
   0x7ffff7fc0008:      xor    rsi,rsi
   0x7ffff7fc000b:      xor    rdx,rdx
   0x7ffff7fc000e:      xor    r10,r10
   0x7ffff7fc0011:      syscall
   0x7ffff7fc0013:      cmp    rax,0xffffffffffffffff
   0x7ffff7fc0017:      jne    0x7ffff7fc001e
=> 0x7ffff7fc0019:      jmp    0x80006f7c000a
   0x7ffff7fc001e:      ret
```
5. Notice that it's doing a `ptrace` syscall to check for a debugger, and jumping to a random place if it's being debugged. This aligns with the piece of code we found earlier.

## Solve
Here are some ways you could (and probably would?) try to solve this: 

### Patching the Shellcode
1. Should you go with the option of patching the code, you might notice that the output of the program is gibberish. Unfortunately, the flag depends on the shellcode to be successfully decrypted. By tampering with the code, the flag fails to correctly decrypt.

### Making ptrace return success
1. All I did was ask ChatGPT to write me a program to intercept `ptrace` syscalls and have them always return success :D