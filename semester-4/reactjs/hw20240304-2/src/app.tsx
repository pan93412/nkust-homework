interface Product {
  id: number
  title: string
  price: number
}

export function Product({ product }: { product: Product }) {
  return (
    <div>
      <h3>{product.title}</h3>
      <p>NTD${product.price}</p>
    </div>
  );
}

export function Products({ products }: { products: Product[] }) {
  return (
    <div>
      {products.map(product => (
        <Product key={product.id} product={product} />
      ))}
    </div>
  );
}

export function App() {
  return (
    <div>
      <Products products={[
        { id: 1, title: "iPhone 15", price: 50000, },
        { id: 2, title: "Mac", price: 100000, },
        { id: 3, title: "Cheap PC", price: 10000 }
      ]} />
    </div>
  );
}
