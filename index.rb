require 'ffi'

module Check
  extend FFI::Library

  ffi_lib './main.dll'

  attach_function :CallFn, [], :void
end

print "lib.CallFn() = ", Check.CallFn(), "\n"
