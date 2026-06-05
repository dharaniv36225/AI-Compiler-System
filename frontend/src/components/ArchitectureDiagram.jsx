export default function ArchitectureDiagram({
  architecture,
}) {
  if (!architecture) return null;

  return (
    <div className="diagram-card">
      <h2>🏗 Architecture Diagram</h2>

      <div className="diagram">
        <div className="diagram-box">
          <h3>Entities</h3>

          {architecture.entities?.map((item) => (
            <span key={item}>{item}</span>
          ))}
        </div>

        <div className="arrow">➡</div>

        <div className="diagram-box">
          <h3>Pages</h3>

          {architecture.pages?.map((item) => (
            <span key={item}>{item}</span>
          ))}
        </div>

        <div className="arrow">➡</div>

        <div className="diagram-box">
          <h3>Roles</h3>

          {architecture.roles?.map((item) => (
            <span key={item}>{item}</span>
          ))}
        </div>
      </div>
    </div>
  );
}