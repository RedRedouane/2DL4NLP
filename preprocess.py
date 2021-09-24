from tokenizers import Tokenizer

tokenizer = Tokenizer.from_file("../byte-level-bpe-en.tokenizer.json")

encoded = tokenizer.encode("I can feel the magic, can you?")

print(encoded)
print(encoded.tokens)
