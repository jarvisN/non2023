from transformers import GPT2LMHeadModel, GPT2Tokenizer

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

input_text = "Hello, how are you?"  # ป้อนข้อความของคุณที่นี่
inputs = tokenizer.encode(input_text, return_tensors="pt")

outputs = model.generate(inputs, max_length=150, num_return_sequences=5, temperature=0.7)

for i, output in enumerate(outputs):
    print(f"Generated text {i+1}:")
    print(tokenizer.decode(output, skip_special_tokens=True))
