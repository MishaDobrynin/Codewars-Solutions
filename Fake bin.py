def fake_bin(x):
    return "".join(['0' if int(el) < 5 else '1' for el in x])