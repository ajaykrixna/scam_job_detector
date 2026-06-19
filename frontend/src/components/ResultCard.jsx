export default function ResultCard({
  result,
  theme,
  domainBarColor,
  domainLabel,
}) {
  const t = theme(result.scam_score);

  return (
    <div
      style={{
        background: "#fff",
        border: `0.5px solid ${t.border}`,
        borderRadius: 12,
        padding: 24,
        marginTop: 20,
      }}
    >
      {/* Score Row */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          gap: 20,
          marginBottom: 20,
          flexWrap: "wrap",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: 16,
          }}
        >
          <div
            style={{
              width: 80,
              height: 80,
              borderRadius: "50%",
              border: `3px solid ${t.circle}`,
              display: "flex",
              flexDirection: "column",
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            <span
              style={{
                fontSize: 28,
                fontWeight: 600,
                color: t.circle,
              }}
            >
              {result.scam_score}
            </span>

            <span
              style={{
                fontSize: 12,
                color: "#9ca3af",
              }}
            >
              /100
            </span>
          </div>

          <div>
            <div
              style={{
                fontSize: 12,
                color: "#6b7280",
                marginBottom: 6,
              }}
            >
              Risk score
            </div>

            <span
              style={{
                background: t.badge,
                color: t.badgeText,
                padding: "6px 12px",
                borderRadius: 6,
                fontSize: 13,
                fontWeight: 500,
              }}
            >
              {result.verdict}
            </span>
          </div>
        </div>

        <div
          style={{
            background: t.badge,
            color: t.badgeText,
            padding: "12px 16px",
            borderRadius: 8,
            maxWidth: 300,
            fontSize: 13,
            lineHeight: 1.5,
          }}
        >
          {result.recommendation}
        </div>
      </div>

      {/* Reasoning */}
      <p
        style={{
          fontSize: 14,
          color: "#4b5563",
          lineHeight: 1.7,
          marginBottom: 20,
        }}
      >
        {result.reasoning}
      </p>

      {/* Flags */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: 20,
        }}
      >
        {/* Red Flags */}
        <div>
          <h3
            style={{
              color: "#dc2626",
              fontSize: 14,
              marginBottom: 10,
            }}
          >
            🚩 Red Flags
          </h3>

          {result.red_flags?.length > 0 ? (
            result.red_flags.map((flag, index) => (
              <div
                key={index}
                style={{
                  background: "#fef2f2",
                  padding: 10,
                  borderRadius: 8,
                  marginBottom: 8,
                  fontSize: 13,
                  lineHeight: 1.5,
                }}
              >
                {flag}
              </div>
            ))
          ) : (
            <p style={{ color: "#9ca3af" }}>None found</p>
          )}
        </div>

        {/* Green Flags */}
        <div>
          <h3
            style={{
              color: "#16a34a",
              fontSize: 14,
              marginBottom: 10,
            }}
          >
            ✅ Green Flags
          </h3>

          {result.green_flags?.length > 0 ? (
            result.green_flags.map((flag, index) => (
              <div
                key={index}
                style={{
                  background: "#f0fdf4",
                  padding: 10,
                  borderRadius: 8,
                  marginBottom: 8,
                  fontSize: 13,
                  lineHeight: 1.5,
                }}
              >
                {flag}
              </div>
            ))
          ) : (
            <p style={{ color: "#9ca3af" }}>
              No green flags identified.
            </p>
          )}

          {result.domain_age != null && (
            <div style={{ marginTop: 16 }}>
              <div
                style={{
                  display: "flex",
                  justifyContent: "space-between",
                  fontSize: 12,
                  marginBottom: 6,
                }}
              >
                <span>Domain Age</span>
                <span>
                  {result.domain_age} days ·{" "}
                  {domainLabel(result.domain_age)}
                </span>
              </div>

              <div
                style={{
                  height: 8,
                  background: "#f3f4f6",
                  borderRadius: 999,
                  overflow: "hidden",
                }}
              >
                <div
                  style={{
                    height: "100%",
                    width: `${Math.min(
                      (result.domain_age / 365) * 100,
                      100
                    )}%`,
                    background: domainBarColor(result.domain_age),
                  }}
                />
              </div>
            </div>
          )}
        </div>
      </div>

          {/* Evidence Summary */}
        {result.evidence_summary?.length > 0 && (
          <div
            style={{
              marginTop: 20,
              marginBottom: 20,
              padding: 16,
              border: "1px solid #e5e7eb",
              borderRadius: 12,
              background: "#fafafa",
            }}
          >
            <h3
              style={{
                marginTop: 0,
                marginBottom: 12,
                fontSize: 14,
              }}
            >
              📋 Evidence Summary
            </h3>

            {result.evidence_summary.map((item, index) => (
              <div
                key={index}
                style={{
                  background: "#f0fdf4",
                  color: "#166534",
                  padding: 10,
                  borderRadius: 8,
                  marginBottom: 8,
                  fontSize: 13,
                }}
              >
                ✓ {item}
              </div>
            ))}
          </div>
        )}

            {/* Source Verification */}
      {result.source_verification && (
        <div
          style={{
            marginTop: 20,
            padding: 16,
            border: "1px solid #e5e7eb",
            borderRadius: 12,
            background: "#fafafa",
          }}
        >
          <h3
            style={{
              marginTop: 0,
              marginBottom: 12,
              fontSize: 14,
            }}
          >
            🔍 Source Verification
          </h3>

          <div style={{ fontSize: 14 }}>

          {result.source_verification.source_domain && (
            <div
              style={{
                background: "#f0fdf4",
                color: "#166534",
                padding: 10,
                borderRadius: 8,
                marginBottom: 10,
              }}
            >
              ✓ Source domain available
            </div>
          )}

          <div
            style={{
              background: "#f9fafb",
              padding: 12,
              borderRadius: 8,
              marginBottom: 10,
              wordBreak: "break-word",
            }}
          >
            {result.source_verification.source_domain || "Source URL not available"}
          </div>

          {result.source_verification.email_domain ? (
          <div
            style={{
              background:
                result.source_verification.email_type === "Corporate"
                  ? "#f0fdf4"
                  : "#fef2f2",
              border:
                result.source_verification.email_type === "Corporate"
                  ? "1px solid #bbf7d0"
                  : "1px solid #fecaca",
              padding: 12,
              borderRadius: 8,
            }}
          >
            <div
              style={{
                fontSize: 13,
                fontWeight: 600,
                marginBottom: 6,
                color:
                  result.source_verification.email_type === "Corporate"
                    ? "#166534"
                    : "#991b1b",
              }}
            >
              {result.source_verification.email_type === "Corporate"
                ? "✓ Corporate Email Detected"
                : "⚠ Free Email Provider Detected"}
            </div>

            <div>
              {result.source_verification.email_domain}
            </div>
          </div>
        ) : (
          <div
            style={{
              background: "#f9fafb",
              padding: 12,
              borderRadius: 8,
              color: "#6b7280",
            }}
          >
            No recruiter email found in posting
          </div>
        )}

        </div>
        </div>
      )}
    </div>
  );
}