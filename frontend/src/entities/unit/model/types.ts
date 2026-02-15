/** Unit entity (matches API). */
export interface Unit {
  id: number;
  property: number;
  name: string;
  area: number | null;
  status: string;
  created_at: string;
  updated_at: string;
}
