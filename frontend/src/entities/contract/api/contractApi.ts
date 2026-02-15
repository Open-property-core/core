import { apiGet, apiPost } from "@/shared/api";
import type { Contract, ContractCreateInput } from "../model/types";

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export async function fetchContracts(): Promise<PaginatedResponse<Contract>> {
  return apiGet<PaginatedResponse<Contract>>("/contracts/");
}

export async function createContract(data: ContractCreateInput): Promise<Contract> {
  const payload = {
    ...data,
    monthly_amount: String(data.monthly_amount),
    status: data.status ?? "draft",
  };
  return apiPost<Contract>("/contracts/", payload);
}
