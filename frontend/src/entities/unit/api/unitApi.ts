import { apiGet } from "@/shared/api";
import type { Unit } from "../model/types";

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export async function fetchUnits(): Promise<PaginatedResponse<Unit>> {
  return apiGet<PaginatedResponse<Unit>>("/units/");
}
