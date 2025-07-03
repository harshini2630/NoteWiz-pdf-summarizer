const HeroSection = () => {
  return (
    <section style={styles.hero}>
      <h1>Transform Lectures Into Insights</h1>
      <p>Upload audio or video lectures and get beautifully summarized PDFs.</p>
    </section>
  );
};

const styles = {
  hero: {
    textAlign: "center",
    padding: "4rem 1rem 2rem",
    fontSize: "1.2rem",
    color: "#e0e0e0",
  },
};

export default HeroSection;
