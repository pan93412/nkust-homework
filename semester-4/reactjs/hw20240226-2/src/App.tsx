import { useState } from 'react'
import "./App.css"

function App() {
  const [counts, setCounts] = useState([0, 0, 0])

  return (
    <div className="counters-container">
      <Counter n={counts[0]} onChange={n => setCounts(c => [n, c[1], c[2]])} />
      <Counter n={counts[1]} onChange={n => setCounts(c => [c[0], n, c[2]])} />
      <Counter n={counts[2]} onChange={n => setCounts(c => [c[0], c[1], n])} />
    </div>
  )
}

function Counter({ n, onChange }: { n: number, onChange: (to: number) => void }) {
  return (
    <div className="container" style={{minWidth: 200}}>
      <button className="chevron chevron-up" onClick={() => onChange(n+1)} />
      <div className="number">{n}</div>
      <button className="chevron chevron-down" onClick={() => onChange(n-1)}/>
    </div>
  )
}

export default App

