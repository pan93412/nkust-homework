import { create } from 'zustand'

export interface CounterState {
  count: number;
}

export interface CounterActions {
  increment: () => void;
  decrement: () => void;
  incrementByAmount: (amount: number) => void;
}

export interface Counter2Actions {
  incrementTwo: () => void;
  decrementTwo: () => void;
}

export interface TextState {
  text: string;
}

export interface TextActions {
  setText: (text: string) => void;
}

export const useCounterStore = create<CounterState & CounterActions>((set) => ({
  count: 0,
  increment: () => set((state) => ({ count: state.count + 1 })),
  decrement: () => set((state) => ({ count: state.count - 1 })),
  incrementByAmount: (amount) => set((state) => ({ count: state.count + amount })),
}))

export const useCounter2Store = create<CounterState & Counter2Actions>((set) => ({
  count: 0,
  incrementTwo: () => set((state) => ({ count: state.count + 2 })),
  decrementTwo: () => set((state) => ({ count: state.count - 2 })),
}))

export const useTextStore = create<TextState & TextActions>((set) => ({
  text: '',
  setText: (text) => set({ text }),
}))
