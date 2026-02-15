import { apiGet } from "@/shared/api";
import type { Property } from "../model/types";

export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export async function fetchProperties(): Promise<PaginatedResponse<Property>> {
  return apiGet<PaginatedResponse<Property>>("/properties/");
}
