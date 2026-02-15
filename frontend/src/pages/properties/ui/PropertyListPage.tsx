import { useEffect, useState } from "react";
import { fetchProperties, type Property } from "@/entities/property";
import { useAuth } from "@/app/providers";

export function PropertyListPage() {
  const { logout } = useAuth();
  const [properties, setProperties] = useState<Property[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let cancelled = false;
    fetchProperties()
      .then((data) => {
        if (!cancelled) setProperties(data.results);
      })
      .catch((err) => {
        if (!cancelled) setError(err instanceof Error ? err.message : "Failed to load");
      })
      .finally(() => {
        if (!cancelled) setLoading(false);
      });
    return () => {
      cancelled = true;
    };
  }, []);

  if (loading) return <p>Loading properties…</p>;
  if (error) return <p style={{ color: "crimson" }}>{error}</p>;

  return (
    <div style={{ padding: "1rem 2rem" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1rem" }}>
        <h1>Properties</h1>
        <button type="button" onClick={logout}>
          Sign out
        </button>
      </div>
      {properties.length === 0 ? (
        <p>No properties yet.</p>
      ) : (
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Name</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Address</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Type</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Status</th>
            </tr>
          </thead>
          <tbody>
            {properties.map((p) => (
              <tr key={p.id}>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{p.name}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{p.address || "—"}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{p.property_type}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{p.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
