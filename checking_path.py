import os

path = "C:\Program Files (x86)\AnyDesk\AnyDesk.exe"

# Check if path exists
os.access(path, os.F_OK)
# Check if path is Readable
os.access(path, os.R_OK)
# Check if path is Writable
os.access(path, os.W_OK)
# Check if path is Executable
os.access(path, os.X_OK)

# also it's possible to perform all checks together
os.access(path, os.F_OK & os.R_OK & os.W_OK & os.X_OK)  # True
# All the above returns True if access is allowed and False if not allowed.
# These are available on unix and windows.

