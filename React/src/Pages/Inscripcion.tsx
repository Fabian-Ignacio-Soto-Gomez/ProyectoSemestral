import React from 'react';
import FormularioInscripcion from '../components/FormularioInscripcion';
import fondoPapel from '../img/fondoPapel.jpg'; 

const Inscripcion: React.FC = () => {
    return (
        <div
            style={{
                fontFamily: 'Arial, sans-serif',
                padding: '20px',
                display: 'flex',
                justifyContent: 'center',
                alignItems: 'center',
                minHeight: '100vh',
                backgroundImage: `url(${fondoPapel})`, 
                backgroundSize: 'cover', 
                backgroundPosition: 'center', 
            }}
        >
            <FormularioInscripcion />
        </div>
    );
};

export default Inscripcion;
