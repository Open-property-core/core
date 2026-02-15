import { AuthProvider, useAuth } from "@/app/providers";
import { HomePage } from "@/pages/home";
import { LoginPage } from "@/pages/login";
import { PropertyListPage } from "@/pages/properties";
import { useState } from "react";

function AppContent() {
  const { isAuthenticated, setToken } = useAuth();
  const [page, setPage] = useState<"home" | "properties">("properties");

  if (!isAuthenticated) {
    return <LoginPage onLoggedIn={(token) => setToken(token)} />;
  }

  return (
    <div>
      <nav style={{ padding: "0.5rem 1rem", borderBottom: "1px solid #ccc", display: "flex", gap: "1rem" }}>
        <button type="button" onClick={() => setPage("home")}>
          Home
        </button>
        <button type="button" onClick={() => setPage("properties")}>
          Properties
        </button>
      </nav>
      {page === "home" ? <HomePage /> : <PropertyListPage />}
    </div>
  );
}

function App() {
  return (
    <AuthProvider>
      <AppContent />
    </AuthProvider>
  );
}

export default App;
