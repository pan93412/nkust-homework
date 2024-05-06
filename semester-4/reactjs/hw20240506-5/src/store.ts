import { create } from 'zustand'

export interface MulVariables {
  a: number;
  b: number;
  c: number;
}

export interface MulState extends MulVariables {
  result: () => number;
}

export interface MulActions {
  multiply: (key: keyof MulVariables, val: number) => void;
}

export const useMulStore = create<MulState & MulActions>((set, get) => ({
  a: 1,
  b: 1,
  c: 1,
  result: () => get().a * get().b * get().c,
  multiply: (key, val) => set({ ...get(), [key]: val }),
}))
