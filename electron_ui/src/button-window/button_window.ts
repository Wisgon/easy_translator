/* eslint global-require: off, no-console: off, promise/always-return: off, import/prefer-default-export: off */

import path from 'path';
import { app, BrowserWindow, shell } from 'electron';
import { resolveHtmlPath } from '../main-window/util';

let buttonWindow: BrowserWindow | null = null;

const isDebug =
  process.env.NODE_ENV === 'development' || process.env.DEBUG_PROD === 'true';

const installExtensions = async () => {
  const installer = require('electron-devtools-installer');
  const forceDownload = !!process.env.UPGRADE_EXTENSIONS;
  const extensions = ['REACT_DEVELOPER_TOOLS'];

  return installer
    .default(
      extensions.map((name) => installer[name]),
      forceDownload
    )
    .catch(console.log);
};

export const createWindow = async (arg: any) => {
  if (isDebug) {
    await installExtensions();
  }

  const RESOURCES_PATH = app.isPackaged
    ? path.join(process.resourcesPath, 'assets')
    : path.join(__dirname, '../../assets');

  const getAssetPath = (...paths: string[]): string => {
    return path.join(RESOURCES_PATH, ...paths);
  };
  buttonWindow = new BrowserWindow({
    frame: false, // unshow minimize maxmize and so on from window, create a no frame window
    show: false,
    width: 150,
    height: 50,
    x: arg.x, // control the x-axis position of window
    y: arg.y, // control the y-axis position of window
    icon: getAssetPath('icon.png'),
    webPreferences: {
      preload: app.isPackaged
        ? path.join(__dirname, 'preload.js')
        : path.join(__dirname, '../../.erb/dll/preload.js'),
      devTools: false, // do not show devtools
    },
  });

  buttonWindow.loadURL(resolveHtmlPath('button_window.html'));
  buttonWindow.setMenu(null); // do not show menu

  buttonWindow.on('ready-to-show', () => {
    if (!buttonWindow) {
      throw new Error('"buttonWindow" is not defined');
    }

    buttonWindow.show();
  });

  buttonWindow.on('closed', () => {
    buttonWindow = null;
  });

  // Open urls in the user's browser
  buttonWindow.webContents.setWindowOpenHandler((edata) => {
    shell.openExternal(edata.url);
    return { action: 'deny' };
  });

  return buttonWindow;
};

export const closeWindow = async (arg: any) => {
  if (buttonWindow != null) {
    buttonWindow.close();
  }
};
