import { useState } from "react";
import axios from "axios";
import ResultCard from "./components/ResultCard";

export default function App() {
  const [mode, setMode] = useState("url");
  const [url, setUrl] = useState("");
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  

  const analyze = async () => {
    if (mode === "url" && !url.trim()) return alert("Paste a URL first");
    if (mode === "text" && !text.trim()) return alert("Paste job description first");
    setLoading(true);
    setError("");
    setResult(null);
    try {
      const payload = mode === "url" ? { url, text: "" } : { url: "", text };


      const res = await axios.post(
        "https://scam-job-detector-1nln.onrender.com/analyze",
        payload,
         { timeout: 30000 }
      );
      setResult(res.data);
    } catch (e) {
    setError("Analysis failed. Please try again or paste the job description manually.");
}
    setLoading(false);
  };

  const theme = (score) => {
    if (score >= 70) return {
      border: "#fca5a5", circle: "#dc2626",
      badge: "#fee2e2", badgeText: "#dc2626",
      flagBg: "#fef2f2"
    };
    if (score >= 40) return {
      border: "#fcd34d", circle: "#d97706",
      badge: "#fef3c7", badgeText: "#d97706",
      flagBg: "#fffbeb"
    };
    return {
      border: "#86efac", circle: "#16a34a",
      badge: "#dcfce7", badgeText: "#16a34a",
      flagBg: "#f0fdf4"
    };
  };

  const domainBarColor = (days) => {
    if (days < 30) return "#dc2626";
    if (days < 180) return "#d97706";
    return "#16a34a";
  };

  const domainLabel = (days) => {
    if (days < 30) return "New → suspicious";
    if (days < 180) return "Fairly new";
    return "Established";
  };

  return (
    <div style={{
      maxWidth: 900,
      margin: "36px auto",
      padding: "0 24px",
      fontFamily: "-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
    }}>

      {/* Header */}
      <div style={{ marginBottom: 24 }}>
        <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 4 }}>
          <span style={{ fontSize: 22 }}>🚨</span>
          <h1 style={{
            fontSize: 24,
            fontWeight: 700,
            margin: 0,
            color: "#111"
          }}>
            Scam job detector
          </h1>
        </div>
        <p style={{ fontSize: 15, color: "#6b7280", margin: "8px 0 0" }}>
          Paste a job URL or description — AI checks if it's legit.
        </p>
      </div>

      {/* Input Card */}
      <div style={{
        background: "#fff",
        border: "1px solid #e5e7eb",
        borderRadius: 20,
        padding: 28,
        marginBottom: 20,
        boxShadow: "0 1px 2px rgba(0,0,0,0.04)"
      }}>

        {/* Toggle */}
        <div style={{
          display: "flex",
          background: "#f3f4f6",
          borderRadius: 14,
          padding: 4,
          marginBottom: 22
        }}>
          {["url", "text"].map((m) => (
            <button key={m} onClick={() => {
                  setMode(m);

                  if (m === "url") {
                    setText("");
                  } else {
                    setUrl("");
                  }
                }}
                style={{
              flex: 1, padding: "8px 0", borderRadius: 8,
              border: "0.5px solid",
              borderColor: mode === m ? "#93c5fd" : "#e5e7eb",
              background: mode === m ? "#eff6ff" : "transparent",
              color: mode === m ? "#1d4ed8" : "#6b7280",
              fontSize: 13, fontWeight: mode === m ? 500 : 400,
              cursor: "pointer"
            }}>
              {m === "url" ? "Paste URL" : "Paste Description"}
            </button>
          ))}
        </div>

        {/* Input */}
        {mode === "url" ? (
          <input
            type="text"
            placeholder="https://company.com/jobs/ml-engineer"
            value={url}
            onChange={e => setUrl(e.target.value)}
            onKeyDown={e => e.key === "Enter" && analyze()}
            style={{
              width: "100%",
              boxSizing: "border-box",
              padding: "16px 18px",
              fontSize: 16,
              border: "1px solid #e5e7eb",
              borderRadius: 14,
              outline: "none",
              marginBottom: 18,
              color: "#111"
            }}
          />
        ) : (
          <textarea
            placeholder="Paste full job description here..."
            value={text}
            onChange={e => setText(e.target.value)}
            rows={6}
            style={{
              width: "100%", boxSizing: "border-box",
              padding: "10px 12px", fontSize: 14,
              border: "0.5px solid #e5e7eb", borderRadius: 8,
              outline: "none", marginBottom: 12,
              resize: "vertical", fontFamily: "inherit", color: "#111"
            }}
          />
        )}

        {/* Button */}
        <button
          onClick={analyze}
          disabled={loading}
          onMouseEnter={(e) => {
            if (!loading) e.target.style.background = "#222";
          }}
          onMouseLeave={(e) => {
            if (!loading) e.target.style.background = "#111";
          }}
          style={{
            width: "100%",
            height: 56,
            background: "#111",
            color: "#fff",
            border: "none",
            borderRadius: 14,
            fontSize: 16,
            fontWeight: 600,
            cursor: loading ? "not-allowed" : "pointer"
          }}
        >
          {loading ? "Analyzing..." : "Analyze job posting"}
        </button>

        {error && (
          <p style={{ color: "#dc2626", fontSize: 13, margin: "10px 0 0" }}>
            ⚠️ {error}
          </p>
        )}
      </div>

      {result && (
  <ResultCard
    result={result}
    theme={theme}
    domainBarColor={domainBarColor}
    domainLabel={domainLabel}
  />
)}

    </div>
  );
}