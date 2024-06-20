import React from 'react';
import RevisionFormulario from '../components/RevisionFormulario';
import styled from 'styled-components';

const RevisionPage = styled.div`
  .titulo-columnas {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 0;
    border-bottom: 2px solid #000;
    margin-right: 10px; 
    margin-left: 10px; 
  }

  .titulo {
    flex: 1;
    margin-right: 10px;
    font-weight: bold;

    &:last-child {
      margin-right: 0;
    }
  }

  @media (max-width: 768px) {
    .titulo-columnas {
      flex-direction: column;
      margin-left: 10px; 
    }
  }
`;

const Revision: React.FC = () => {
  // Ejemplo de datos (simulados o desde una fuente real como una API)
  const data = [
    { nombre: 'Juan Pérez', archivoPDF: null },
    { nombre: 'María García', archivoPDF: new File(['archivo.pdf'], 'archivo.pdf') }
    // Más datos aquí...
  ];

  const handleAceptar = () => {
    // Lógica para aceptar la pasantía
    console.log('Aceptar pasantía');
  };

  const handleRechazar = () => {
    // Lógica para rechazar la pasantía
    console.log('Rechazar pasantía');
  };

  return (
    <RevisionPage>
      <div className="titulo-columnas">
        <div className="titulo">Nombre del Alumno</div>
        <div className="titulo">Archivo PDF</div>
        <div className="titulo">Aceptar/Rechazar</div>
      </div>
      {data.map((item, index) => (
        <RevisionFormulario
          key={index}
          nombreAlumno={item.nombre}
          archivoPDF={item.archivoPDF}
          onAceptar={handleAceptar}
          onRechazar={handleRechazar}
        />
      ))}
    </RevisionPage>
  );
}

export default Revision;
