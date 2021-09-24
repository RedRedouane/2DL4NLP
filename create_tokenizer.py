# from tokenizers import CharBPETokenizer
#
# # Initialize a tokenizer
# vocab = "./path/to/vocab.json"
# merges = "./path/to/merges.txt"
# tokenizer = CharBPETokenizer(vocab, merges)
#
# # And then encode:
# encoded = tokenizer.encode("I can feel the magic, can you?")
# print(encoded.ids)
# print(encoded.tokens)
#
# # Initialize a tokenizer
# tokenizer = CharBPETokenizer()
#
# # Then train it!
# tokenizer.train([ "./path/to/files/1.txt", "./path/to/files/2.txt" ])
#
# # Now, let's use it:
# encoded = tokenizer.encode("I can feel the magic, can you?")
#
# # And finally save it somewhere
# tokenizer.save("./path/to/directory/my-bpe.tokenizer.json")

from tokenizers import Tokenizer, models, pre_tokenizers, decoders, trainers, processors

# Initialize a tokenizer
tokenizer = Tokenizer(models.BPE())

# Customize pre-tokenization and decoding
tokenizer.pre_tokenizer = pre_tokenizers.ByteLevel(add_prefix_space=True)
tokenizer.decoder = decoders.ByteLevel()
tokenizer.post_processor = processors.ByteLevel(trim_offsets=True)

# And then train
trainer = trainers.BpeTrainer(vocab_size=20000, min_frequency=2)
tokenizer.train([
	"../train.en",
	"../val.en",
	"../test.en"
], trainer=trainer)

# And Save it
tokenizer.save("../byte-level-bpe-en.tokenizer.json", pretty=True)
