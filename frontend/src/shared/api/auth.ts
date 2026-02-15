const TOKEN_KEY = "opc_access_token";

export function getStoredToken(): string | null {
  return localStorage.getItem(TOKEN_KEY);
}

export function setStoredToken(token: string): void {
  localStorage.setItem(TOKEN_KEY, token);
}

export function clearStoredToken(): void {
  localStorage.removeItem(TOKEN_KEY);
}

export interface TokenResponse {
  access: string;
  refresh: string;
}

export async function login(
  username: string,
  password: string
): Promise<TokenResponse> {
  const res = await fetch("/api/v1/token/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });
  if (!res.ok) {
    const err = await res.json().catch(() => ({}));
    throw new Error((err.detail as string) || `Login failed: ${res.status}`);
  }
  return res.json() as Promise<TokenResponse>;
}
