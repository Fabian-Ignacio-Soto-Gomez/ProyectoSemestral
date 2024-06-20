import React, { useState, useTransition } from 'react';
import { useTranslation } from "react-i18next";

const FormularioInscripcion: React.FC = () => {
    const { t } = useTranslation()

    const [formData, setFormData] = useState({
        nombre: '',
        idEstudiante: '',
        email: '',
        telefono: '',
        carrera: '',
        semestre: '',
        promedio: '',
        areaInteres: '',
        empresasPreferidas: '',
        fechaInicio: '',
        fechaFin: '',
        campus: '',
        supervisor: '',
        cv: null,
        cartaMotivacion: null,
        otrosDocumentos: null,
    });

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, files } = e.target;
        if (files && files.length > 0) {
            setFormData({
                ...formData,
                [name]: files[0],
            });
        }
    };

    const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
        e.preventDefault();
        console.log('Form data:', formData);
    };

    return (
        <form
            style={{
                backgroundColor: '#fff',
                padding: '20px',
                borderRadius: '8px',
                boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
                maxWidth: '800px',
                margin: 'auto',
                fontFamily: 'Arial, sans-serif',
                border: '5px solid brown', // Agregar un borde sutil
                marginBottom: '20px', // Agregar espacio debajo del formulario
                fontSize: '1.1rem', // Aumentar el tamaño de la letra
            }}
            onSubmit={handleSubmit}
        >
            <h1 style={{ color: '#333', textAlign: 'center', marginBottom: '30px', fontSize: '2rem'}}>{t("Inscripcion.Section-1.title")}</h1>
            <section style={{ marginBottom: '30px' }}>
                <h2 style={{ color: '#333',marginBottom: '10px', fontSize: '1.5rem' }}>{t("Inscripcion.Section-1.sub-title")}</h2>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-1.name")}:
                    <input
                        type="text"
                        name="nombre"
                        value={formData.nombre}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    />
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-1.rut")}:
                    <input
                        type="text"
                        name="idEstudiante"
                        value={formData.idEstudiante}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    />
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-1.email")}:
                    <input
                        type="email"
                        name="email"
                        value={formData.email}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    />
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-1.phone")}:
                    <input
                        type="tel"
                        name="telefono"
                        value={formData.telefono}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    />
                </label>
            </section>
            <section style={{ marginBottom: '20px' }}>
                <h2 style={{ color: '#333' ,marginBottom: '10px', fontSize: '1.5rem'}}>{t("Inscripcion.Section-2.title")}</h2>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-2.Carrera.title")}:
                    <select
                        name="carrera"
                        value={formData.carrera}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    >
                        <option value="">{t("Inscripcion.Section-2.Carrera.option-1")}</option>
                        <option value="Ingeniería">{t("Inscripcion.Section-2.Carrera.option-2")}</option>
                        <option value="Economía">{t("Inscripcion.Section-2.Carrera.option-3")}l</option>
                        <option value="Derecho">{t("Inscripcion.Section-2.Carrera.option-4")}</option>
                        <option value="Piscología">{t("Inscripcion.Section-2.Carrera.option-5")}</option>
                        <option value="Periodismo">{t("Inscripcion.Section-2.Carrera.option-6")}</option>

                    </select>
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>{t("Inscripcion.Section-2.Campus.title")}:
                    <select
                        name="campus"
                        value={formData.campus}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    >
                        <option value="">{t("Inscripcion.Section-2.Campus.option-1")}</option>
                        <option value="Ingeniería">{t("Inscripcion.Section-2.Campus.option-2")}</option>
                        <option value="Medicina">{t("Inscripcion.Section-2.Campus.option-3")}</option>

                    </select>
                </label>
            </section>
            <section style={{ marginBottom: '20px' }}>
                <h2 style={{ color: '#333' ,marginBottom: '10px', fontSize: '1.5rem'}}>{t("Inscripcion.Section-3.title")}</h2>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-3.Stake.title")}:
                    <select
                        name="areaInteres"
                        value={formData.areaInteres}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    >
                        <option value="">{t("Inscripcion.Section-3.Stake.option-1")}</option>
                        <option value="Desarrollo de Software">{t("Inscripcion.Section-3.Stake.option-2")}</option>
                        <option value="Marketing">{t("Inscripcion.Section-3.Stake.option-3")}</option>
                        <option value="Finanzas">{t("Inscripcion.Section-3.Stake.option-4")}</option>
                        <option value="Investigación">{t("Inscripcion.Section-3.Stake.option-5")}</option>
                    </select>
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-3.Company.title")}:
                    <input
                        type="text"
                        name="empresasPreferidas"
                        value={formData.empresasPreferidas}
                        onChange={handleChange}
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    />
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                {t("Inscripcion.Section-3.Company.date")}:
                    <input
                        type="date"
                        name="fechaInicio"
                        value={formData.fechaInicio}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    />
                    <input
                        type="date"
                        name="fechaFin"
                        value={formData.fechaFin}
                        onChange={handleChange}
                        required
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    />
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                {t("Inscripcion.Section-3.Company.name-supervisor")}:
                    <input
                        type="text"
                        name="supervisor"
                        value={formData.supervisor}
                        onChange={handleChange}
                        style={{
                            width: 'calc(100% - 20px)',
                            padding: '10px',
                            marginTop: '5px',
                            marginBottom: '20px',
                            border: '1px solid #ccc',
                            borderRadius: '4px',
                        }}
                    />
                </label>
            </section>
            <section style={{ marginBottom: '20px' }}>
                <h2 style={{ color: '#333' ,marginBottom: '10px', fontSize: '1.5rem'}}>{t("Inscripcion.Section-4.title")}</h2>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-4.cv")}:
                    <input
                        type="file"
                        name="cv"
                        onChange={handleFileChange}
                        required
                        style={{
                            display: 'block',
                            marginTop: '5px',
                            marginBottom: '20px',
                        }}
                    />
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-4.letter")}:
                    <input
                        type="file"
                        name="cartaMotivacion"
                        onChange={handleFileChange}
                        required
                        style={{
                            display: 'block',
                            marginTop: '5px',
                            marginBottom: '20px',
                        }}
                    />
                </label>
                <label style={{ display: 'block', marginBottom: '10px' }}>
                    {t("Inscripcion.Section-4.document")}:
                    <input
                        type="file"
                        name="otrosDocumentos"
                        onChange={handleFileChange}
                        style={{
                            display: 'block',
                            marginTop: '5px',
                            marginBottom: '20px',
                        }}
                    />
                </label>
            </section>
            <section style={{ marginBottom: '20px' }}>
                <h2 style={{ color: '#333' }}>{t("Inscripcion.Section-5.title")}</h2>
                <p>{t("Inscripcion.Section-5.info")}</p>
            </section>
            <div
                style={{
                    display: 'flex',
                    justifyContent: 'space-between',
                }}
            >
                <button
                    type="submit"
                    style={{
                        padding: '10px 20px',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer',
                        backgroundColor: '#4CAF50',
                        color: 'white',
                    }}
                >
                    {t("Inscripcion.button-1")}
                </button>
                <button
                    type="button"
                    onClick={() => alert('Borrador guardado')}
                    style={{
                        padding: '10px 20px',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer',
                        backgroundColor: '#f0f0f0',
                        color: '#333',
                    }}
                >
                    {t("Inscripcion.button-2")}
                </button>
                <button
                    type="button"
                    onClick={() => alert('Inscripción cancelada')}
                    style={{
                        padding: '10px 20px',
                        border: 'none',
                        borderRadius: '4px',
                        cursor: 'pointer',
                        backgroundColor: '#f0f0f0',
                        color: '#333',
                    }}
                >
                    {t("Inscripcion.button-3")}
                </button>
            </div>
        </form>
    );
};

export default FormularioInscripcion;
