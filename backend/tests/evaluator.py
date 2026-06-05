import json
import requests
import time

API_URL = "http://127.0.0.1:8000/generate"


def run_evaluation():

    with open("tests/prompts.json", "r") as file:
        prompts = json.load(file)

    total = len(prompts)

    success_count = 0
    clarification_count = 0
    failure_count = 0

    total_latency = 0

    results = []

    print("\nRunning Evaluation...\n")

    for item in prompts:

        prompt = item["prompt"]

        start = time.time()

        try:

            response = requests.post(
                API_URL,
                json={
                    "prompt": prompt
                }
            )

            latency = round(
                (time.time() - start) * 1000,
                2
            )

            total_latency += latency

            if response.status_code == 200:

                data = response.json()

                if data.get("status") == "needs_clarification":

                    clarification_count += 1

                    status = "CLARIFICATION"

                else:

                    success_count += 1

                    status = "SUCCESS"

            else:

                failure_count += 1

                status = "FAILED"

            results.append({
                "prompt": prompt,
                "status": status,
                "latency_ms": latency
            })

            print(
                f"{status:<15} | {latency:>6} ms | {prompt}"
            )

        except Exception as e:

            failure_count += 1

            print(
                f"FAILED          | ERROR | {prompt}"
            )

            print(str(e))

    average_latency = round(
        total_latency / total,
        2
    )

    success_rate = round(
        (success_count / total) * 100,
        2
    )

    summary = {

        "total_prompts": total,

        "success_count": success_count,

        "clarification_count": clarification_count,

        "failure_count": failure_count,

        "success_rate_percent": success_rate,

        "average_latency_ms": average_latency
    }

    print("\n")
    print("=" * 60)
    print("EVALUATION SUMMARY")
    print("=" * 60)

    print(
        json.dumps(
            summary,
            indent=4
        )
    )

    with open(
        "tests/evaluation_results.json",
        "w"
    ) as outfile:

        json.dump(
            {
                "summary": summary,
                "results": results
            },
            outfile,
            indent=4
        )

    print(
        "\nSaved results to tests/evaluation_results.json"
    )


if __name__ == "__main__":
    run_evaluation()