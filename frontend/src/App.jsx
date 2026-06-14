import { useState } from "react";
import axios from "axios";
import {
  Cpu,
  Database,
  Shield,
  CheckCircle,
  Download,
} from "lucide-react";

import ArchitectureDiagram from "./components/ArchitectureDiagram";

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const generateApp = async () => {
    if (!prompt.trim()) return;

    try {
      setLoading(true);

      const response = await axios.post(
       `${import.meta.env.VITE_API_URL}generate`,
       {
        prompt,
       }
      );

      setResult(response.data);
    } catch (err) {
      console.error(err);
      alert("Backend connection failed");
    } finally {
      setLoading(false);
    }
  };

  const downloadJson = () => {
    if (!result) return;

    const blob = new Blob(
      [JSON.stringify(result, null, 2)],
      {
        type: "application/json",
      }
    );

    const url = URL.createObjectURL(blob);

    const a = document.createElement("a");

    a.href = url;
    a.download = "generated_app.json";

    a.click();

    URL.revokeObjectURL(url);
  };

  return (
    <div className="container">
      <header>
        <h1>🤖 AI App Compiler</h1>

        <p>
          Natural Language → Architecture → Validation → Runtime
        </p>
      </header>

      <div className="prompt-box">
        <textarea
          placeholder="Build CRM with login contacts dashboard payments analytics"
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <div className="actions">
          <button onClick={generateApp}>
            {loading ? "Generating..." : "Generate"}
          </button>

          {result && (
            <button
              className="download-btn"
              onClick={downloadJson}
            >
              <Download size={18} />
              Export JSON
            </button>
          )}
        </div>
      </div>

      {result && (
        <>
          <div className="metrics">
            <MetricCard
              icon={<Cpu size={24} />}
              title="Latency"
              value={`${result.metrics?.latency_ms ?? 0} ms`}
            />

            <MetricCard
              icon={<Database size={24} />}
              title="Repairs"
              value={result.metrics?.repairs_applied ?? 0}
            />

            <MetricCard
              icon={<CheckCircle size={24} />}
              title="Validation"
              value={`${result.metrics?.validation_score ?? 100}%`}
            />

            <MetricCard
              icon={<Shield size={24} />}
              title="Status"
              value={
                result.validation?.valid
                  ? "Valid"
                  : "Invalid"
              }
            />
          </div>

          <ArchitectureDiagram
            architecture={result.architecture}
          />

          <div className="grid">
            <JsonCard
              title="Intent"
              data={result.intent}
            />

            <JsonCard
              title="Assumptions"
              data={result.assumptions}
            />

            <JsonCard
              title="Decision Log"
              data={result.decision_log}
            />

            <JsonCard
              title="Architecture"
              data={result.architecture}
            />

            <JsonCard
              title="Generated Config"
              data={result.config}
            />

            <JsonCard
              title="Validation"
              data={result.validation}
            />

            <JsonCard
              title="Runtime Preview"
              data={result.runtime_preview}
            />
          </div>
        </>
      )}
    </div>
  );
}

function MetricCard({ icon, title, value }) {
  return (
    <div className="metric-card">
      {icon}
      <h3>{title}</h3>
      <h2>{value}</h2>
    </div>
  );
}

function JsonCard({ title, data }) {
  return (
    <div className="card">
      <h2>{title}</h2>

      <pre>
        {JSON.stringify(data, null, 2)}
      </pre>
    </div>
  );
}
