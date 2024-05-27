import "./i18n.ts";

import { createRoot } from 'react-dom/client';
import { App } from "./app.tsx";
import { StrictMode } from 'react';

const root = createRoot(document.getElementById('app')!);
root.render((
    <StrictMode>
        <App />
    </StrictMode>
));
