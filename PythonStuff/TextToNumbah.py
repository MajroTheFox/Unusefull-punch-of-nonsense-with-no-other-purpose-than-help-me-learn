text = "More ma nilla!"
numbah = int.from_bytes(text.encode("utf-8"), "big")
back = numbah.to_bytes((numbah.bit_length() + 7) // 8, "big").decode("utf-8")
print(text)
print(numbah)
print(back)