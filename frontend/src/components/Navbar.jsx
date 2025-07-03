const Navbar = () => {
  return (
    <nav style={styles.navbar}>
      <h2 style={styles.logo}>🎧 NoteWiz</h2>
    </nav>
  );
};

const styles = {
  navbar: {
    padding: "1rem 2rem",
    backgroundColor: "rgba(255,255,255,0.05)",
    backdropFilter: "blur(10px)",
    borderBottom: "1px solid rgba(255,255,255,0.1)",
  },
  logo: {
    fontSize: "1.8rem",
    background: "linear-gradient(to right, #ff4d00, #ffae00)",
    WebkitBackgroundClip: "text",
    WebkitTextFillColor: "transparent",
  },
};

export default Navbar;
