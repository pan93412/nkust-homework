export default function AboutPage() {
  return (
    <div>
      <header>
        <h1>About Us</h1>
      </header>
      <main>
        <section>
          <h2>Our Mission</h2>
          <p>
            Our mission is to deliver exceptional service and products that
            enhance the lives of our customers.
          </p>
        </section>
        <section>
          <h2>Our Team</h2>
          <p>
            We are a diverse group of passionate professionals dedicated to
            making a difference in the world.
          </p>
        </section>
        <section>
          <h2>Contact Us</h2>
          <p>
            Have questions? Our team is ready to help. Reach out to us at{" "}
            <a href="mailto:contact@ourcompany.com">contact@ourcompany.com</a>.
          </p>
        </section>
      </main>
      <footer>
        <p>
          &copy; {new Date().getFullYear()} Our Company. All rights reserved.
        </p>
      </footer>
    </div>
  );
}
