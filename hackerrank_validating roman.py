regex_pattern = r"^(?!.*?([IVXCM])\1{3}|LL|DD)[IVXCMLD]+$"
import re
print(str(bool(re.match(regex_pattern, input()))))