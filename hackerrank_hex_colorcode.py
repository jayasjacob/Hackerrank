import re

if __name__ == "__main__":
    # reg = re.compile(r"(#[abcdefABCDEF1234567890]{3}|#[abcdefABCDEF1234567890]{6})")
    # reg = re.compile(r"#[abcdefABCDEF1234567890]{3,}")
    reg = re.compile(r"(:|,| +)(#[abcdefABCDEF1234567890]{3}|#[abcdefABCDEF1234567890]{6})\b")

    n = int(input())
    
    for i in range(n):
        line  = input()
        items = reg.findall(line)

        if items:
            # print(", ".join(str(s) for s in items ))
            # for match in items:
            #   print(items.group())
            for item in items:    
                print( item[1] )