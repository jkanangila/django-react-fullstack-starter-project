import React, {
  createContext,
  useRef,
  useCallback,
  useContext,
  useSyncExternalStore,
} from "react";

export default function ContextCreator<T>(initialState: T) {
  function useStoreData(): {
    get: () => T;
    set: (value: Partial<T>) => void;
    subscribe: (callback: () => void) => () => void;
  } {
    const store = useRef(initialState);

    const subscribers = useRef(new Set<() => void>());

    const get = useCallback(() => store.current, []);

    const set = useCallback((value: Partial<T>) => {
      store.current = { ...store.current, ...value };
      subscribers.current.forEach((callback) => callback());
    }, []);

    const subscribe = useCallback((callback: () => void) => {
      subscribers.current.add(callback);

      return () => subscribers.current.delete(callback);
    }, []);

    return {
      get,
      set,
      subscribe,
    };
  }

  type UseStoreDataReturnType = ReturnType<typeof useStoreData>;

  const StoreContext = createContext<UseStoreDataReturnType | null>(null);

  const StoreProvider: React.FC<{ children: React.ReactNode }> = ({
    children,
  }) => {
    return (
      <StoreContext.Provider value={useStoreData()}>
        {children}
      </StoreContext.Provider>
    );
  };

  function useStore<K>(
    selector: (store: T) => K
  ): [K, (value: Partial<T>) => void] {
    const store = useContext(StoreContext)!;
    if (!store) {
      throw new Error("useStore called outside of StoreContext");
    }

    const state = useSyncExternalStore(
      store.subscribe,
      () => selector(store.get()),
      () => selector(initialState)
    );

    return [state, store.set];
  }

  return { StoreProvider, useStore };
}
