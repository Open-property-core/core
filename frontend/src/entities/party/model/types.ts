/** Party entity (matches API). */
export interface Party {
  id: number;
  name: string;
  party_type: string;
  email: string;
  phone: string;
  created_at: string;
  updated_at: string;
}

export interface PartyCreateInput {
  name: string;
  party_type: string;
  email?: string;
  phone?: string;
}
