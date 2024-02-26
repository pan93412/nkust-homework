import React from 'react'
import ReactDOM from 'react-dom/client'
// import App from './App.tsx'
// import './index.css'

const deviceName = "Galaxy S24 Ultra";
const currentPrice = 49900;

const salePrice = (currentPrice: number, discount: number): number => {
  return currentPrice * discount;
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <p style={{fontSize: 32, fontWeight: 'bold'}}>
      現在 {deviceName} 的售價是 ${currentPrice}，特價{' '}
      ${salePrice(currentPrice, 0.7)}
    </p>
  </React.StrictMode>,
)
