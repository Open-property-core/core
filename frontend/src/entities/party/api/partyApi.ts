import { apiGet, apiPost } from "@/shared/api";
import type { Party, PartyCreateInput } from "../model/types";

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export async function fetchParties(): Promise<PaginatedResponse<Party>> {
  return apiGet<PaginatedResponse<Party>>("/parties/");
}

export async function createParty(data: PartyCreateInput): Promise<Party> {
  return apiPost<Party>("/parties/", data);
}
