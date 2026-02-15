import { useEffect, useState } from "react";
import {
  fetchContracts,
  createContract,
  type Contract,
  type ContractCreateInput,
} from "@/entities/contract";
import { fetchUnits } from "@/entities/unit";
import { fetchParties } from "@/entities/party";
import type { Unit } from "@/entities/unit";
import type { Party } from "@/entities/party";
import { useAuth } from "@/app/providers";

export function ContractListPage() {
  const { logout } = useAuth();
  const [contracts, setContracts] = useState<Contract[]>([]);
  const [units, setUnits] = useState<Unit[]>([]);
  const [parties, setParties] = useState<Party[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [showForm, setShowForm] = useState(false);
  const [submitting, setSubmitting] = useState(false);
  const [formData, setFormData] = useState<ContractCreateInput>({
    unit: 0,
    party: 0,
    start_date: "",
    end_date: "",
    monthly_amount: "",
    status: "draft",
  });

  const load = () => {
    setLoading(true);
    Promise.all([fetchContracts(), fetchUnits(), fetchParties()])
      .then(([contractsRes, unitsRes, partiesRes]) => {
        setContracts(contractsRes.results);
        setUnits(unitsRes.results);
        setParties(partiesRes.results);
      })
      .catch((err) => setError(err instanceof Error ? err.message : "Failed to load"))
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    load();
  }, []);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!formData.unit || !formData.party) return;
    setSubmitting(true);
    createContract({
      ...formData,
      unit: formData.unit,
      party: formData.party,
    })
      .then(() => {
        setShowForm(false);
        setFormData({
          unit: 0,
          party: 0,
          start_date: "",
          end_date: "",
          monthly_amount: "",
          status: "draft",
        });
        load();
      })
      .catch((err) => setError(err instanceof Error ? err.message : "Failed to create"))
      .finally(() => setSubmitting(false));
  };

  const formatDate = (s: string) => (s ? new Date(s).toLocaleDateString() : "—");

  if (loading && contracts.length === 0) return <p>Loading contracts…</p>;
  if (error && contracts.length === 0) return <p style={{ color: "crimson" }}>{error}</p>;

  const unitMap = new Map(units.map((u) => [u.id, u]));
  const partyMap = new Map(parties.map((p) => [p.id, p]));

  return (
    <div style={{ padding: "1rem 2rem" }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1rem" }}>
        <h1>Contracts</h1>
        <div style={{ display: "flex", gap: "0.5rem" }}>
          <button type="button" onClick={() => setShowForm(!showForm)}>
            {showForm ? "Cancel" : "Add Contract"}
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
          <h3 style={{ marginTop: 0 }}>New Contract</h3>
          <div style={{ display: "flex", flexDirection: "column", gap: "0.5rem" }}>
            <label>
              Unit{" "}
              <select
                value={formData.unit || ""}
                onChange={(e) => setFormData({ ...formData, unit: Number(e.target.value) })}
                required
              >
                <option value="">Select unit</option>
                {units.map((u) => (
                  <option key={u.id} value={u.id}>
                    {u.name}
                  </option>
                ))}
              </select>
            </label>
            <label>
              Party{" "}
              <select
                value={formData.party || ""}
                onChange={(e) => setFormData({ ...formData, party: Number(e.target.value) })}
                required
              >
                <option value="">Select party</option>
                {parties.map((p) => (
                  <option key={p.id} value={p.id}>
                    {p.name} ({p.party_type})
                  </option>
                ))}
              </select>
            </label>
            <label>
              Start date <input
                type="date"
                value={formData.start_date}
                onChange={(e) => setFormData({ ...formData, start_date: e.target.value })}
                required
              />
            </label>
            <label>
              End date <input
                type="date"
                value={formData.end_date}
                onChange={(e) => setFormData({ ...formData, end_date: e.target.value })}
                required
              />
            </label>
            <label>
              Monthly amount <input
                type="number"
                step="0.01"
                value={formData.monthly_amount}
                onChange={(e) => setFormData({ ...formData, monthly_amount: e.target.value })}
                required
              />
            </label>
            <label>
              Status{" "}
              <select
                value={formData.status ?? "draft"}
                onChange={(e) => setFormData({ ...formData, status: e.target.value })}
              >
                <option value="draft">Draft</option>
                <option value="active">Active</option>
                <option value="terminated">Terminated</option>
              </select>
            </label>
            <button type="submit" disabled={submitting}>
              {submitting ? "Creating…" : "Create"}
            </button>
          </div>
        </form>
      )}

      {contracts.length === 0 ? (
        <p>No contracts yet.</p>
      ) : (
        <table style={{ width: "100%", borderCollapse: "collapse" }}>
          <thead>
            <tr>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Unit</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Party</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Start</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>End</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Amount</th>
              <th style={{ textAlign: "left", padding: 8, borderBottom: "1px solid #ccc" }}>Status</th>
            </tr>
          </thead>
          <tbody>
            {contracts.map((c) => (
              <tr key={c.id}>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>
                  {unitMap.get(c.unit)?.name ?? c.unit}
                </td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>
                  {partyMap.get(c.party)?.name ?? c.party}
                </td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{formatDate(c.start_date)}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{formatDate(c.end_date)}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{c.monthly_amount}</td>
                <td style={{ padding: 8, borderBottom: "1px solid #eee" }}>{c.status}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}
