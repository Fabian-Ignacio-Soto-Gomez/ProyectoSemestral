import React from 'react';
import styled from 'styled-components';

// Estilos utilizando styled-components
const FormularioRow = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #ccc;
  padding: 10px 0;

  &:not(:last-child) {
    border-bottom: 1px solid #ccc;
  }

  @media (max-width: 768px) {
    flex-direction: column;
  }
`;

const FormularioColumn = styled.div`
  flex: 1;
  margin-right: 10px;

  &:last-child {
    margin-right: 0;
  }
`;

const BotonAceptar = styled.button`
  padding: 5px 10px;
  cursor: pointer;
  border: none;
  border-radius: 4px;
  color: #fff;
  font-size: 14px;
  margin-right: 5px;
  background-color: #5cb85c; /* Verde */
`;

const BotonRechazar = styled.button`
  padding: 5px 10px;
  cursor: pointer;
  border: none;
  border-radius: 4px;
  color: #fff;
  font-size: 14px;
  background-color: #d9534f; /* Rojo */
`;

interface RevisionFormularioProps {
  nombreAlumno: string;
  archivoPDF: File | null;
  onAceptar: () => void;
  onRechazar: () => void;
}

const RevisionFormulario: React.FC<RevisionFormularioProps> = ({
  nombreAlumno,
  archivoPDF,
  onAceptar,
  onRechazar
}) => {
  return (
    <FormularioRow>
      <FormularioColumn>
        {nombreAlumno}
      </FormularioColumn>
      <FormularioColumn>
        {archivoPDF ? archivoPDF.name : 'Archivo no seleccionado'}
      </FormularioColumn>
      <FormularioColumn>
        <BotonAceptar onClick={onAceptar}>Aceptar</BotonAceptar>
        <BotonRechazar onClick={onRechazar}>Rechazar</BotonRechazar>
      </FormularioColumn>
    </FormularioRow>
  );
}

export default RevisionFormulario;
