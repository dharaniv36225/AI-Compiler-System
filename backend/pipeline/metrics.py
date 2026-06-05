import time


def generate_metrics(
    start_time,
    repairs_count,
    validation
):

    latency = max(
        round(
            (time.time() - start_time) * 1000,
            2
        ),
        1
    )

    validation_score = 100

    if not validation["valid"]:
        validation_score -= 20

    return {
        "latency_ms": latency,
        "repairs_applied": repairs_count,
        "validation_score": validation_score
    }