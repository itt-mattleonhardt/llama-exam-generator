import requests
import json

EXAM = 'AWS SAP-C03'
MODEL = 'wizardlm2:7b'
ENDPOINT = 'http://localhost:11434/api/generate'


def execute_prompt(p):
    response = requests.post(
        ENDPOINT,
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "model": MODEL,
            "prompt": p,
            "stream": False,
        })
    )

    if response.status_code != 200:
        print("Error: ", response.status_code, response.text)
        exit(1)

    return json.loads(response.text)["response"]


while True:
    topic = input('Exam question topic (blank for any, \'quit\' to quit): ')
    if topic.lower() in ['quit', 'q']:
        exit(0)

    prompt = (f'Generate a challenging test prep question for the {EXAM} exam. The question should be in the '
              'style of the actual exam, with the following guidelines:\n'
              '1. Present a complex scenario or problem that requires a deeper understanding of AWS services and best '
              'practices.\n'
              '2. Provide four answer options (A, B, C, D) that are lengthier and more detailed than simple '
              'one-liners.\n'
              '3. Ensure the correct answer is not immediately obvious, and the incorrect options are plausible but '
              'subtly incorrect.\n'
              '4. Use technical terminology and specific AWS service names where appropriate.\n'
              '5. Do not include the answer to the question in the generated output.\n'
              'Format the question and options clearly and concisely.')

    if topic:
        prompt += f'\nFocus the question topic on {topic}'

    question = execute_prompt(prompt)
    print(question, "\n")

    answer = input('What\'s your answer? ')

    score = execute_prompt(f'Is this answer: {answer} correct for the following question? Explain why each possible'
                           f'answer is correct or incorrect.\n\n'
                           f'{question}')

    print(score, "\n")
