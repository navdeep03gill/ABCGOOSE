import { useState, createContext, useContext } from "react";

export const NumGameContext = createContext();

export function useNumGameContext() {
  return useContext(NumGameContext);
}
