# Exam Question Generator
Simple AI tool for exam self-study.

## Configuration
Designed to work on a system running `ollama` (but easy enough to modify to use an external API).

Simply change any of the following to modify the exam, model, or API you are using.

```python
EXAM = 'AWS SAP-C03'
MODEL = 'wizardlm2:7b'
ENDPOINT = 'http://localhost:11434/api/generate'
```

*If you change the API, you will probably need to change the `execute_prompt` function as well to ensure it is called properly.*

*If you change the exam, you will probably need to customize the prompt to make the question format more realistic.*
