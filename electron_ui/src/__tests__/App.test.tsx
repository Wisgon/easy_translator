import '@testing-library/jest-dom';
import { render } from '@testing-library/react';
import App from '../main-window-renderer/App';

describe('App', () => {
  it('should render', () => {
    expect(render(<App />)).toBeTruthy();
  });
});
