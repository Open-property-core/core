import { useEffect, useState } from "react";
import { fetchParties, createParty, type Party, type PartyCreateInput } from "@/entities/party";
import { useAuth } from "@/app/providers";

export function PartyListPage() {
  const { logout } = useAuth();
  const [parties, setParties] = useState<Party[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [formData, setFormData] = useState<PartyCreateInput>({
    name: "",
    party_type: "tenant",
    email: "",
    phone: "",
  });

  const load = () => {
    setLoading(true);
    fetchParties()
      .then((data) => setParties(data.results))
      .catch((err) => setError(err instanceof Error ? err.message : "Failed to load"))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    load();
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setSubmitting(true);
    createParty(formData)
      .then(() => {
        setShowForm(false);
        setFormData({ name: "", party_type: "tenant", email: "", phone: "" });
        load();
      })
      .catch((err) => setError(err instanceof Error ? err.message : "Failed to create"))
      .finally(() => setSubmitting(false));
  };

  if (loading && parties.length === 0) return <p>Loading parties…</p>;
  if (error && parties.length === 0) return <p style={{ color: "crimson" }}>{error}</p>;

  return (
    <div style={{ padding: "1rem 2rem" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1rem" }}>
        <h1>Parties</h1>
        <div style={{ display: "flex", gap: "0.5rem" }}>
          <button type="button" onClick={() => setShowForm(!showForm)}>
            {showForm ? "Cancel" : "Add Party"}
          </button>
          <button type="button" onClick={logout}>
            Sign out
          </button>
        </div>
      </div>

      {showForm && (
        <form
          onSubmit={handleSubmit}
          style={{ marginBottom: "1.5rem", padding: "1rem", border: "1px solid #ccc", borderRadius: 4, maxWidth: 400 }}
        >
          <h3 style={{ marginTop: 0 }}>New Party</h3>
          <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
            <label>
              Name <input
                type="text"
                value={formData.name}
                onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                required
              />
            </label>
            <label>
              Type{" "}
              <select
                value={formData.party_type}
                onChange={(e) => setFormData({ ...formData, party_type: e.target.value })}
              >
                <option value="tenant">Tenant</option>
                <option value="landlord">Landlord</option>
                <option value="manager">Manager</option>
              </select>
            </label>
            <label>
              Email <input
                type="email"
                value={formData.email ?? ""}
                onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              />
            </label>
            <label>
              Phone <input
                type="text"
                value={formData.phone ?? ""}
                onChange={(e) => setFormData({ ...formData, phone: e.target.value })}
              />
            </label>
            <button type="submit" disabled={submitting}>
              {submitting ? "Creating…" : "Create"}
            </button>
          </div>
        </form>
      )}

      {parties.length === 0 ? (
        <p>No parties yet.</p>
      ) : (
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Name</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Type</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Email</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Phone</th>
            </tr>
          </thead>
          <tbody>
            {parties.map((p) => (
              <tr key={p.id}>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{p.name}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{p.party_type}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{p.email || "—"}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{p.phone || "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
