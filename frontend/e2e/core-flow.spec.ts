import { test, expect } from "@playwright/test";

const USERNAME = process.env.E2E_USER ?? "admin";
const PASSWORD = process.env.E2E_PASSWORD ?? "admin";
const API_BASE = process.env.E2E_API_BASE ?? "http://localhost:8080/api/v1";

async function getToken(): Promise<string> {
  const res = await fetch(`${API_BASE}/token/`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username: USERNAME, password: PASSWORD }),
  });
  if (!res.ok) throw new Error(`Login failed: ${res.status}`);
  const data = await res.json();
  return data.access;
}

async function apiPost(token: string, path: string, body: unknown): Promise<unknown> {
  const res = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${token}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  });
  if (!res.ok) throw new Error(`API ${path} failed: ${res.status}`);
  return res.json();
}

test("core flow: login, create property/unit/party/contract, assert contract appears", async ({
  page,
}) => {
  await page.goto("/");

  // Login via UI
  await expect(page.getByLabel("Username")).toBeVisible();
  await page.getByLabel("Username").fill(USERNAME);
  await page.getByLabel("Password").fill(PASSWORD);
  await page.getByRole("button", { name: /sign in/i }).click();

  // Wait for nav (Properties button visible = logged in)
  await expect(page.getByRole("button", { name: "Properties" })).toBeVisible();

  // Create property, unit, party, contract via API
  const token = await getToken();
  const property = (await apiPost(token, "/properties/", {
    name: "E2E Test Property",
    address: "123 Test St",
    property_type: "residential",
    status: "active",
  })) as { id: number };
  const unit = (await apiPost(token, "/units/", {
    property: property.id,
    name: "Unit 101",
    area: "50",
    status: "available",
  })) as { id: number };
  const party = (await apiPost(token, "/parties/", {
    name: "E2E Test Party",
    party_type: "tenant",
    email: "test@example.com",
  })) as { id: number };
  const startDate = new Date();
  const endDate = new Date();
  endDate.setFullYear(endDate.getFullYear() + 1);
  await apiPost(token, "/contracts/", {
    unit: unit.id,
    party: party.id,
    start_date: startDate.toISOString().slice(0, 10),
    end_date: endDate.toISOString().slice(0, 10),
    monthly_amount: "1000",
    status: "active",
  });

  // Open Contracts page and assert
  await page.getByRole("button", { name: "Contracts" }).click();
  await expect(page.getByText("E2E Test Party")).toBeVisible();
  await expect(page.getByText("Unit 101")).toBeVisible();
});
