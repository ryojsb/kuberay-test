from starlette.requests import Request

import ray
from ray import serve
from ray.serve.handle import DeploymentHandle

from transformers import pipeline

@serve.deployment
class Summarizer:
    def __init__(self):
        # Load model.
        self.model = pipeline("summarization", model="t5-small")

    def summarize(self, text: str) -> str:
        # Run inference
        model_output = self.model(text, min_length=5, max_length=15)

        # Post-process output to return only the summary text
        summary = model_output[0]["summary_text"]

        return summary

    async def __call__(self, http_request: Request) -> str:
        english_text: str = await http_request.json()
        return self.summarize(english_text)

summarize_app = Summarizer.bind()
