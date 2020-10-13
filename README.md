# symbol_checker
Reads in a library and an executable (or another library, or a directory) and displays which symbols from the first library are used

```
/symbol_checker.py ./libsp_4.a NEMS.exe

Symbols provided by './libsp_4.a' that are used by 'NEMS.exe':
    _radb5_  from  fftpack.F.o
    _radf3_  from  fftpack.F.o
    _rfftf1_  from  fftpack.F.o
    _rfftb1_  from  fftpack.F.o
    _rfftb_  from  fftpack.F.o
    _splat_  from  splat.F.o
    _rffti1_  from  fftpack.F.o
    _ludcmp_  from  lapack_gen.F.o
    _lubksb_  from  lapack_gen.F.o
    _srcft_  from  fftpack.F.o
    _scrft_  from  fftpack.F.o
    _radb2_  from  fftpack.F.o
    _radf2_  from  fftpack.F.o
    _drcft_  from  fftpack.F.o
    _scfft_  from  fftpack.F.o
    _radfg_  from  fftpack.F.o
    _radf4_  from  fftpack.F.o
    _radb3_  from  fftpack.F.o
    _dcrft_  from  fftpack.F.o
    _radf5_  from  fftpack.F.o
    _radbg_  from  fftpack.F.o
    _radb4_  from  fftpack.F.o
    _csfft_  from  fftpack.F.o
    _rfftf_  from  fftpack.F.o
    _rffti_  from  fftpack.F.o 
   ```
