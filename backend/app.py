from fastapi import FastAPI
import time
from fastapi.middleware.cors import CORSMiddleware
from pipeline.intent import extract_intent
from pipeline.planner import create_architecture
from pipeline.generator import generate_config
from pipeline.validator import validate_config
from pipeline.repair import repair_config

from pipeline.ambiguity import check_ambiguity
from pipeline.assumptions import generate_assumptions
from pipeline.decision_log import generate_decision_log
from pipeline.metrics import generate_metrics

from runtime.executor import runtime_preview

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running"
    }


@app.post("/generate")
def generate(payload: dict):

    start_time = time.time()

    if "prompt" not in payload:
        return {
            "error": "prompt field required"
        }

    prompt = payload["prompt"]

    # Ambiguity Check
    ambiguity = check_ambiguity(prompt)

    if ambiguity["clarification_needed"]:
        return {
            "status": "needs_clarification",
            "ambiguity": ambiguity,
            "questions": [
                "What type of application would you like?",
                "Who are the users?",
                "What core features are required?"
            ]
        }

    # Intent Extraction
    intent = extract_intent(prompt)

    # Assumptions
    assumptions = generate_assumptions(intent)

    # Decision Log
    decision_log = generate_decision_log(intent)

    # Architecture Planning
    architecture = create_architecture(intent)

    # Schema Generation
    config = generate_config(architecture)

    # Validation
    validation = validate_config(config)

    repairs = []

    # Repair Engine
    if not validation["valid"]:

        repaired = repair_config(
            config,
            validation["errors"]
        )

        config = repaired["config"]
        repairs = repaired["repairs"]

    # Runtime Preview
    preview = runtime_preview(config)

    # Metrics
    metrics = generate_metrics(
        start_time,
        len(repairs),
        validation
    )

    return {
        "intent": intent,
        "assumptions": assumptions,
        "decision_log": decision_log,
        "architecture": architecture,
        "config": config,
        "validation": validation,
        "repairs": repairs,
        "metrics": metrics,
        "runtime_preview": preview
    }