def main():
    
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    
    #Check for punctuations
    punctuations = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' '
    ]
    for char in s:
        if char in punctuations:
            return False

    #6 chars max, 2 chars min
    if len(s) < 2 and len(s) > 6:
        return False
    
     #starts with 2 letters at least
    first_two_chars = s[0] + s[1]
    if not first_two_chars.isalpha():
        return False
    
    #Number not in middle of plate..can come at the end
    for i in range(len(s)):
        if (s[i].isdigit()):
            if not (s[i:].isdigit()):
                return False
                break

    return True

   


if __name__ == "__main__":
    main()
