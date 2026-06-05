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

# ✅ CORS FIX (IMPORTANT for Vercel frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing (change to Vercel URL in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check
@app.get("/")
def home():
    return {
        "message": "AI App Compiler Running"
    }

# Main pipeline endpoint
@app.post("/generate")
def generate(payload: dict):

    start_time = time.time()

    if "prompt" not in payload:
        return {
            "error": "prompt field required"
        }

    prompt = payload["prompt"]

    # 1. Ambiguity Check
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

    # 2. Intent Extraction
    intent = extract_intent(prompt)

    # 3. Assumptions
    assumptions = generate_assumptions(intent)

    # 4. Decision Log
    decision_log = generate_decision_log(intent)

    # 5. Architecture Planning
    architecture = create_architecture(intent)

    # 6. Schema Generation
    config = generate_config(architecture)

    # 7. Validation
    validation = validate_config(config)

    repairs = []

    # 8. Repair Engine
    if not validation["valid"]:
        repaired = repair_config(
            config,
            validation["errors"]
        )

        config = repaired["config"]
        repairs = repaired["repairs"]

    # 9. Runtime Preview
    preview = runtime_preview(config)

    # 10. Metrics
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