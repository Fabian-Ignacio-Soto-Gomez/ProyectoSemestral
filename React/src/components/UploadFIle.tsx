import axios from "axios"
import { useState } from "react"

export function UploadFileForm (){
    const [selectedFile, SetSelectedFile] = useState('')

    const handleFileUpload = ( e:React.ChangeEvent<any> ) => {
        SetSelectedFile(e.target.files[0])
    }

    const handleSubmit = () => {
        const formData = new FormData()
    
        formData.append("file", selectedFile as any)

        let axiosConfig ={
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }       

        // Agregar link de la carpeta BBDD/Files usando la API
        //Editar el nombre por defecto del archivo por NOMBREUSUARIO-FECHA-NUMEVALUACION
        //Arreglar Peticion POST

        axios.post('http://127.0.0.1:8000/api/upload/', formData, axiosConfig).then( (response) => {
            console.log(response)
        }).catch( (error) => {
            console.log(error)
        })
        // axios.get('http://127.0.0.1:8000/upload/files/').then(response => {console.log(response)}).catch(error => {console.log(error)})
    }
    

    
 return (
    <div>
        <input type="file" onChange={handleFileUpload}/>
        <button className="rounded-md bg-green-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-green-500" onClick={handleSubmit}>Subir</button>
    </div>
 )   
}