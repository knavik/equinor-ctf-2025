## Challenge description
```
Flags are usually **strings** in files, matching the pattern "EPT{...}" where "..." is some text. 

Here's an executable that prints the flag for you. Can you find the flag?

(For security reasons, we encrypt the flag before printing)
```

## Solution
1. Download the file
2. Run strings on the file
`strings filechecker`
3. Look for the flag
```
/lib64/ld-linux-x86-64.so.2
puts
__libc_start_main
__cxa_finalize
printf
__isoc99_scanf
libc.so.6
GLIBC_2.7
GLIBC_2.2.5
GLIBC_2.34
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
<@~i
<yu8H
EPT{FOOLEDYOUONCELOL}
Would you like to print the flag? [y/n]
Here it is, encrypted for your safety: %s
Ok, nevermind then...
;*3$"
GCC: (Debian 14.2.0-19) 14.2.0
Scrt1.o
__abi_tag
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.0
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
flagprinter.c
__FRAME_END__
_DYNAMIC
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_start_main@GLIBC_2.34
_ITM_deregisterTMCloneTable
encode
puts@GLIBC_2.2.5
_edata
_fini
printf@GLIBC_2.2.5
__data_start
__gmon_start__
__dso_handle
FLAG
_IO_stdin_used
_end
__bss_start
main
__isoc99_scanf@GLIBC_2.7
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@GLIBC_2.2.5
_init
.symtab
.strtab
.shstrtab
.note.gnu.property
.note.gnu.build-id
.interp
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.note.ABI-tag
.init_array
.fini_array
.dynamic
.got.plt
.data
.bss
.comment
```

**Flag:** `EPT{FOOLEDYOUONCELOL}`