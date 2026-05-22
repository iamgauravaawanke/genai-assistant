from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
)


def ask_qwen(prompt):

    response = client.chat.completions.create(
        model="qwen2.5-coder-1.5b-instruct",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


# Test
# answer = ask_qwen("Who is Dhoni?")
# print(answer)