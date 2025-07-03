const Footer = () => {
  return (
    <footer style={styles.footer}>
      <p>© 2025 NoteWiz · Built with ❤️ for curious minds</p>
    </footer>
  );
};

const styles = {
  footer: {
    textAlign: "center",
    padding: "1.5rem",
    marginTop: "auto",
    background: "rgba(255,255,255,0.05)",
    fontSize: "0.9rem",
    color: "#ccc",
  },
};

export default Footer;
