/** Contract entity (matches API). */
export interface Contract {
  id: number;
  unit: number;
  party: number;
  start_date: string;
  end_date: string;
  monthly_amount: string;
  status: string;
  created_at: string;
  updated_at: string;
}

export interface ContractCreateInput {
  unit: number;
  party: number;
  start_date: string;
  end_date: string;
  monthly_amount: string | number;
  status?: string;
}
