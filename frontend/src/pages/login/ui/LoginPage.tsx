import { useState } from "react";
import { login, setStoredToken } from "@/shared/api";

interface LoginPageProps {
  onLoggedIn: (accessToken: string) => void;
}

export function LoginPage({ onLoggedIn }: LoginPageProps) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setLoading(true);
    try {
      const data = await login(username, password);
      setStoredToken(data.access);
      onLoggedIn(data.access);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Login failed");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div style={{ maxWidth: 320, margin: "2rem auto", padding: "0 1rem" }}>
      <h1>Open Property Core</h1>
      <p>Sign in</p>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: "1rem" }}>
          <label htmlFor="username" style={{ display: "block", marginBottom: 4 }}>
            Username
          </label>
          <input
            id="username"
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
            autoComplete="username"
            style={{ width: "100%", padding: 8 }}
          />
        </div>
        <div style={{ marginBottom: "1rem" }}>
          <label htmlFor="password" style={{ display: "block", marginBottom: 4 }}>
            Password
          </label>
          <input
            id="password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            autoComplete="current-password"
            style={{ width: "100%", padding: 8 }}
          />
        </div>
        {error && (
          <p style={{ color: "crimson", marginBottom: "1rem" }}>{error}</p>
        )}
        <button type="submit" disabled={loading} style={{ padding: "8px 16px" }}>
          {loading ? "Signing in…" : "Sign in"}
        </button>
      </form>
    </div>
  );
}
