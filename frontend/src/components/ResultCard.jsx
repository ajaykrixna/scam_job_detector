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
    </div>
  );
}