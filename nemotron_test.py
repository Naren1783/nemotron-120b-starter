from openai import OpenAI

client = OpenAI(
  base_url = "https://integrate.api.nvidia.com/v1",
  api_key = "Paste the API key you get in https://build.nvidia.com/nvidia/nemotron-3-ultra-550b-a55b" 
)

completion = client.chat.completions.create(
  model="nvidia/nemotron-3-super-120b-a12b",
  messages=[{"role":"user","content":"When did india won cricket world cup in t20 and odi both."}],
  temperature=1,
  top_p=0.95,
  max_tokens=16384,
  extra_body={"chat_template_kwargs":{"enable_thinking":True},"reasoning_budget":16384},
)

# Print the model's response
print(completion.choices[0].message.content)