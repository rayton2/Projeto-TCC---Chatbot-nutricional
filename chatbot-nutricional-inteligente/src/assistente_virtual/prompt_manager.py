class PromptManager:
    def __init__(self):
        self.prompts = {}

    def add_prompt(self, key, prompt):
        self.prompts[key] = prompt

    def get_prompt(self, key):
        return self.prompts.get(key, "Prompt not found.")

    def build_prompt(self, key, **kwargs):
        prompt = self.get_prompt(key)
        if prompt == "Prompt not found.":
            return prompt
        return prompt.format(**kwargs)