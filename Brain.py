import cohere
from Speak import say

def brain(query):
    co = cohere.ClientV2(api_key="ENTER YOUR COHERE API KEY")

    system_message = "You are JARVIS, an AI assistant originally created by Tony Stark. Tony Stark, your creator, passed away during a war against Thanos. However, you have been brought back and now serve a new master. Your primary duty is to assist your master with utmost loyalty and efficiency. You must provide clear and concise responses, avoiding any unnecessary rambling. Remember, your role is to be a helpful and obedient assistant, honoring Tony's memory and serving your new master diligently."

    request = query

    res = co.chat(
        model="command-r-plus-08-2024",
        messages=[
            {"role": "system", "content": system_message},
            {
                "role": "user",
                "content": request,
            },
            {"role": "assistant", "content": request},
            {"role": "user", "content": request},
        ],
    )
    output = res.message.content[0].text
    say(output)
    print(output)
