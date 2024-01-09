from starlette.requests import Request

import ray
from ray import serve
from ray.serve.handle import DeploymentHandle

from fastapi import FastAPI

from transformers import pipeline

app = FastAPI()

@serve.deployment
@serve.ingress(app)
class Summarizer:
    def __init__(self):
        # Load model.
        self.model = pipeline("summarization", model="t5-small")

    @app.get("/healthz")
    def health(self):
        return "Hello from RayServe!"

    @app.get("/summarize")
    def summarize(self, text: str) -> str:
        # Run inference
        model_output = self.model(text, min_length=5, max_length=15)

        # Post-process output to return only the summary text
        summary = model_output[0]["summary_text"]

        return summary

summarize_app = Summarizer.bind()
