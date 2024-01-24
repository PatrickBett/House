import "./Footer.css";

export default function Footer() {
  const currentYear = new Date().getFullYear();
  const myName = "Keja Yangu Developers Ltd";
  return (
    <div>
      <footer id="footer">
        <p>
          &copy; {myName} {currentYear} . All rights reserved.
        </p>
      </footer>
    </div>
  );
}
