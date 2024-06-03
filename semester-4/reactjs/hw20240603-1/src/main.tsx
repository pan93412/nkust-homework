import '@mantine/core/styles.css';

import { createRoot } from 'react-dom/client';
import { App } from "./app.tsx";
import { StrictMode } from 'react';

import { createTheme, MantineProvider } from '@mantine/core';

const theme = createTheme({});

const root = createRoot(document.getElementById('app')!);
root.render((
    <StrictMode>
        <MantineProvider theme={theme}>
            <App />
        </MantineProvider>
    </StrictMode>
));
