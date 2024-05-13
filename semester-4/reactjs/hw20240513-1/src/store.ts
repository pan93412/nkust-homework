import { StoreApi, UseBoundStore, create } from 'zustand'

export interface Variables {
  a: number;
  b: number;
  c: number;
}

export interface State extends Variables {
  result: () => number;
}

export interface Actions {
  pushValue: (key: keyof Variables, val: number) => void;
}

export type CalculateStoreHook = UseBoundStore<StoreApi<State & Actions>>;

export const useMulStore: CalculateStoreHook = create<State & Actions>((set, get) => ({
  a: 1,
  b: 1,
  c: 1,
  result: () => get().a * get().b * get().c,
  pushValue: (key, val) => set({ ...get(), [key]: val }),
}))

export const usePlusStore: CalculateStoreHook = create<State & Actions>((set, get) => ({
  a: 1,
  b: 1,
  c: 1,
  result: () => get().a + get().b + get().c,
  pushValue: (key, val) => set({ ...get(), [key]: val }),
}))

export const useMinusStore: CalculateStoreHook = create<State & Actions>((set, get) => ({
  a: 1,
  b: 1,
  c: 1,
  result: () => get().a - get().b - get().c,
  pushValue: (key, val) => set({ ...get(), [key]: val }),
}))

export const useDivStore: CalculateStoreHook = create<State & Actions>((set, get) => ({
  a: 1,
  b: 1,
  c: 1,
  result: () => get().a / get().b / get().c,
  pushValue: (key, val) => set({ ...get(), [key]: val }),
}))
