import { createContext, useCallback, useContext, useState } from "react";
import { getStoredToken, clearStoredToken } from "@/shared/api";

type AuthContextValue = {
  token: string | null;
  isAuthenticated: boolean;
  logout: () => void;
  setToken: (token: string | null) => void;
};

const AuthContext = createContext<AuthContextValue | null>(null);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [token, setTokenState] = useState<string | null>(getStoredToken);

  const setToken = useCallback((t: string | null) => {
    if (t) localStorage.setItem("opc_access_token", t);
    else clearStoredToken();
    setTokenState(t);
  }, []);

  const logout = useCallback(() => {
    clearStoredToken();
    setTokenState(null);
  }, []);

  const value: AuthContextValue = {
    token,
    isAuthenticated: !!token,
    logout,
    setToken,
  };

  return (
    <AuthContext.Provider value={value}>{children}</AuthContext.Provider>
  );
}

export function useAuth(): AuthContextValue {
  const ctx = useContext(AuthContext);
  if (!ctx) throw new Error("useAuth must be used within AuthProvider");
  return ctx;
}
