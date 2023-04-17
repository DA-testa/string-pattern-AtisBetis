def read_input():
    mode = input()
    if mode == 'F':
        try:
            with open("./tests/06") as f:
                pattern, text = f.read().splitlines()
        except FileNotFoundError:
            print("Input file not found")
            return None, None

    elif mode == 'I':
        pattern = input().rstrip()
        text = input().rstrip()

    else:
        print("Invalid mode")
        return None, None

    return pattern, text

def print_occurrences(occurrences):
    if occurrences:
        print(' '.join(map(str, occurrences)))
    else:
        print("Pattern not found in text")

def get_occurrences(pattern, text):
    d = 256
    q = 101
    p_len = len(pattern)
    t_len = len(text)
    h = pow(d, p_len-1, q)
    p_hash = 0
    t_hash = 0
    for i in range(p_len):
        p_hash = (d*p_hash + ord(pattern[i])) % q
        t_hash = (d*t_hash + ord(text[i])) % q
    occurrences = []
    for i in range(t_len-p_len+1):
        if p_hash == t_hash and pattern == text[i:i+p_len]:
            occurrences.append(i)
        if i < t_len-p_len:
            t_hash = (d*(t_hash-ord(text[i])*h) + ord(text[i+p_len])) % q
    return occurrences

if __name__ == '__main__':
    pattern, text = read_input()
    if pattern and text:
        occurrences = get_occurrences(pattern, text)
        print_occurrences(occurrences)
