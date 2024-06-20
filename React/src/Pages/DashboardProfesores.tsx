import axios from "axios";
import { useEffect, useState } from "react";
import { StudentInfo } from "../components/StudentInfo";


export function DashboardProfesor(){
  const [students, setStudents] = useState([])
  const [loading, setLoading] = useState(true)


  async function handleCourseinfo(){
    const data = {
      "rut": "100000-1",
      "id": "PO1"
    }
    try {
      const response = await axios.post('http://127.0.0.1:8000/api/courseinfo/', data)
      setStudents(response.data)
    } catch (error) {
      console.log(error)
    } finally {
      setLoading(false)
    }
    
  }

  useEffect(() => {
    handleCourseinfo()
  }, [loading])

  return (
    <div className="flex flex-col">
      <div>
        <p className="text-xl">Avance 1</p>
        <input type="file" />
        {
          students.map((data:{
            rut_student:string,
            nota_1:number,
            comentario_1:string,
          }) => (
            <StudentInfo rut={data.rut_student} nota={data.nota_1} comentario={data.comentario_1} num={0} />
          ))
        }
      </div>
      <div>
      <p className="text-xl">Avance 2</p>
      <input type="file" />
        {
          students.map((data:{
            rut_student:string,
            nota_2:number,
            comentario_2:string,
          }) => (
            <StudentInfo rut={data.rut_student} nota={data.nota_2} comentario={data.comentario_2} num={1} />
          ))
        }
      </div>
      <div>
      <p className="text-xl">Avance 3</p>
      <input type="file" />
        {
          students.map((data:{
            rut_student:string,
            nota_3:number,
            comentario_3:string,
          }) => (
            <StudentInfo rut={data.rut_student} nota={data.nota_3} comentario={data.comentario_3} num={2} />
          ))
        }
      </div>
      
    </div>
  )
}