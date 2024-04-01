// Assuming you have an array of blog posts
const blogPosts = [
  {
    id: 1,
    title: "The Future of Web Development",
    author: "Jane Doe",
    date: "March 29, 2024",
    content:
      "The future of web development is full of exciting new technologies...",
  },
  {
    id: 2,
    title: "Understanding React Hooks",
    author: "John Smith",
    date: "April 5, 2024",
    content:
      "React Hooks provide a powerful way to hook into React features...",
  },
  // Add more blog posts here
];

export default function Blog() {
  return (
    <div>
      <h1>Blog</h1>
      {blogPosts.map((post) => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>
            By {post.author} on {post.date}
          </p>
          <div>{post.content}</div>
        </article>
      ))}
    </div>
  );
}
