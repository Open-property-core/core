import { AuthProvider, useAuth } from "@/app/providers";
import { HomePage } from "@/pages/home";
import { LoginPage } from "@/pages/login";
import { PropertyListPage } from "@/pages/properties";
import { PartyListPage } from "@/pages/parties";
import { ContractListPage } from "@/pages/contracts";
import { useState } from "react";

type Page = "home" | "properties" | "parties" | "contracts";

function AppContent() {
  const { isAuthenticated, setToken } = useAuth();
  const [page, setPage] = useState<Page>("properties");

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
        <button type="button" onClick={() => setPage("parties")}>
          Parties
        </button>
        <button type="button" onClick={() => setPage("contracts")}>
          Contracts
        </button>
      </nav>
      {page === "home" && <HomePage />}
      {page === "properties" && <PropertyListPage />}
      {page === "parties" && <PartyListPage />}
      {page === "contracts" && <ContractListPage />}
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
