section .text
    global main
main:
    mov eax, 1
    xor ebx, ebx
    int 0x80
