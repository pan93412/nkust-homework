export function Name({ name }: { name: string }) {
  return <h1>Hello, {name}!</h1>
}

export function App() {
  return (
    <div>
      <Name name="Pan" />
    </div>
  )
}
