import { Channels } from 'main-window/preload';

declare global {
  interface Window {
    electron: {
      ipcRenderer: {
        openbuttonWindow(): void;
        sendMessage(channel: Channels, args: unknown[]): void;
        on(
          channel: Channels,
          func: (...args: unknown[]) => void
        ): (() => void) | undefined;
        once(channel: Channels, func: (...args: unknown[]) => void): void;
      };
    };
  }
}

export {};
