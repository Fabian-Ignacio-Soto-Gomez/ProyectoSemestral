import { Advance } from "../components/Advance"
import axios from "axios"
import { useEffect, useState } from "react"
import { useLocation, useNavigate } from "react-router-dom"



export function DashboardAlumno(){
    const {state} = useLocation()   
    const { emailState, rolState } = state
    const navigate = useNavigate()

    const [rut, setRut] = useState("")
    const [email, setEmail] = useState("")
    const [name, setName] = useState("")
    const [avance1, setAvance1] = useState(false)
    const [avance2, setAvance2] = useState(false)
    const [avance3, setAvance3] = useState(false)

    const [nota1, setNota1] = useState(1)
    const [nota2, setNota2] = useState(1)
    const [nota3, setNota3] = useState(1)
    const [comentario1, setComentario1] = useState("")
    const [comentario2, setComentario2] = useState("")
    const [comentario3, setComentario3] = useState("")

    function handleInfoStudent() {
        setEmail(emailState)
        console.log(emailState)
        const data = {
            "email": email
        }
        axios.post('http://127.0.0.1:8000/api/student/', data).then(
            (response) => {
                setRut(response.data.rut)
                setName(response.data.name)
                setAvance1(response.data.avance_1)
                setAvance2(response.data.avance_2)
                setAvance3(response.data.avance_3)
            }
        ).catch( (error) => {
            console.log(error)
        })
    }

    function handleCourseInfoStudent() {
        const data = {
            "rut": rut
        }
        axios.post('http://127.0.0.1:8000/api/studentpercourse/', data).then(
            (response) => {
                setNota1(response.data.nota_1)
                setNota2(response.data.nota_2)
                setNota3(response.data.nota_3)
                setComentario1(response.data.comentario_1)
                setComentario2(response.data.comentario_2)
                setComentario3(response.data.comentario_3)
            }
        ).catch( (error) => {
            console.log(error)
        })
    }
    useEffect( () => {
        handleInfoStudent()
        handleCourseInfoStudent()
    }, [[],])
    
    return (
        <div className="flex flex-row">
            <div className="flex flex-col">
                <p>{name}</p>
                <div><Advance avance={avance1} nota={nota1} comentario={comentario1} /></div>
                <div><Advance avance={avance2} nota={nota2} comentario={comentario2} /></div>
                <div><Advance avance={avance3} nota={nota3} comentario={comentario3} /></div>
            </div>
        </div>
    )
}